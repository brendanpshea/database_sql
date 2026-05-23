# SQL and Database Management Through Pop Culture

An open educational resource built as a public Jupyter Book and a set of notebook-first lessons for teaching database design, SQL, PostgreSQL, security, performance, and deployment through pop-culture case studies.

The main public entry point for this project is the GitHub Pages site:

- [Read the live book](https://brendanpshea.github.io/database_sql/)
- [Open Chapter 1 in Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_01_StarShipSQL.ipynb)
- [Browse the repository](https://github.com/brendanpshea/database_sql)

## What this project includes

- A published Jupyter Book designed for web reading and classroom adoption
- 12 core notebook chapters covering the full course sequence
- Guided labs and interactive quiz tools for additional practice
- Google Colab-ready notebooks so students can run the material without local setup
- Public OER course materials supported by Minnesota State and Rochester Community and Technical College

## Why it is structured this way

This project is designed so students and instructors can use the same content in two ways:

- **Read on the web:** the GitHub Pages book works as the main textbook and public-facing course site
- **Run in Colab:** each notebook can be launched directly for hands-on experimentation

That combination keeps the material easy to adopt in class while still preserving a fully editable notebook workflow for teaching, remixing, and maintenance.

## Course coverage

The book moves from foundations to applied database work:

- Data modeling and database types
- Core SQL querying with `SELECT`, filtering, sorting, joins, and set operations
- Advanced querying with aggregation, subqueries, JSON, and views
- Schema design and writing data
- Indexes, transactions, and performance analysis
- PostgreSQL features including procedures, window functions, and richer data types
- Database security, deployment, testing, and a final project

## Project layout

- `Database_01_*.ipynb` through `Database_12_*.ipynb`: main course chapters
- `labs/`: guided lab notebooks
- `quiz/`, `sql_select_quiz/`, `sql_ddl_quiz/`: quiz data and interactive practice tools
- `_static/`: CSS, JavaScript, and browser-based interactive assets used by the published book
- `data/`: source datasets and notebook generators used by the course materials
- `_config.yml` and `_toc.yml`: Jupyter Book configuration and navigation

## Local development

This repository uses the classic Jupyter Book layout.

Build the site locally from the repository root with:

```bash
jupyter-book build .
```

The published site is intended to be the canonical public experience, while the notebooks remain the source format for editing and Colab delivery.

## Practice tools

Two quiz systems are included for structured SQL practice:

- [SQL SELECT Quiz](https://github.com/brendanpshea/database_sql/tree/main/sql_select_quiz)
- [SQL DDL Quiz](https://github.com/brendanpshea/database_sql/tree/main/sql_ddl_quiz)

## Contributing

Contributions that improve the book, notebooks, quizzes, or supporting assets are welcome. Open an issue or submit a pull request if you want to propose a change.

## License

This project is distributed under the GNU Public License.

## Use of AI Tools

This project has been developed with the help of generative AI tools across multiple model generations, alongside direct author editing and instructional design work.

## About the Author

Brendan Shea, PhD, is Professor of Philosophy and Computer Science at Rochester Community and Technical College and a Resident Fellow at the Minnesota Center for Philosophy of Science at the University of Minnesota-Twin Cities. His research and teaching focus on philosophy of science, data modeling, applied ethics, and related interdisciplinary topics. More information is available on [PhilPeople](https://philpeople.org/profiles/brendan-shea).
