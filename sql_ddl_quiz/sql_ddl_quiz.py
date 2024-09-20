# sql_ddl_quiz.py
# Ensure necessary libraries are installed
# You can uncomment and run these lines if the libraries are not already installed
# !pip install ipywidgets requests pandas

import sqlite3
import json
import requests
from IPython.display import clear_output, display
import pandas as pd
from ipywidgets import (
    Textarea, Button, VBox, HBox, Output, HTML, Layout, IntProgress
)

class SQLDDLQuiz:
    def __init__(self, questions_source):
        """
        Initialize the SQL Quiz.

        Args:
            questions_source (dict or list or str):
                - If dict/list: Directly provides the quiz questions.
                - If str: URL to a JSON file containing the quiz questions.
        """
        self.output = Output()
        self.comparison_output = Output()
        self.progress = IntProgress(
            value=0,
            min=0,
            max=100,
            description='Progress:',
            bar_style='info',
            style={'description_width': 'initial'},
            layout=Layout(width='100%')
        )
        self.load_questions(questions_source)
        self.current_question = 0
        self.correct_answers = 0
        self.create_widgets()
        if self.quiz:
            self.load_question()
        else:
            self.display_error("No quiz questions available.")

    def load_questions(self, source):
        """Load quiz questions from a dict/list or a JSON URL."""
        if isinstance(source, str):
            try:
                response = requests.get(source)
                response.raise_for_status()
                self.quiz = response.json()
            except Exception as e:
                self.quiz = []
                self.display_error(f"Failed to load questions from URL: {e}")
        elif isinstance(source, (dict, list)):
            self.quiz = source
        else:
            self.quiz = []
            self.display_error("Invalid questions source provided.")

    def display_error(self, message):
        """Display an error message."""
        with self.output:
            display(HTML(f"<div style='color: red; font-weight: bold;'>{message}</div>"))

    def create_widgets(self):
        """Create and layout all UI widgets."""
        # Display elements
        self.question_label = HTML()
        self.schema_display = HTML()

        # SQL input area with placeholder behavior
        self.sql_input = Textarea(
            value='',
            placeholder='-- Write your SQL query here',
            description='Your SQL:',
            layout=Layout(width='100%', height='120px')
        )

        # Buttons
        self.submit_button = Button(
            description='Submit',
            button_style='primary',
            layout=Layout(width='100px')
        )
        self.retry_button = Button(
            description='Retry',
            button_style='warning',
            layout=Layout(width='100px', display='none')
        )
        self.next_button = Button(
            description='Next',
            button_style='success',
            layout=Layout(width='100px', display='none')
        )

        # Bind button events
        self.submit_button.on_click(self.on_submit)
        self.retry_button.on_click(self.on_retry)
        self.next_button.on_click(self.on_next)

        # Buttons layout
        self.buttons_box = HBox([
            self.submit_button,
            self.retry_button,
            self.next_button
        ], layout=Layout(justify_content='center', gap='10px'))

        # Main layout
        self.quiz_layout = VBox([
            self.progress,
            self.schema_display,
            self.question_label,
            self.sql_input,
            self.buttons_box,
            self.output,
            self.comparison_output  # Add comparison output below main output
        ], layout=Layout(padding='20px', border='solid 1px #ddd', border_radius='10px', width='800px'))

    def load_question(self):
        """Load and display the current question."""
        clear_output(wait=True)
        display(self.quiz_layout)

        if self.current_question >= len(self.quiz):
            self.display_completion()
            return

        question = self.quiz[self.current_question]

        # Update progress bar
        progress_percentage = ((self.current_question) / len(self.quiz)) * 100
        self.progress.value = progress_percentage

        # Execute setup SQL to determine table schemas
        temp_conn = sqlite3.connect(':memory:')
        try:
            temp_conn.executescript(question.get('setup', ''))
        except Exception as e:
            self.schema_display.value = f"<h3 style='color: red;'>Error in setup SQL:</h3><p>{e}</p>"
            temp_conn.close()
            return

        # Get table schemas
        schema_html = self.get_table_schemas(temp_conn)
        self.schema_display.value = f"<h3>Table Schema:</h3>{schema_html}"
        temp_conn.close()

        # Display the question
        self.question_label.value = f"<h2>Question {self.current_question + 1} of {len(self.quiz)}:</h2><p>{question.get('question', '')}</p>"

        # Reset input and buttons
        self.sql_input.value = ''
        self.output.clear_output()
        self.comparison_output.clear_output()
        self.submit_button.layout.display = 'inline-block'
        self.retry_button.layout.display = 'none'
        self.next_button.layout.display = 'none'

    def get_table_schemas(self, connection):
        """Retrieve and format table schemas from the SQLite connection."""
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        schema_html = ""
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            # Sort columns alphabetically by name
            columns_sorted = sorted(columns, key=lambda x: x[1].lower())
            if columns_sorted:
                schema_html += f"<b>{table_name}:</b><br>"
                schema_html += "<ul>"
                for col in columns_sorted:
                    col_name = col[1]
                    col_type = col[2]
                    not_null = "NOT NULL" if col[3] else ""
                    pk = "PRIMARY KEY" if col[5] else ""
                    schema_html += f"<li>{col_name} ({col_type}) {not_null} {pk}</li>"
                schema_html += "</ul>"
        return schema_html

    def on_submit(self, button):
        """Handle the submit button click."""
        with self.output:
            self.output.clear_output()
            question = self.quiz[self.current_question]
            student_query = self.sql_input.value.strip()

            if not student_query:
                display(HTML("<span style='color: red;'>Please enter a valid SQL query.</span>"))
                return

            result, feedback = self.check_answer(
                student_query,
                question.get('answer', ''),
                question.get('setup', '')
            )
            if result:
                self.correct_answers += 1
                display(HTML("<span style='color: green; font-weight: bold;'>Correct!</span>"))
                self.submit_button.layout.display = 'none'
                self.retry_button.layout.display = 'none'
                self.next_button.layout.display = 'inline-block'
            else:
                display(HTML("<span style='color: red; font-weight: bold;'>Incorrect. Please try again.</span>"))
                self.retry_button.layout.display = 'inline-block'
                # Display schemas and data comparison
                self.display_comparison()

    def check_answer(self, student_query, correct_query, setup_query):
        """Compare the student's query against the correct answer."""
        # Initialize in-memory databases
        student_conn = sqlite3.connect(':memory:')
        correct_conn = sqlite3.connect(':memory:')

        try:
            # Apply setup queries
            student_conn.executescript(setup_query)
            correct_conn.executescript(setup_query)

            # Execute student's query
            student_conn.executescript(student_query)
        except Exception as e:
            with self.output:
                display(HTML(f"<h3 style='color: red;'>Error in your SQL query:</h3><p>{e}</p>"))
            student_conn.close()
            correct_conn.close()
            return False, None

        try:
            # Execute correct query
            correct_conn.executescript(correct_query)
        except Exception as e:
            # This should not happen if the correct query is valid
            with self.output:
                display(HTML(f"<h3 style='color: red;'>Error in the correct SQL query:</h3><p>{e}</p>"))
            student_conn.close()
            correct_conn.close()
            return False, None

        # Get list of tables after setup
        student_tables = self.get_tables(student_conn)
        correct_tables = self.get_tables(correct_conn)

        # Compare table lists
        if set(student_tables) != set(correct_tables):
            with self.output:
                display(HTML("<h3 style='color: red;'>Tables mismatch.</h3>"))
            student_conn.close()
            correct_conn.close()
            return False, None

        # Compare each table's data
        all_match = True
        for table in student_tables:
            match, _, _ = self.compare_table_data(student_conn, correct_conn, table)
            if not match:
                all_match = False

        student_conn.close()
        correct_conn.close()
        return all_match, None

    def get_tables(self, connection):
        """Retrieve a list of table names from the SQLite connection."""
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        return tables

    def compare_table_data(self, student_conn, correct_conn, table_name):
        """Compare data in a specific table between student and correct databases."""
        try:
            student_df = pd.read_sql_query(f"SELECT * FROM {table_name} ORDER BY ROWID;", student_conn)
            correct_df = pd.read_sql_query(f"SELECT * FROM {table_name} ORDER BY ROWID;", correct_conn)
            # Sort columns alphabetically by name
            student_df = student_df.reindex(sorted(student_df.columns), axis=1)
            correct_df = correct_df.reindex(sorted(correct_df.columns), axis=1)
            # Compare DataFrames
            match = student_df.equals(correct_df)
            return match, student_df, correct_df
        except Exception as e:
            with self.output:
                display(HTML(f"<h3 style='color: red;'>Error comparing table '{table_name}':</h3><p>{e}</p>"))
            return False, pd.DataFrame(), pd.DataFrame()

    def display_comparison(self):
        """Display the user's and expected schema and data after an incorrect answer."""
        question = self.quiz[self.current_question]
        setup_query = question.get('setup', '')
        correct_query = question.get('answer', '')
        student_query = self.sql_input.value.strip()

        # Initialize in-memory databases
        student_conn = sqlite3.connect(':memory:')
        correct_conn = sqlite3.connect(':memory:')

        try:
            # Apply setup queries
            student_conn.executescript(setup_query)
            correct_conn.executescript(setup_query)

            # Execute student's query
            student_conn.executescript(student_query)

            # Execute correct query
            correct_conn.executescript(correct_query)
        except Exception as e:
            with self.comparison_output:
                display(HTML(f"<h3 style='color: red;'>Error during comparison:</h3><p>{e}</p>"))
            student_conn.close()
            correct_conn.close()
            return

        # Get table schemas
        student_schema = self.get_table_schemas(student_conn)
        correct_schema = self.get_table_schemas(correct_conn)

        # Get tables
        student_tables = self.get_tables(student_conn)
        correct_tables = self.get_tables(correct_conn)

        # Prepare HTML for schemas
        schemas_html = f"""
            <h3>Schema Comparison:</h3>
            <div class="diff-container">
                <div class="diff-table">
                    <b>Your Schema:</b><br>{student_schema}
                </div>
                <div class="diff-table">
                    <b>Expected Schema:</b><br>{correct_schema}
                </div>
            </div>
        """

        # Prepare HTML for data
        data_html = "<h3>Data Comparison:</h3><div class='diff-container'>"
        for table in student_tables:
            try:
                student_df = pd.read_sql_query(f"SELECT * FROM {table} ORDER BY ROWID;", student_conn)
                correct_df = pd.read_sql_query(f"SELECT * FROM {table} ORDER BY ROWID;", correct_conn)
                # Sort columns alphabetically by name
                student_df = student_df.reindex(sorted(student_df.columns), axis=1)
                correct_df = correct_df.reindex(sorted(correct_df.columns), axis=1)
                data_html += f"""
                    <div class="diff-table">
                        <b>Your Data - {table}:</b><br>{student_df.to_html(index=False)}
                    </div>
                    <div class="diff-table">
                        <b>Expected Data - {table}:</b><br>{correct_df.to_html(index=False)}
                    </div>
                """
            except Exception as e:
                data_html += f"""
                    <div class="diff-table">
                        <b>Error comparing table '{table}':</b><br>{e}
                    </div>
                """
        data_html += "</div>"

        # Combine schemas and data
        comparison_html = schemas_html + data_html

        # Inject CSS for comparison layout
        with self.comparison_output:
            display(HTML("""
                <style>
                    .diff-container {
                        display: flex;
                        flex-wrap: wrap;
                        gap: 20px;
                        margin-bottom: 20px;
                    }
                    .diff-table {
                        flex: 1;
                        min-width: 300px;
                        padding: 10px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        overflow-x: auto;
                        background-color: #f9f9f9;
                    }
                </style>
            """))
            display(HTML(comparison_html))

        student_conn.close()
        correct_conn.close()

    def on_retry(self, button):
        """Handle the retry button click."""
        self.load_question()

    def on_next(self, button):
        """Handle the next button click."""
        self.current_question += 1
        if self.current_question < len(self.quiz):
            self.load_question()
        else:
            self.display_completion()

    def display_completion(self):
        """Display a completion message and final score."""
        clear_output(wait=True)
        display(self.quiz_layout)
        # Update progress to 100%
        self.progress.value = 100
        completion_message = f"""
        <h2>Congratulations! You've completed the quiz.</h2>
        <p>Your Score: {self.correct_answers} out of {len(self.quiz)}</p>
        """
        with self.output:
            display(HTML(completion_message))
        # Hide input and buttons
        self.sql_input.layout.display = 'none'
        self.buttons_box.layout.display = 'none'
        self.comparison_output.layout.display = 'none'


# Provide a URL to a JSON file containing the questions
# Ensure that the URL points to a JSON file with the correct structure
# quiz_url = 'https://github.com/brendanpshea/database_sql/raw/main/sql_ddl_quiz/sqy_sql_ddl_quiz.json'
# Instantiate and display the quiz
# Use either quiz_questions or quiz_url
# sql_quiz = SQLDDLQuiz(quiz_questions)
# sql_quiz = SQLDDLQuiz(quiz_url)
