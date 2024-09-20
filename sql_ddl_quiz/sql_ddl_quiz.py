# sql_ddl_quiz.py
import sqlite3
import re
import pandas as pd
import requests
import json
from IPython.display import display, clear_output
from ipywidgets import (
    Textarea, Button, VBox, HBox, Layout, IntProgress,
    HTML as HTMLWidget, Label, Output, Tab, Dropdown
)

class SQLPractice:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0
        self.create_connection()
        self.setup_ui()
        self.display_current_step()

    def create_connection(self):
        self.conn = sqlite3.connect(':memory:')  # In-memory database
        self.conn.isolation_level = None  # Enable manual transaction control

    def get_existing_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        return [table[0] for table in tables if table[0] != 'sqlite_sequence']  # Exclude SQLite internal tables

    def get_table_schema(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        # Build a concise schema representation
        schema_parts = []
        for col in columns:
            col_def = f"{col[1]} {col[2]}"
            if col[5]:
                col_def += " PRIMARY KEY"
            elif col[3]:
                col_def += " NOT NULL"
            schema_parts.append(col_def)
        schema = f"<b>{table_name}</b> ({', '.join(schema_parts)})"
        return schema

    def setup_ui(self):
        self.progress_bar = IntProgress(
            min=0, max=len(self.steps), value=1, description='Progress:')
        self.step_label = HTMLWidget(value='')

        self.tables_info = HTMLWidget(value='')  # To display existing tables and schemas

        self.text_area = Textarea(
            placeholder='Type your SQL statements here...',
            layout=Layout(width='100%', height='150px')
        )
        self.execute_button = Button(description="Execute", button_style='success')
        self.clear_button = Button(description="Clear", button_style='warning')
        self.hint_button = Button(description="Hint", button_style='info')
        self.reset_button = Button(description="Reset Database", button_style='danger')
        self.next_button = Button(description="Next Step", button_style='info', disabled=True)

        self.execute_button.on_click(self.execute_statements)
        self.clear_button.on_click(self.clear_text)
        self.hint_button.on_click(self.show_hint)
        self.reset_button.on_click(self.reset_practice)
        self.next_button.on_click(self.next_step)

        self.output_area = Output()

        # Create the main tab widget
        self.tab_widget = Tab()

        # First tab: SQL Input and Output
        self.sql_tab = VBox([
            self.text_area,
            HBox([self.execute_button, self.clear_button, self.hint_button, self.next_button, self.reset_button]),
            self.output_area
        ])

        # Second tab: View Tables
        self.table_dropdown = Dropdown(options=[], description='Select Table:')
        self.table_view_output = Output()
        self.table_dropdown.observe(self.display_table_content, names='value')

        self.view_tables_tab = VBox([self.table_dropdown, self.table_view_output])

        self.tab_widget.children = [self.sql_tab, self.view_tables_tab]
        self.tab_widget.set_title(0, 'SQL Editor')
        self.tab_widget.set_title(1, 'View Tables')

        # Main UI layout
        self.ui = VBox([
            self.progress_bar,
            self.step_label,
            self.tables_info,
            self.tab_widget
        ])

    def display_current_step(self):
        clear_output(wait=True)
        self.output_area.clear_output()
        self.table_view_output.clear_output()
        step_info = self.steps[self.current_step]
        self.step_label.value = f"<h3>Step {self.current_step + 1} of {len(self.steps)}</h3><p>{step_info['instruction']}</p>"
        self.progress_bar.value = self.current_step + 1

        # Display existing tables and their schemas
        existing_tables = self.get_existing_tables()
        if existing_tables:
            schemas = [self.get_table_schema(table) for table in existing_tables]
            tables_html = "<h4>Existing Tables and Schemas:</h4><ul>"
            for schema in schemas:
                tables_html += f"<li>{schema}</li>"
            tables_html += "</ul>"
        else:
            tables_html = "<p><em>No tables exist yet.</em></p>"
        self.tables_info.value = tables_html

        # Update the table dropdown in the "View Tables" tab
        self.table_dropdown.options = existing_tables
        if existing_tables:
            self.table_dropdown.value = existing_tables[0]
            # Manually call display_table_content to display the table content
            self.display_table_content({'new': self.table_dropdown.value})
        else:
            self.table_dropdown.value = None
            self.table_view_output.clear_output()

        display(self.ui)

    def execute_statements(self, _):
        user_sql = self.text_area.value.strip()
        if not user_sql:
            with self.output_area:
                clear_output()
                print("Please enter your SQL statements.")
            return
    
        try:
            cursor = self.conn.cursor()
            cursor.execute("BEGIN TRANSACTION;")  # Start a transaction
    
            # Preprocess user's SQL to handle CREATE TABLE statements
            user_sql = self.preprocess_sql(user_sql)
    
            cursor.executescript(user_sql)
    
            # Now check the result
            expected_check = self.steps[self.current_step]['check']
            cursor.execute(expected_check['query'])
            user_result = cursor.fetchall()
            expected_result = expected_check['expected']
    
            # Convert expected_result lists to tuples
            expected_result = [tuple(item) for item in expected_result]
    
            # Compare results
            if user_result == expected_result:
                self.conn.commit()  # Commit the transaction
                feedback = HTMLWidget(value="<h4 style='color: green;'>Correct! Changes have been committed. You may proceed to the next step.</h4>")
                self.next_button.disabled = False
                self.execute_button.disabled = True
            else:
                self.conn.rollback()  # Rollback the transaction
                feedback = HTMLWidget(value="<h4 style='color: red;'>Incorrect. Your changes have been rolled back. Please try again.</h4>")
                self.next_button.disabled = True
                self.execute_button.disabled = False
    
            # Update existing tables info
            # ... (rest of the code remains the same)
    
        except Exception as e:
            self.conn.rollback()  # Rollback the transaction on error
            with self.output_area:
                clear_output()
                print(f"Error executing your SQL statements: {e}")
    
    def preprocess_sql(self, sql):
        # Regular expression to find CREATE TABLE statements
        pattern = re.compile(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)', re.IGNORECASE)
        statements = sql.split(';')  # Split statements by semicolon
        preprocessed_statements = []

        for stmt in statements:
            stmt = stmt.strip()
            if not stmt:
                continue
            match = pattern.match(stmt)
            if match:
                table_name = match.group(1)
                drop_stmt = f"DROP TABLE IF EXISTS {table_name};"
                preprocessed_statements.append(drop_stmt)
            preprocessed_statements.append(stmt + ';')

        return '\n'.join(preprocessed_statements)

    def clear_text(self, _):
        self.text_area.value = ''

    def show_hint(self, _):
        hint = self.steps[self.current_step].get('hint', 'No hint available for this step.')
        with self.output_area:
            clear_output()
            display(HTMLWidget(value=f"<strong>Hint:</strong> {hint}"))

    def reset_practice(self, _):
        self.current_step = 0
        self.create_connection()  # Recreate the in-memory database
        self.execute_button.disabled = False
        self.next_button.disabled = True
        self.text_area.value = ''
        self.display_current_step()
        with self.output_area:
            clear_output()
            print("Practice has been reset. You are back at step one.")

    def next_step(self, _):
        self.current_step += 1
        if self.current_step < len(self.steps):
            self.execute_button.disabled = False
            self.next_button.disabled = True
            self.text_area.value = ''
            self.display_current_step()
        else:
            clear_output(wait=True)
            print("Congratulations! You have completed all the steps.")

    def display_table_content(self, change):
        selected_table = change['new']
        self.table_view_output.clear_output()
        if selected_table:
            with self.table_view_output:
                try:
                    df = pd.read_sql_query(f"SELECT * FROM {selected_table};", self.conn)
                    if df.empty:
                        print(f"The table '{selected_table}' is empty.")
                    else:
                        display(df)
                except Exception as e:
                    print(f"Error retrieving data from '{selected_table}': {e}")

def run_sql_ddl_quiz(steps_url):
    response = requests.get(steps_url)
    if response.status_code != 200:
        print(f"Failed to retrieve steps from URL: {steps_url}")
        return
    steps = json.loads(response.text)
    sql_practice = SQLPractice(steps)
