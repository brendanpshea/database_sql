# SQL and Database Management Through Pop Culture

Welcome to this interactive, openly licensed textbook for database design, SQL querying, security, performance, and PostgreSQL. Designed as a modern, hands-on introduction to data management, this book is built from the ground up for both active student engagement and seamless classroom adoption.

<div class="home-stats" style="display: grid; grid-template-columns: repeat(4, 1fr); margin: 2rem 0; gap: 1rem;">
	<div class="home-stat" style="text-align: center; padding: 0.95rem; border-radius: 18px; background: var(--db-paper);">
		<strong style="display: block; margin-bottom: 0.2rem; color: var(--db-accent-strong); font-size: 1.6rem; font-weight: 700;">12+</strong> Chapters
	</div>
	<div class="home-stat" style="text-align: center; padding: 0.95rem; border-radius: 18px; background: var(--db-paper);">
		<strong style="display: block; margin-bottom: 0.2rem; color: var(--db-accent-strong); font-size: 1.6rem; font-weight: 700;">Zero-Setup</strong> Web + Colab
	</div>
	<div class="home-stat" style="text-align: center; padding: 0.95rem; border-radius: 18px; background: var(--db-paper);">
		<strong style="display: block; margin-bottom: 0.2rem; color: var(--db-accent-strong); font-size: 1.6rem; font-weight: 700;">CC BY-NC 4.0</strong> Open License
	</div>
	<div class="home-stat" style="text-align: center; padding: 0.95rem; border-radius: 18px; background: var(--db-paper);">
		<strong style="display: block; margin-bottom: 0.2rem; color: var(--db-accent-strong); font-size: 1.6rem; font-weight: 700;">DataSys+</strong> Aligned
	</div>
</div>

---

## For Students
Each chapter is structured as a self-contained, story-driven learning experience set in familiar pop-culture universes (including *Star Trek*, *Mario Bros*, *Gotham City*, *Pokémon*, and *Emerald City Clinic*). You can read each chapter in your browser or launch it directly in **Google Colab** with a single click. 

There are no complex software installations, version mismatches, or setup hurdles—you can start writing and running SQL immediately. Interactive, **auto-graded quizzes are built directly into the notebooks**, giving you instant feedback on your SQL query writing and schema design skills as you read and practice.

## For Instructors
This curriculum is closely aligned with the **CompTIA DataSys+ (DS0-002)** certification exam, covering core database foundations, design, deployment, security, and integration. It provides a complete, zero-setup, active-learning framework featuring built-in, autograded quizzes and game-based review sets. Every single chapter features a unique pop-culture case study that helps make abstract database and SQL concepts approachable and memorable. As an **Open Educational Resource (OER)**, it is freely shareable, adaptable, and optimized for digital publishing.

<div class="home-hero__support" style="margin-top: 1.5rem; padding: 1.2rem; border-left: 4px solid var(--db-accent); background-color: var(--db-paper); border-radius: 0 12px 12px 0; font-size: 0.95rem; line-height: 1.6; color: var(--db-ink-soft);">
  Development of this textbook was made possible by generous grant funding from the <strong>Minnesota State (MinnState)</strong> system and <strong>Rochester Community and Technical College (RCTC)</strong>, as part of their ongoing commitment to high-quality, zero-cost learning resources for students.
</div>

---

## Textbook Table of Contents

Each chapter is Google Colab-ready. Launch a notebook to execute code dynamically, or read the web version for clean offline study.

