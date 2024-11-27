# SQL SELECT Quiz

![License](https://img.shields.io/github/license/brendanpshea/database_sql)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Creating Custom Quizzes](#creating-custom-quizzes)
- [Available Quizzes](#available-quizzes)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

**SQL SELECT Quiz** is an interactive tool designed to help learners practice and test their knowledge of SQL `SELECT` statements. Built to be seamlessly integrated into [Google Colab](https://colab.research.google.com/), this tool provides an engaging quiz interface where users can execute SQL queries against predefined SQLite databases, receive instant feedback, and compare their results with expected outcomes.

## Features

- **Interactive Quiz Interface:** Presents SQL `SELECT` questions with a user-friendly interface for writing and submitting SQL queries.
- **Real-Time Feedback:** Executes user-submitted queries and provides immediate feedback on correctness.
- **Schema Display:** Shows the current database schema to aid in crafting accurate queries.
- **Result Comparison:** Compares the user's query results with the expected results, highlighting discrepancies.
- **Progress Tracking:** Visual progress bar to monitor quiz completion.
- **Multiple Quizzes:** Supports various datasets (e.g., books, movies, Mario, music, firewall logs) to provide diverse querying scenarios.
- **Customizable Quizzes:** Allows educators to create tailored quizzes by loading custom JSON files.

## Installation

Since the tool is designed to be used within Google Colab, installation is straightforward. You can download the `sql_select_quiz.py` script directly into your Colab environment using `wget`.

```python
# Download the SQL SELECT Quiz script
!wget https://github.com/brendanpshea/database_sql/raw/main/sql_select_quiz/sql_select_quiz.py -q -nc

# Import all necessary classes and functions
from sql_select_quiz import *
```

## Usage

Here's a step-by-step guide to setting up and using the SQL SELECT Quiz in Google Colab:

1. **Download and Import the Script:**

    ```python
    # Download the script
    !wget https://github.com/brendanpshea/database_sql/raw/main/sql_select_quiz/sql_select_quiz.py -q -nc

    # Import all necessary classes and functions
    from sql_select_quiz import *
    ```

2. **Choose a Quiz by ID:**

    The tool comes with several predefined quizzes. You can choose one by specifying its ID.

    ```python
    # Start the 'firewall' quiz
    sql_select_quiz_from_id("firewall")
    ```

    Available quiz IDs:
    - `"books"`: Sci-Fi Books Database
    - `"movies"`: Movies Database
    - `"mario"`: Mario Bros Plumbing Database
    - `"music"`: Greatest Albums Database
    - `"firewall"`: Firewall Logs Database

3. **Using a Custom Quiz JSON:**

    If you have a custom JSON file defining your own quiz questions, you can use it as follows:

    ```python
    # Replace with your custom quiz JSON URL
    custom_quiz_url = 'https://github.com/yourusername/yourrepo/raw/main/your_custom_quiz.json'
    
    sql_select_quiz_url('https://github.com/yourusername/yourrepo/raw/main/data/your_database.db', custom_quiz_url)
    ```

    Ensure that your custom JSON follows the required structure (see [Creating Custom Quizzes](#creating-custom-quizzes)).

4. **Interactive Quiz Interface:**

    Once the quiz starts, you'll see an interface with the following components:
    - **Progress Bar:** Shows your current progress through the quiz.
    - **Question Display:** Presents the current SQL `SELECT` question and the relevant database schema.
    - **Query Input Area:** Where you can type your SQL `SELECT` statement.
    - **Buttons:**
        - **Submit:** Execute your query and receive feedback.
        - **Clear:** Clear the query input area.
        - **Hint:** Receive a hint for the current question.
        - **Skip to:** Jump to a specific question number.
    - **Results Tab:** Displays your query results compared to the expected results, along with feedback.

## Creating Custom Quizzes

You can create your own quizzes by defining a JSON file with the required structure. Here's a basic outline of how to structure your quiz JSON:

```json
[
    {
        "question": "Retrieve all records from the 'students' table.",
        "setup": "CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER); INSERT INTO students (name, age) VALUES ('Alice', 23), ('Bob', 30);",
        "answer": "SELECT * FROM students;",
        "expected_table": "students"
    },
    {
        "question": "Find the names of students older than 25.",
        "setup": "CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER); INSERT INTO students (name, age) VALUES ('Alice', 23), ('Bob', 30);",
        "answer": "SELECT name FROM students WHERE age > 25;",
        "expected_table": "students"
    }
    // Add more questions as needed
]
```

- **question:** The prompt displayed to the user.
- **setup:** SQL statements to set up the initial database state for the question.
- **answer:** The correct SQL `SELECT` statement expected from the user.
- **expected_table:** The table to focus on when displaying schema and data comparisons.

### Uploading Your Quiz

1. **Create Your JSON File:** Define your quiz questions as shown above.
2. **Upload to GitHub:** Push your JSON file and corresponding SQLite database to a GitHub repository or any accessible URL.
3. **Use the URL in Colab:**

    ```python
    custom_db_url = 'https://github.com/yourusername/yourrepo/raw/main/data/your_database.db'
    custom_quiz_url = 'https://github.com/yourusername/yourrepo/raw/main/your_custom_quiz.json'
    
    sql_select_quiz_url(custom_db_url, custom_quiz_url)
    ```

## Available Quizzes

The SQL SELECT Quiz tool offers several predefined quizzes, each associated with a specific SQLite database:

1. **Books Quiz (`"books"`):**
    - **Database:** Sci-Fi Books
    - **Quiz JSON:** [sql_book_quiz.json](https://github.com/brendanpshea/database_sql/raw/main/quiz/sql_book_quiz.json)

2. **Movies Quiz (`"movies"`):**
    - **Database:** Movies
    - **Quiz JSON:** [sql_movie_quiz.json](https://github.com/brendanpshea/database_sql/raw/main/quiz/sql_movie_quiz.json)

3. **Mario Quiz (`"mario"`):**
    - **Database:** Mario Bros Plumbing
    - **Quiz JSON:** [sql_mario_quiz.json](https://github.com/brendanpshea/database_sql/raw/main/quiz/sql_mario_quiz.json)

4. **Music Quiz (`"music"`):**
    - **Database:** Greatest Albums
    - **Quiz JSON:** [sql_music_quiz.json](https://github.com/brendanpshea/database_sql/raw/main/quiz/sql_music_quiz.json)

5. **Firewall Quiz (`"firewall"`):**
    - **Database:** Firewall Logs
    - **Quiz JSON:** [sql_toad_city_fw.json](https://github.com/brendanpshea/database_sql/raw/main/quiz/sql_toad_city_fw.json)

To start any of these quizzes, use the corresponding quiz ID as shown in the [Usage](#usage) section.

## Dependencies

The SQL SELECT Quiz relies on several Python libraries. While Google Colab comes pre-installed with most of these, ensure that the following packages are available:

- `sqlite3`
- `pandas`
- `requests`
- `ipywidgets`
- `IPython`

If you're running the tool outside of Google Colab, you may need to install these dependencies:

```bash
pip install pandas requests ipywidgets
```

**Note:** To enable `ipywidgets` in Jupyter notebooks, you might need to run:

```bash
jupyter nbextension enable --py widgetsnbextension
```

## Contributing

Contributions are welcome! If you'd like to contribute to the SQL SELECT Quiz, please follow these steps:

1. **Fork the Repository:** Click the "Fork" button at the top-right of the repository page.
2. **Create a Branch:** Create a new branch for your feature or bugfix.
3. **Make Changes:** Implement your changes and ensure the code follows best practices.
4. **Submit a Pull Request:** Open a pull request describing your changes.

For major changes, please open an issue first to discuss your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Happy querying! 🚀*
