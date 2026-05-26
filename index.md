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

### For Students
Each chapter is structured as a self-contained, story-driven learning experience set in familiar pop-culture universes (like exploring database models through *Star Trek*, tracking inventory for *Mario Bros Plumbing*, or managing security at *Gotham City Bank*). You can read each chapter in your browser or launch it directly in **Google Colab** with a single click. There are no complex software installations, version mismatches, or setup hurdles—you can start writing and running SQL immediately.

### For Instructors
This curriculum is closely aligned with the **CompTIA DataSys+ (DS0-002)** certification exam, covering core database foundations, design, deployment, security, and integration. It provides a complete, zero-setup, active-learning framework featuring built-in, autograded quizzes and game-based review sets. As an **Open Educational Resource (OER)**, it is freely shareable, adaptable, and optimized for digital publishing.

<div class="home-hero__support" style="margin-top: 1.5rem; padding: 1.2rem; border-left: 4px solid var(--db-accent); background-color: var(--db-paper); border-radius: 0 12px 12px 0; font-size: 0.95rem; line-height: 1.6; color: var(--db-ink-soft);">
  Development of this textbook was made possible by generous grant funding from the <strong>Minnesota State (MinnState)</strong> system and <strong>Rochester Community and Technical College (RCTC)</strong>, as part of their ongoing commitment to high-quality, zero-cost learning resources for students.
</div>

---

## Textbook Table of Contents

Each chapter is Google Colab-ready. Launch a notebook to execute code dynamically, or read the web version for clean offline study.

| Chapter | Title & Theme | Core Learning Concepts | Interactive Formats |
| :--- | :--- | :--- | :--- |
| **Ch 00** | [Introduction](Database_00_Introduction.html) | Book pedagogy, author, DataSys+ alignment | [Read Online](Database_00_Introduction.html) |
| **Ch 01** | [Starship SQL (Star Trek)](Database_01_StarShipSQL.html) | Data models (Relational, JSON, Graph), databases vs. flat files | [Read Online](Database_01_StarShipSQL.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_01_StarShipSQL.ipynb) |
| **Ch 02** | [Intro to SQL SELECT](Database_02_IntroToSQL.html) | Basic queries, SELECT, FROM, WHERE, ORDER BY, DISTINCT | [Read Online](Database_02_IntroToSQL.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_02_IntroToSQL.ipynb) |
| **Ch 03** | [JOINs and Sets](Database_03_Joins_Sets_SQL.html) | INNER/OUTER JOINs, UNIONS, EXCEPT, INTERSECT | [Read Online](Database_03_Joins_Sets_SQL.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_03_Joins_Sets_SQL.ipynb) |
| **Ch 04** | [Advanced SELECT](Database_04_AdvancedSelect.html) | GROUP BY, HAVING, subqueries, complex filtering | [Read Online](Database_04_AdvancedSelect.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_04_AdvancedSelect.ipynb) |
| **Ch 05** | [Database Design](Database_05_Design.html) | ERDs, normalization, primary & foreign keys, constraint rules | [Read Online](Database_05_Design.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_05_Design.ipynb) |
| **Ch 06** | [Writing Data (Mario Plumbing)](Database_06_WritingData.html) | INSERT, UPDATE, DELETE, triggers, application connections | [Read Online](Database_06_WritingData.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_06_WritingData.ipynb) |
| **Ch 07** | [Views and CTEs](Database_07_Views.html) | Reusable query blocks, reporting structures, access controls | [Read Online](Database_07_Views.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_07_Views.ipynb) |
| **Ch 08** | [Indexes and Transactions](Database_08_IndexesTransactions.html) | Indexing types, execution plans, ACID transactions | [Read Online](Database_08_IndexesTransactions.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_08_IndexesTransactions.ipynb) |
| **Ch 09** | [Pokémon and PostgreSQL](Database_09_PokemonAndPostgres.html) | SQLite-to-PostgreSQL, schemas, advanced types, procedural code | [Read Online](Database_09_PokemonAndPostgres.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_09_PokemonAndPostgres.ipynb) |
| **Ch 10** | [Database Security (Gotham Bank)](Database_10_DatabaseSecurity.html) | CIA Triad, access control (RBAC), SQL injection, encryption | [Read Online](Database_10_DatabaseSecurity.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_10_DatabaseSecurity.ipynb) |
| **Ch 11** | [Design, Deploy, Test](Database_11_DesignDeployTest.html) | Systems lifecycle, physical architecture, verification | [Read Online](Database_11_DesignDeployTest.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_11_DesignDeployTest.ipynb) |
| **Ch 12** | [Data Integration (Emerald Clinic)](Database_12_DataIntegration.html) | CSV, JSON, XML, APIs, ETL pipelines, AI tools | [Read Online](Database_12_DataIntegration.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_12_DataIntegration.ipynb) |
| **Ch 13** | [Final Capstone Project](Database_13_FinalProject.html) | End-to-end database design, build, optimization, and docs | [Read Online](Database_13_FinalProject.html) \| [Launch Colab](https://colab.research.google.com/github/brendanpshea/database_sql/blob/main/Database_13_FinalProject.ipynb) |

---

## Integrated Case Studies

To bring abstract concepts to life, instruction is anchored in story-driven case studies inspired by pop culture:

* 🛰️ **Starship SQL (Chapter 1)**: Explore database data models (Relational, JSON, Graph) on board the USS Enterprise.
* 🍄 **Mario Bros Plumbing (Chapter 6 & 8)**: Build a service database, handle concurrent repair orders, and manage ACID transactions.
* 🦇 **Gotham City Bank (Chapter 10)**: Secure vault keys and assign role-based access to protect against bank robberies.
* 💎 **Emerald City Clinic (Chapter 12)**: Ingest patient records across CSV, JSON, and APIs to design an advanced medical ETL pipeline.

---

## Learning & Practice Resources

Each chapter is supported by comprehensive self-check quizzes and gamified review sets to reinforce core skills:

### Chapter Review Games (Loop of the Recursive Dragon)
Test your knowledge with RPG-style adaptive review sets set in the *Loop of the Recursive Dragon* review game. Select a chapter and play:

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

### Autograded Practical Quizzes
To test your hands-on query writing skills, launch these auto-graded CLI/Python practice tests in your terminal:
* 📝 **[SQL SELECT Quiz](https://github.com/brendanpshea/database_sql/tree/main/sql_select_quiz)**: Focused practice for retrieving, filtering, sorting, and combining data.
* 📝 **[SQL DDL Quiz](https://github.com/brendanpshea/database_sql/tree/main/sql_ddl_quiz)**: Focused practice for building, altering, and managing relational schemas.

---

## Coming Soon

Scenario-based case studies on stewardship, policy, compliance, quality controls, governance risk, and data lifecycle management.