| Chapter | Title & Theme | Core Learning Concepts | Interactive Formats |
| :--- | :--- | :--- | :--- |
| **Ch 00** | [Chapter 0: Introduction to Databases and SQL (Pop Culture Overview)](database_ch00_introduction.ipynb) | Book pedagogy, author, DataSys+ alignment | [Read Online](database_ch00_introduction.ipynb) |
| **Ch 01** | [Chapter 1: Database Foundations (Star Trek and Starfleet Command)](database_ch01_foundations_starfleet.ipynb) | Data models (Relational, JSON, Graph), databases vs. flat files | [Read Online](database_ch01_foundations_starfleet.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch01_foundations_starfleet.ipynb) |
| **Ch 02** | [Chapter 2: Basic Retrieval with SELECT (The Sci-Fi Classics Catalog)](database_ch02_select_scifi.ipynb) | Basic queries, SELECT, FROM, WHERE, ORDER BY, DISTINCT | [Read Online](database_ch02_select_scifi.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch02_select_scifi.ipynb) |
| **Ch 03** | [Chapter 3: Joins and Set Operations (The IMDb Cinema Database)](database_ch03_joins_imdb.ipynb) | INNER/OUTER JOINs, UNIONS, EXCEPT, INTERSECT | [Read Online](database_ch03_joins_imdb.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch03_joins_imdb.ipynb) |
| **Ch 04** | [Chapter 4: Advanced SQL & Business Continuity (Mario Brothers Plumbing)](database_ch04_advanced_mario.ipynb) | GROUP BY, HAVING, subqueries, complex filtering | [Read Online](database_ch04_advanced_mario.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch04_advanced_mario.ipynb) |
| **Ch 05** | [Chapter 5: Relational Schema Design (The Covert Spy Academy)](database_ch05_design_spy.ipynb) | ERDs, normalization, primary & foreign keys, constraint rules | [Read Online](database_ch05_design_spy.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch05_design_spy.ipynb) |
| **Ch 06** | [Chapter 6: Data Modification with DML (Rolling Stone's Greatest Albums)](database_ch06_dml_rollingstone.ipynb) | INSERT, UPDATE, DELETE, triggers, application connections | [Read Online](database_ch06_dml_rollingstone.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch06_dml_rollingstone.ipynb) |
| **Ch 07** | [Chapter 7: Schema Abstraction with Views (The Pop Culture Music Archive)](database_ch07_views_music.ipynb) | Reusable query blocks, reporting structures, access controls | [Read Online](database_ch07_views_music.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch07_views_music.ipynb) |
| **Ch 08** | [Chapter 8: Indexes, Performance & Transactions (Gotham National Bank)](database_ch08_indexes_gotham.ipynb) | Indexing types, execution plans, ACID transactions | [Read Online](database_ch08_indexes_gotham.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch08_indexes_gotham.ipynb) |
| **Ch 09** | [Chapter 9: Enterprise Databases with PostgreSQL (The Pokémon Pokédex)](database_ch09_postgres_pokemon.ipynb) | SQLite-to-PostgreSQL, schemas, advanced types, procedural code | [Read Online](database_ch09_postgres_pokemon.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch09_postgres_pokemon.ipynb) |
| **Ch 10** | [Chapter 10: Database Security & Defense (Toad Town Medical Center)](database_ch10_security_toad.ipynb) | CIA Triad, access control (RBAC), SQL injection, encryption | [Read Online](database_ch10_security_toad.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch10_security_toad.ipynb) |
| **Ch 11** | [Chapter 11: Architecture Patterns & Testing (The Springfield Power Plant)](database_ch11_architecture_springfield.ipynb) | Systems lifecycle, physical architecture, verification | [Read Online](database_ch11_architecture_springfield.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch11_architecture_springfield.ipynb) |
| **Ch 12** | [Chapter 12: Data Integration and ETL Pipelines (The Emerald City Clinic)](database_ch12_integration_emerald.ipynb) | CSV, JSON, XML, APIs, ETL pipelines, AI tools | [Read Online](database_ch12_integration_emerald.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch12_integration_emerald.ipynb) |
| **Ch 13** | [Chapter 13: Relational Design Capstone (Your Pop Culture Sandbox)](database_ch13_final_project.ipynb) | End-to-end database design, build, optimization, and docs | [Read Online](database_ch13_final_project.ipynb) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/database_ch13_final_project.ipynb) |

---

## Chapter Review Games (Loop of the Recursive Dragon)

Each chapter is supported by an RPG-style adaptive review set in the *Loop of the Recursive Dragon* review game. Select a chapter and play:

* ⚔️ [Ch 1 — Foundations](https://brendanpshea.github.io/LotRD/?set=database_01_foundations.json) (Data, models, structures)
* ⚔️ [Ch 2 — SELECT basics](https://brendanpshea.github.io/LotRD/?set=database_02_select.json) (Filtering, sorting, aggregates)
* ⚔️ [Ch 3 — JOINs and sets](https://brendanpshea.github.io/LotRD/?set=database_03_joins_sets.json) (Inner, outer, unions)
* ⚔️ [Ch 4 — Advanced retrieval](https://brendanpshea.github.io/LotRD/?set=database_04_advanced_retrieval.json) (GROUP BY, HAVING, subqueries)
* ⚔️ [Ch 5 — Database design](https://brendanpshea.github.io/LotRD/?set=database_05_design.json) (ER modeling, normalization, keys)
* ⚔️ [Ch 6 — Writing data](https://brendanpshea.github.io/LotRD/?set=database_06_writing_data.json) (INSERT, UPDATE, DELETE, triggers)
* ⚔️ [Ch 7 — Views & governance](https://brendanpshea.github.io/LotRD/?set=database_07_views_ctes_governance.json) (CTEs, data governance, GDPR)
* ⚔️ [Ch 8 — Performance & ACID](https://brendanpshea.github.io/LotRD/?set=database_08_performance_transactions.json) (Indexes, plans, transactions)
* ⚔️ [Ch 9 — PostgreSQL](https://brendanpshea.github.io/LotRD/?set=database_09_postgres.json) (Postgres types, procedures, roles)
* ⚔️ [Ch 10 — Database security](https://brendanpshea.github.io/LotRD/?set=database_10_security.json) (CIA triad, roles, SQL injection, encryption)
* ⚔️ [Ch 11 — Architecture & testing](https://brendanpshea.github.io/LotRD/?set=database_11_architecture_testing.json) (Design patterns, deployment models)
* ⚔️ [Ch 12 — Data integration](https://brendanpshea.github.io/LotRD/?set=database_12_data_integration.json) (ETL, formats, AI tooling)
* ⚔️ [Ch 13 — Capstone review](https://brendanpshea.github.io/LotRD/?set=database_13_final_project.json) (Comprehensive final project prep)

---

## Coming Soon

Scenario-based case studies on stewardship, policy, compliance, quality controls, governance risk, and data lifecycle management.
