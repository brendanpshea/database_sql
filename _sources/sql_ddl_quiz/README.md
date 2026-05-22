# SQL DDL Quiz

![License](https://img.shields.io/github/license/brendanpshea/database_sql)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Creating Custom Quizzes](#creating-custom-quizzes)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

**SQL DDL Quiz** is an interactive tool designed to help learners practice and test their knowledge of SQL Data Definition Language (DDL) and Data Manipulation Language (DML) statements. Built to be seamlessly integrated into [Google Colab](https://colab.research.google.com/), this tool provides an engaging quiz interface where users can execute SQL queries, receive instant feedback, and compare their solutions against correct answers.

## Features

- **Interactive Quiz Interface:** Presents SQL questions with a user-friendly interface for writing and submitting SQL queries.
- **Real-Time Feedback:** Executes user-submitted queries and provides immediate feedback on correctness.
- **Schema and Data Comparison:** Displays differences between the user's database state and the expected state after executing queries.
- **Progress Tracking:** Visual progress bar to monitor quiz completion.
- **View Tables Tab:** Allows users to view the current state of their in-memory SQLite database.
- **Customizable Quizzes:** Supports loading quizzes from JSON files, enabling educators to create tailored quizzes.

## Installation

Since the tool is designed to be used within Google Colab, installation is straightforward. You can download the `sql_ddl_quiz.py` script directly into your Colab environment using `wget`.

```python
# Download the SQL DDL Quiz script
!wget https://github.com/brendanpshea/database_sql/raw/main/sql_ddl_quiz/sql_ddl_quiz.py -q -nc

# Import the SQLDDLQuiz class
from sql_ddl_quiz import SQLDDLQuiz
```

## Usage

Here's a step-by-step guide to setting up and using the SQL DDL Quiz in Google Colab:

1. **Download and Import the Script:**

    ```python
    # Download the script
    !wget https://github.com/brendanpshea/database_sql/raw/main/sql_ddl_quiz/sql_ddl_quiz.py -q -nc

    # Import the SQLDDLQuiz class
    from sql_ddl_quiz import SQLDDLQuiz
    ```

2. **Specify the Quiz JSON File:**

    The quiz questions are defined in a JSON file. You can use one of the existing quizzes or create your own.

    ```python
    # URL to the quiz JSON file
    quiz_url = 'https://github.com/brendanpshea/database_sql/raw/main/sql_ddl_quiz/cartoon_quiz.json'
    ```

3. **Instantiate and Launch the Quiz:**

    ```python
    # Create an instance of SQLDDLQuiz
    sql_quiz = SQLDDLQuiz(quiz_url)
    ```

    Upon running the above cell, an interactive quiz interface will appear, allowing you to start answering SQL questions.

## Creating Custom Quizzes

You can create your own quizzes by defining a JSON file with the required structure. Here's a basic outline of how to structure your quiz JSON:

```json
[
    {
        "question": "Create a table named 'students' with columns 'id' (integer primary key) and 'name' (text).",
        "setup": "",
        "answer": "CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT);",
        "expected_table": "students"
    },
    {
        "question": "Insert a student with id 1 and name 'Alice' into the 'students' table.",
        "setup": "CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT);",
        "answer": "INSERT INTO students (id, name) VALUES (1, 'Alice');",
        "expected_table": "students"
    }
    // Add more questions as needed
]
```

- **question:** The prompt displayed to the user.
- **setup:** SQL statements to set up the initial database state for the question.
- **answer:** The correct SQL statement expected from the user.
- **expected_table:** The table to focus on when displaying schema and data comparisons.

### Uploading Your Quiz

1. **Create Your JSON File:** Define your quiz questions as shown above.
2. **Upload to GitHub:** Push your JSON file to a GitHub repository or any accessible URL.
3. **Use the URL in Colab:**

    ```python
    quiz_url = 'https://github.com/yourusername/yourrepo/raw/main/your_quiz.json'
    sql_quiz = SQLDDLQuiz(quiz_url)
    ```

## Dependencies

The SQL DDL Quiz relies on several Python libraries. While Google Colab comes pre-installed with most of these, ensure that the following packages are available:

- `sqlite3`
- `requests`
- `IPython`
- `pandas`
- `ipywidgets`

If you're running the tool outside of Google Colab, you may need to install these dependencies:

```bash
pip install requests pandas ipywidgets
```

## Contributing

Contributions are welcome! If you'd like to contribute to the SQL DDL Quiz, please follow these steps:

1. **Fork the Repository:** Click the "Fork" button at the top-right of the repository page.
2. **Create a Branch:** Create a new branch for your feature or bugfix.
3. **Make Changes:** Implement your changes and ensure the code follows best practices.
4. **Submit a Pull Request:** Open a pull request describing your changes.

For major changes, please open an issue first to discuss your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Happy quizzing! 🚀*
