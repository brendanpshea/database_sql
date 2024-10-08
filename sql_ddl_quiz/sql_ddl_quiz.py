# sql_ddl_quiz.py

import sqlite3
import requests
from IPython.display import clear_output, display
import pandas as pd
from ipywidgets import (
    Textarea, Button, VBox, HBox, Output, HTML, Layout, IntProgress, Tab, Dropdown
)

class SQLDDLQuiz:
    """A class representing the SQL DDL Quiz."""

    def __init__(self, questions_source):
        """
        Initialize the SQLDDLQuiz.

        Args:
            questions_source (dict or list or str):
                - If dict/list: Directly provides the quiz questions.
                - If str: URL to a JSON file containing the quiz questions.
        """
        self.quiz = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.student_conn = None  # SQLite connection for the student's database
        self.answered_questions = {}  # Track answered questions: {index: is_correct}

        self.output = Output()
        self.comparison_output = Output()
        self.table_output = Output()

        # Initialize Progress Bar
        self.initialize_progress_bar()

        # Load quiz questions
        self.load_questions(questions_source)

        # Create UI Widgets
        self.create_widgets()

        if self.quiz:
            self.load_question()
        else:
            self.display_error("No quiz questions available.")

    # ----------------- Initialization Methods -----------------

    def initialize_progress_bar(self):
        """Initialize the progress bar widget."""
        self.progress = IntProgress(
            value=0,
            min=0,
            max=100,
            description='Progress:',
            bar_style='info',
            style={'description_width': 'initial'},
            layout=Layout(width='100%')
        )

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

    # ----------------- UI Creation Methods -----------------

    def create_widgets(self):
        """Create and layout all UI widgets."""
        # Create Quiz Tab Widgets
        self.create_quiz_widgets()
        # Create View Tables Tab Widgets
        self.create_table_view_widgets()
        # Create Tab Layout
        self.create_tabs()

    def create_quiz_widgets(self):
        """Create UI widgets for the quiz tab."""
        # Display elements
        self.question_label = HTML()
        self.schema_display = HTML()

        # Question selector dropdown
        self.question_selector = Dropdown(
            options=[(f"Question {i+1}", i) for i in range(len(self.quiz))],
            description='Go to:',
            value=self.current_question_index,
            layout=Layout(width='200px')
        )
        self.question_selector.observe(self.on_question_change, names='value')

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

        # Main Quiz layout
        self.quiz_layout = VBox([
            self.progress,
            HBox([self.schema_display, self.question_selector], layout=Layout(justify_content='space-between')),
            self.question_label,
            self.sql_input,
            self.buttons_box,
            self.output,
            self.comparison_output  # Add comparison output below main output
        ], layout=Layout(padding='20px', border='solid 1px #ddd', border_radius='10px', width='800px'))

    def create_table_view_widgets(self):
        """Create UI widgets for the table view tab."""
        # Create Table View layout
        self.table_view_layout = VBox([
            HTML("<h2>Current Tables Content</h2>"),
            self.table_output
        ], layout=Layout(padding='20px', border='solid 1px #ddd', border_radius='10px', width='800px'))

    def create_tabs(self):
        """Create the tab layout with Quiz and View Tables."""
        # Create Tab widget with Quiz and View Tables
        self.tabs = Tab(children=[self.quiz_layout, self.table_view_layout])
        self.tabs.set_title(0, 'Quiz')
        self.tabs.set_title(1, 'View Tables')

        # Display the Tab widget
        display(self.tabs)

    # ----------------- Question Handling Methods -----------------

    def load_question(self):
        """Load and display the current question."""
        # Update the dropdown value without triggering the event
        self.question_selector.unobserve(self.on_question_change, names='value')
        self.question_selector.value = self.current_question_index
        self.question_selector.observe(self.on_question_change, names='value')

        # Reset student connection for the new question
        try:
            self.reset_student_connection()
            question = self.get_current_question()
            setup_sql = question.get('setup', '')
            self.execute_setup_sql(setup_sql)
        except Exception as e:
            self.schema_display.value = f"<h3 style='color: red;'>{e}</h3>"
            return

        # Update progress bar
        progress_percentage = ((len(self.answered_questions)) / len(self.quiz)) * 100
        self.progress.value = progress_percentage

        # Get table schemas from student connection
        schema_html = self.get_table_schemas(self.student_conn)
        self.schema_display.value = f"<h3>Table Schema:</h3>{schema_html}"

        # Display the question
        self.question_label.value = f"<h2>Question {self.current_question_index + 1} of {len(self.quiz)}:</h2><p>{question.get('question', '')}</p>"

        # Reset input and outputs
        self.reset_ui_elements()

        # Check if the question was already answered
        if self.current_question_index in self.answered_questions:
            is_correct = self.answered_questions[self.current_question_index]
            if is_correct:
                with self.output:
                    display(HTML("<span style='color: green; font-weight: bold;'>You have already answered this question correctly.</span>"))
                self.update_button_states(correct=True)
            else:
                with self.output:
                    display(HTML("<span style='color: red; font-weight: bold;'>You have previously attempted this question.</span>"))
                self.update_button_states(correct=False)

        # Refresh the table view
        self.refresh_table_view()

    def reset_ui_elements(self):
        """Reset the input fields and button states."""
        self.sql_input.value = ''
        self.output.clear_output()
        self.comparison_output.clear_output()
        self.submit_button.layout.display = 'inline-block'
        self.retry_button.layout.display = 'none'
        self.next_button.layout.display = 'none'

    def get_current_question(self):
        """Get the current question."""
        if 0 <= self.current_question_index < len(self.quiz):
            return self.quiz[self.current_question_index]
        else:
            return None

    def reset_student_connection(self):
        """Reset the student SQLite connection."""
        if self.student_conn:
            self.student_conn.close()
        self.student_conn = sqlite3.connect(':memory:')

    def execute_setup_sql(self, setup_sql):
        """Execute the setup SQL on the student connection."""
        try:
            self.student_conn.executescript(setup_sql)
        except Exception as e:
            raise RuntimeError(f"Error in setup SQL: {e}")

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

    # ----------------- Event Handlers -----------------

    def on_submit(self, button):
        """Handle the submit button click."""
        with self.output:
            self.output.clear_output()
            question = self.get_current_question()
            student_query = self.sql_input.value.strip()

            if not student_query:
                display(HTML("<span style='color: red;'>Please enter a valid SQL query.</span>"))
                return

            # Execute the student's query on the student connection
            try:
                self.execute_student_query(student_query)
            except Exception as e:
                display(HTML(f"<h3 style='color: red;'>{e}</h3>"))
                return

            # Perform answer checking
            try:
                result, feedback = self.check_answer(
                    student_query,
                    question.get('answer', ''),
                    question.get('setup', '')
                )
            except Exception as e:
                display(HTML(f"<h3 style='color: red;'>{e}</h3>"))
                return

            # Record the answer
            self.record_answer(result)

            if result:
                self.correct_answers += 1
                display(HTML("<span style='color: green; font-weight: bold;'>Correct!</span>"))
                self.update_button_states(correct=True)
            else:
                display(HTML("<span style='color: red; font-weight: bold;'>Incorrect. Please try again.</span>"))
                if feedback:
                    display(HTML(f"<p style='color: red;'>{feedback}</p>"))
                self.update_button_states(correct=False)
                # Display schemas and data comparison
                self.display_comparison()

            # Refresh the table view after submission
            self.refresh_table_view()

            # Update progress bar
            progress_percentage = ((len(self.answered_questions)) / len(self.quiz)) * 100
            self.progress.value = progress_percentage

    def on_retry(self, button):
        """Handle the retry button click."""
        self.load_question()

    def on_next(self, button):
        """Handle the next button click."""
        self.current_question_index += 1
        if self.current_question_index < len(self.quiz):
            self.load_question()
        else:
            self.display_completion()

    def on_question_change(self, change):
        """Handle the question selector dropdown change."""
        new_index = change['new']
        self.current_question_index = new_index
        self.load_question()

    def update_button_states(self, correct):
        """Update the visibility of buttons based on correctness."""
        if correct:
            self.submit_button.layout.display = 'none'
            self.retry_button.layout.display = 'none'
            self.next_button.layout.display = 'inline-block'
        else:
            self.retry_button.layout.display = 'inline-block'

    # ----------------- Answer Checking Methods -----------------

    def execute_student_query(self, student_query):
        """Execute the student's query on the student connection."""
        try:
            self.student_conn.executescript(student_query)
        except Exception as e:
            raise RuntimeError(f"Error in your SQL query: {e}")

    def check_answer(self, student_query, correct_query, setup_query):
        """Compare the student's query against the correct answer, including schema and data."""
        # Initialize in-memory databases for checking
        student_check_conn = sqlite3.connect(':memory:')
        correct_conn = sqlite3.connect(':memory:')

        try:
            # Apply setup queries
            student_check_conn.executescript(setup_query)
            correct_conn.executescript(setup_query)

            # Execute student's query
            student_check_conn.executescript(student_query)

            # Execute correct query
            correct_conn.executescript(correct_query)
        except Exception as e:
            raise RuntimeError(f"Error during checking: {e}")

        # Compare tables and schemas
        result, feedback = self.compare_databases(student_check_conn, correct_conn)

        student_check_conn.close()
        correct_conn.close()
        return result, feedback

    def compare_databases(self, student_conn, correct_conn):
        """Compare the student and correct databases."""
        student_tables = self.get_tables(student_conn)
        correct_tables = self.get_tables(correct_conn)

        # Compare table lists
        if set(student_tables) != set(correct_tables):
            missing = set(correct_tables) - set(student_tables)
            extra = set(student_tables) - set(correct_tables)
            messages = []
            if missing:
                messages.append(f"Missing tables: {', '.join(missing)}.")
            if extra:
                messages.append(f"Unexpected tables: {', '.join(extra)}.")
            return False, f"Tables mismatch. {' '.join(messages)}"

        # Compare each table's schema and data
        all_match = True
        schema_feedback = []
        for table in student_tables:
            schema_match, schema_diff = self.compare_table_schema(student_conn, correct_conn, table)
            data_match, _, _ = self.compare_table_data(student_conn, correct_conn, table)
            if not schema_match:
                all_match = False
                schema_feedback.append(f"Schema mismatch in table '{table}': {schema_diff}")
            if not data_match:
                all_match = False
                schema_feedback.append(f"Data mismatch in table '{table}'.")

        feedback = ' '.join(schema_feedback)
        return all_match, feedback

    def get_tables(self, connection):
        """Retrieve a list of table names from the SQLite connection."""
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        return tables

    def compare_table_schema(self, student_conn, correct_conn, table_name):
        """Compare the schema of a specific table between student and correct databases."""
        student_schema = self.get_full_schema(student_conn, table_name)
        correct_schema = self.get_full_schema(correct_conn, table_name)

        if student_schema != correct_schema:
            # Identify differences
            differences = self.identify_schema_differences(student_schema, correct_schema)
            difference_str = ' '.join(differences)
            return False, difference_str

        return True, ""

    def identify_schema_differences(self, student_schema, correct_schema):
        """Identify differences between two schemas."""
        differences = []
        student_columns = {col['name']: col for col in student_schema['columns']}
        correct_columns = {col['name']: col for col in correct_schema['columns']}

        # Check for missing and extra columns
        missing_columns = set(correct_columns.keys()) - set(student_columns.keys())
        extra_columns = set(student_columns.keys()) - set(correct_columns.keys())
        if missing_columns:
            differences.append(f"Missing columns: {', '.join(missing_columns)}.")
        if extra_columns:
            differences.append(f"Unexpected columns: {', '.join(extra_columns)}.")

        # Check for column discrepancies
        for col in correct_columns:
            if col in student_columns:
                student_col = student_columns[col]
                correct_col = correct_columns[col]
                if (student_col['type'].upper() != correct_col['type'].upper() or
                    student_col['notnull'] != correct_col['notnull'] or
                    student_col['pk'] != correct_col['pk']):
                    differences.append(
                        f"Column '{col}' mismatch. Expected Type: {correct_col['type']}, "
                        f"NOT NULL: {correct_col['notnull']}, PRIMARY KEY: {correct_col['pk']}. "
                        f"Got Type: {student_col['type']}, NOT NULL: {student_col['notnull']}, "
                        f"PRIMARY KEY: {student_col['pk']}."
                    )

        # Compare foreign keys
        student_fks = student_schema.get('foreign_keys', [])
        correct_fks = correct_schema.get('foreign_keys', [])
        if len(student_fks) != len(correct_fks):
            differences.append("Mismatch in number of foreign keys.")
        else:
            for fk in correct_fks:
                if fk not in student_fks:
                    differences.append(f"Missing foreign key: {fk}.")

        return differences

    def get_full_schema(self, connection, table_name):
        """Retrieve the full schema of a table, including columns and foreign keys."""
        cursor = connection.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns_info = cursor.fetchall()
        columns = []
        for col in columns_info:
            columns.append({
                'cid': col[0],
                'name': col[1],
                'type': col[2],
                'notnull': bool(col[3]),
                'default_value': col[4],
                'pk': bool(col[5])
            })

        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        fks_info = cursor.fetchall()
        foreign_keys = []
        for fk in fks_info:
            foreign_keys.append({
                'id': fk[0],
                'seq': fk[1],
                'table': fk[2],
                'from': fk[3],
                'to': fk[4],
                'on_update': fk[5],
                'on_delete': fk[6],
                'match': fk[7]
            })

        return {
            'columns': columns,
            'foreign_keys': foreign_keys
        }

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
            raise RuntimeError(f"Error comparing table '{table_name}': {e}")

    def record_answer(self, is_correct):
        """Record whether the current question was answered correctly."""
        self.answered_questions[self.current_question_index] = is_correct

    # ----------------- Comparison Display Methods -----------------

    def display_comparison(self):
        """Display the user's and expected schema and data after an incorrect answer."""
        question = self.get_current_question()
        setup_query = question.get('setup', '')
        correct_query = question.get('answer', '')
        student_query = self.sql_input.value.strip()

        # Initialize in-memory databases for comparison
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

        # Generate comparison HTML
        comparison_html = self.generate_comparison_html(student_conn, correct_conn, question.get('expected_table'))

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

    def generate_comparison_html(self, student_conn, correct_conn, expected_table):
        """Generate HTML for the schema and data comparison."""
        # Get table schemas
        student_schema = self.get_full_schema(student_conn, expected_table)
        correct_schema = self.get_full_schema(correct_conn, expected_table)

        # Prepare HTML for schemas
        schemas_html = f"""
            <h3>Schema Comparison:</h3>
            <div class="diff-container">
                <div class="diff-table">
                    <b>Your Schema:</b><br>{self.format_schema_html(student_schema)}
                </div>
                <div class="diff-table">
                    <b>Expected Schema:</b><br>{self.format_schema_html(correct_schema)}
                </div>
            </div>
        """

        # Get tables
        student_tables = self.get_tables(student_conn)

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
        return comparison_html

    def format_schema_html(self, schema):
        """Format the schema dictionary into HTML."""
        columns = schema['columns']
        foreign_keys = schema.get('foreign_keys', [])

        html = "<ul>"
        for col in columns:
            constraints = []
            if col['notnull']:
                constraints.append("NOT NULL")
            if col['pk']:
                constraints.append("PRIMARY KEY")
            constraints_str = " ".join(constraints)
            html += f"<li>{col['name']} ({col['type']}) {constraints_str}</li>"
        html += "</ul>"

        if foreign_keys:
            html += "<b>Foreign Keys:</b><br><ul>"
            for fk in foreign_keys:
                html += f"<li>FOREIGN KEY({fk['from']}) REFERENCES {fk['table']}({fk['to']})</li>"
            html += "</ul>"

        return html

    # ----------------- Completion and Table View Methods -----------------

    def display_completion(self):
        """Display a completion message and final score."""
        # Close student connection
        if self.student_conn:
            self.student_conn.close()
            self.student_conn = None

        clear_output(wait=True)
        display(self.tabs)
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

    def refresh_table_view(self):
        """Refresh the table view tab with current table contents."""
        with self.table_output:
            self.table_output.clear_output()
            if not self.student_conn:
                display(HTML("<span style='color: red;'>No active connection to display tables.</span>"))
                return

            cursor = self.student_conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            if not tables:
                display(HTML("<span>No tables available.</span>"))
                return

            for table in tables:
                table_name = table[0]
                try:
                    df = pd.read_sql_query(f"SELECT * FROM {table_name};", self.student_conn)
                    if df.empty:
                        display(HTML(f"<h3>{table_name} (Empty)</h3>"))
                    else:
                        display(HTML(f"<h3>{table_name}</h3>"))
                        display(df)
                except Exception as e:
                    display(HTML(f"<h3 style='color: red;'>Error retrieving table '{table_name}':</h3><p>{e}</p>"))

# Example Usage:

# Instantiate and display the quiz
# Provide a URL to a JSON file containing the questions
# quiz_url = 'https://github.com/brendanpshea/database_sql/raw/main/sql_ddl_quiz/sqy_sql_ddl_quiz.json'
# sql_quiz = SQLDDLQuiz(quiz_url)
