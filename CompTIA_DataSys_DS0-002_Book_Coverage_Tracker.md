# CompTIA DataSys+ DS0-002 Book Coverage Tracker

## Review Basis

- Objective source reviewed: `DRAFT-CompTIA DataSys+ DS0-002 Draft Exam Objs 1.2.txt`
- Book source reviewed: the current root chapter notebooks from [Database_01_StarShipSQL.ipynb](Database_01_StarShipSQL.ipynb) through [Database_12_FinalProject.ipynb](Database_12_FinalProject.ipynb)
- Review standard:
  - `Met` = the book teaches the objective clearly enough to support quiz writing at the objective level.
  - `Partial` = the book teaches a meaningful portion of the objective, but important exam bullets are missing, scattered, or too light.
  - `Not Met` = the book does not currently teach the objective in a usable way.

## Planned Structural Changes

- Insert a new **Chapter 12: Data Integration at Emerald City Clinic** between the current Chapter 11 and the existing Final Project.
- Renumber the existing Final Project notebook from Chapter 12 to **Chapter 13**.
- Add the new chapter to `_toc.yml`, the index page chapter grid, and the Loop of the Recursive Dragon review-set list.
- All other insertions described below are added to existing chapters; no other notebook splits or merges are planned.

## Required Updates for Every Insertion

Every planned insertion below ships with the same four-part change set inside the target chapter. The per-objective entries spell out the specifics; this section is the standing checklist:

1. **New content cells** at the documented anchor inside the notebook.
2. **Learning Outcomes cell** updated to include new outcome bullets that mirror the inserted content.
3. **Chapter Summary cell** updated to include matching self-check bullets ("You can now…"). The Summary list stays parallel to the Learning Outcomes list, one-to-one.
4. **Glossary cell** extended with the listed new terms, sorted into the existing topical subsection or into a new subsection if the topic does not yet have one.

If an insertion crosses chapters, each affected chapter gets its own four-part update.

## Overall Snapshot

| Domain | Current alignment | Post-insertion target | Quick read |
| --- | --- | --- | --- |
| 1.0 Database Fundamentals | Strong partial | Met | Core SQL, modeling, and database concepts are strong; small inserts in Chapters 1, 6, and 9 close the remaining gaps. |
| 2.0 Database Deployment | Moderate partial | Strong partial | Deployment models are present; planning, operations, connectivity, and OLTP/OLAP need expansion in Chapter 11. |
| 3.0 Database Management and Maintenance | Moderate partial | Strong partial | Monitoring and tuning are covered; a maintenance-operations and alerts section in Chapter 8 closes most gaps. |
| 4.0 Data and Database Security | Strong partial | Met | Security is one of the book's strongest domains; advanced identity, governance, and platform security inserts in Chapter 10 finish it. |
| 5.0 Business Continuity | Strong partial | Met | The DR case study is substantial; a short terminology and fault-tolerance insert in Chapter 4 closes the remaining gaps. |
| 6.0 Data Integration | Weak | Met | A dedicated new chapter (Chapter 12) covers acquisition, troubleshooting, and emerging-tech/AI in one place. |

Current count by objective:

- Met: 1
- Partial: 17
- Not Met: 2

Post-insertion target by objective:

- Met: 20
- Partial: 0
- Not Met: 0

## Objective Review

## 1.0 Database Fundamentals

### 1.1 Compare and contrast database types and data types.

- Status: `Partial`
- Current coverage: [Database_01_StarShipSQL.ipynb](Database_01_StarShipSQL.ipynb) compares relational, document, graph, and column-oriented models and introduces conceptual, logical, and physical modeling. [Database_04_AdvancedSelect.ipynb](Database_04_AdvancedSelect.ipynb) and [Database_09_PokemonAndPostgres.ipynb](Database_09_PokemonAndPostgres.ipynb) reinforce JSON-focused storage.
- Missing or weak: Key-value, vector, time-series, and object-oriented databases are not taught. Structured vs. semistructured vs. unstructured data is not taught as a formal compare-and-contrast topic.

**Planned insertion**

- **Target chapter:** Chapter 1 (Starship SQL).
- **Anchor A:** Insert directly after the existing "Logical Model: Graphs for Networks of Connected Information" section and before "Logical Models: Columns for Analysis."
- **Anchor B:** Insert directly before "Physical Models: Choosing a DBMS."
- **Cells to add at Anchor A (one new H2 section, "Other database types you should know"):**
  1. *Markdown cell* — opening paragraph framed as Spock briefing the bridge crew: "Captain, four more data models deserve mention before we choose hardware." Then one short paragraph per type:
     - **Key-value databases** — Redis cache for the Enterprise's mission-status board; one example use.
     - **Vector databases** — pgvector / Pinecone; tied to "Spock's similarity searches across alien language samples."
     - **Time-series databases** — InfluxDB / TimescaleDB; tied to sensor telemetry from the warp core.
     - **Object-oriented databases** — db4o as a historical reference; tied to the holodeck's serialized object library.
  2. *Markdown cell* — short closing paragraph: "Most modern relational systems can simulate these patterns, but specialized stores trade flexibility for speed in their niche."
- **Cells to add at Anchor B (one new H2 section, "Structured, semistructured, and unstructured data"):**
  1. *Markdown cell* — three paragraphs (one per category) plus a small markdown table with columns *Shape*, *Example data*, *Typical storage*, *Typical access pattern*. Rows: Structured (crew roster CSV), Semistructured (mission log JSON), Unstructured (sensor video).
- **Narrative fit:** Reuses Spock, the Enterprise crew, mission logs, and sensor data already established in the chapter. No new characters introduced.
- **Learning Outcomes additions:**
  - Identify key-value, vector, time-series, and object-oriented databases and pick an appropriate use case for each.
  - Distinguish structured, semistructured, and unstructured data and match each to a sensible storage choice.
- **Chapter Summary additions:**
  - You can recognize key-value, vector, time-series, and object-oriented databases and name a use case for each.
  - You can sort data into structured, semistructured, and unstructured categories and explain why the category matters.
- **Glossary additions:** `key-value database`, `vector database`, `time-series database`, `object-oriented database`, `structured data`, `semistructured data`, `unstructured data`.

### 1.2 Given a scenario, develop, modify, and run SQL code.

- Status: `Met`
- Current coverage: [Database_02_IntroToSQL.ipynb](Database_02_IntroToSQL.ipynb), [Database_03_Joins_Sets_SQL.ipynb](Database_03_Joins_Sets_SQL.ipynb), [Database_04_AdvancedSelect.ipynb](Database_04_AdvancedSelect.ipynb), [Database_05_Design.ipynb](Database_05_Design.ipynb), [Database_06_WritingData.ipynb](Database_06_WritingData.ipynb), [Database_08_IndexesTransactions.ipynb](Database_08_IndexesTransactions.ipynb), [Database_09_PokemonAndPostgres.ipynb](Database_09_PokemonAndPostgres.ipynb), and [Database_12_FinalProject.ipynb](Database_12_FinalProject.ipynb) collectively cover DDL, DML, DQL, TCL, CRUD, set-based logic, joins, nested queries, window functions, triggers, stored procedures, and extensive hands-on SQL execution.
- Missing or weak: User-defined SQL functions are lighter than the rest of the objective.

**Planned insertion**

- **Target chapter:** Chapter 9 (Pokémon and PostgreSQL).
- **Anchor:** Insert as a new H3 inside the existing "Stored Procedures in PostgreSQL" section, immediately after the stored-procedure example.
- **Cells to add:**
  1. *Markdown cell* — H3 **"User-defined functions"**. Defines a UDF, contrasts it with a stored procedure (returns a value vs. performs an action), and introduces the Pokémon Research example.
  2. *Code cell* — `CREATE FUNCTION pokemon_age_in_days(captured_on DATE) RETURNS INTEGER LANGUAGE plpgsql AS $$ … $$;` returning the number of days a Pokémon has been in Professor Oak's care.
  3. *Code cell* — `SELECT name, pokemon_age_in_days(captured_on) AS age_days FROM pokemon ORDER BY age_days DESC LIMIT 10;`.
  4. *Markdown cell* — short closing note on when to use a UDF (reusable scalar calculation) vs. a procedure (multi-step side effects).
- **Narrative fit:** Reuses Professor Oak, the existing `pokemon` table, and the existing PL/pgSQL syntax already in the chapter.
- **Learning Outcomes additions:**
  - Write a user-defined function in PL/pgSQL and call it from a query.
- **Chapter Summary additions:**
  - You can create a user-defined function and call it from a `SELECT`.
- **Glossary additions:** `user-defined function`, `PL/pgSQL function`.

### 1.3 Compare and contrast scripting methods and environments.

- Status: `Partial`
- Current coverage: [Database_01_StarShipSQL.ipynb](Database_01_StarShipSQL.ipynb) and [Database_02_IntroToSQL.ipynb](Database_02_IntroToSQL.ipynb) introduce notebook-based SQL workflows. [Database_06_WritingData.ipynb](Database_06_WritingData.ipynb) compares CLI access, shell scripting, Python scripting, and ORM-based interaction patterns.
- Missing or weak: Server-side vs. client-side runtime, IDE scripting, and a formal compare-and-contrast of PowerShell, Unix shell, Python, and Perl are not present.

**Planned insertion**

- **Target chapter:** Chapter 6 (Writing Data).
- **Anchor:** Insert at the end of the existing "Case Study: Database Interaction Methods" section, before "2. Scripts and ORMs."
- **Cells to add:**
  1. *Markdown cell* — H3 **"Where scripts run: server-side, client-side, and IDE-based"**. Defines each location explicitly using the Rolling Stone admin dashboard scenario as the recurring example. Roughly 150 words.
  2. *Markdown cell* — H3 **"Scripting environments at a glance"** with a compare-and-contrast table. Columns: *Language*, *Where it runs*, *Typical role*, *How it connects to a database*. Rows: Bash/Unix shell, PowerShell, Python, Perl, JavaScript (browser), JavaScript (Node.js).
- **Narrative fit:** Reuses the Rolling Stone Greatest Albums admin/back-office framing already established in the chapter — for example, "the chart-update script the editorial team runs every Monday."
- **Learning Outcomes additions:**
  - Distinguish server-side, client-side, and IDE-based scripting environments.
  - Compare common scripting languages (Bash, PowerShell, Python, Perl, JavaScript) by where they run and how they reach a database.
- **Chapter Summary additions:**
  - You can name whether a script runs server-side, client-side, or inside an IDE, and explain why that matters.
  - You can compare the major scripting languages on where they run and how they connect to a database.
- **Glossary additions:** `server-side runtime`, `client-side runtime`, `IDE-based scripting`, `Perl`, `JavaScript (browser)`, `JavaScript (Node.js)`.

### 1.4 Explain the impact of programming on database performance.

- Status: `Partial`
- Current coverage: [Database_06_WritingData.ipynb](Database_06_WritingData.ipynb) introduces ORMs and other application interaction methods, and [Database_08_IndexesTransactions.ipynb](Database_08_IndexesTransactions.ipynb) teaches query plans, performance trade-offs, and tuning concepts.
- Missing or weak: Inspecting ORM-generated SQL, validating it, measuring its server-side impact, and remediating inefficient code are not taught.

**Planned insertion**

- **Target chapter:** Chapter 6 (Writing Data), with a forward reference to Chapter 8.
- **Anchor:** Insert at the end of the existing ORM subsection, before the chapter's Lab section.
- **Cells to add:**
  1. *Markdown cell* — H3 **"When ORMs go bad: the N+1 query problem"**. Tells the story of an editorial intern at Rolling Stone who lists every album and then loads each album's tracks separately, accidentally running hundreds of queries. ~150 words.
  2. *Code cell* — A small SQLAlchemy snippet that reproduces the N+1 pattern against the album/track tables, with `echo=True` logging the generated SQL.
  3. *Markdown cell* — Two short paragraphs: how to read the logged SQL, and a forward reference to Chapter 8's `EXPLAIN QUERY PLAN`.
  4. *Code cell* — `EXPLAIN QUERY PLAN` against the worst query, with the output annotated in a comment.
  5. *Code cell* — A fixed version using `joinedload()` (or the raw SQL equivalent), with the new query log showing one query instead of many.
  6. *Markdown cell* — Closing one-paragraph lesson: the database does not know about the application's intent; ORM convenience can hide expensive patterns.
- **Narrative fit:** Reuses the Rolling Stone Greatest Albums dataset and the editorial-team framing already in the chapter.
- **Learning Outcomes additions:**
  - Inspect the SQL an ORM generates, identify an N+1 problem, and refactor it.
- **Chapter Summary additions:**
  - You can read the SQL an ORM produces, spot an N+1 pattern, and rewrite it as a single efficient query.
- **Glossary additions:** `N+1 query problem`, `SQL logging`, `eager loading`.

## 2.0 Database Deployment

### 2.1 Compare and contrast aspects of database planning and operations.

- Status: `Partial`
- Current coverage: [Database_11_DesignDeployTest.ipynb](Database_11_DesignDeployTest.ipynb) covers on-premises, cloud, and hybrid deployment; IaaS, PaaS, SaaS, and DBaaS; DNS; and static vs. dynamic IPs. [Database_12_FinalProject.ipynb](Database_12_FinalProject.ipynb) requires schema validation, keys, and index decisions. [Database_04_AdvancedSelect.ipynb](Database_04_AdvancedSelect.ipynb) adds operational continuity context.
- Missing or weak: Requirements gathering, resource projection, SLAs/KPIs, deployment phases (provision/upgrade/import), computational persistence, and formal database validation workflows are thin or absent.

**Planned insertion**

- **Target chapter:** Chapter 11 (Design, Deployment, and Testing).
- **Anchor:** Insert as a new H2 section between "Introduction to Design Patterns" and the first pattern ("Normalize to 3NF").
- **Cells to add (one H2 section, "Planning and operations"):**
  1. *Markdown cell* — Opening paragraph framed through a fresh Oz-adjacent or pop-culture lens consistent with the chapter's existing rotating cast. Use the **Springfield Nuclear Power Plant** (already established in the 3NF section) for continuity. Mr. Burns is told he can't just "buy the database" — he needs a plan.
  2. *Markdown cell* — H3 **"Requirements gathering"**. Bulleted list of inputs: stakeholders, regulatory requirements, expected data volume, peak concurrent users, latency targets. ~120 words.
  3. *Markdown cell* — H3 **"Resource projection, SLAs, and KPIs"**. Defines SLA, SLO, and KPI. Includes a small table showing sample targets for Mr. Burns's plant (e.g., 99.9% uptime SLO, mean query latency < 200ms KPI).
  4. *Markdown cell* — H3 **"Deployment phases"**. Bulleted walkthrough of provision → configure → import → validate → upgrade → decommission. Defines **computational persistence** and **database validation workflow** as inline glossary terms.
  5. *Markdown cell* — Short closing paragraph: "Patterns sit on top of planning. The next sections cover the patterns; everything you build with them lives or dies by the plan above."
- **Narrative fit:** Reuses Springfield Nuclear Power Plant and Homer Simpson (already characters in §6 of Chapter 11). Mr. Burns plays the executive demanding answers.
- **Learning Outcomes additions:**
  - Identify the inputs to database requirements gathering and resource projection.
  - Define and apply SLAs, SLOs, KPIs, RPO, and RTO to a sample database deployment.
  - Walk a database through the standard deployment phases.
- **Chapter Summary additions:**
  - You can list the inputs to requirements gathering and resource projection.
  - You can define SLA, SLO, KPI, RPO, and RTO and pick reasonable targets.
  - You can name and order the deployment phases from provisioning through decommission.
- **Glossary additions:** `SLA`, `SLO`, `KPI`, `requirements gathering`, `resource projection`, `computational persistence`, `database validation workflow`, `provisioning`, `decommission`. (`RPO` and `RTO` already exist in Chapter 4's glossary; cross-reference rather than duplicate.)

### 2.2 Given a scenario, implement techniques related to database design and documentation.

- Status: `Partial`
- Current coverage: [Database_01_StarShipSQL.ipynb](Database_01_StarShipSQL.ipynb), [Database_05_Design.ipynb](Database_05_Design.ipynb), [Database_07_Views.ipynb](Database_07_Views.ipynb), and [Database_12_FinalProject.ipynb](Database_12_FinalProject.ipynb) cover logical and physical schema work, ERDs, data dictionaries, and written design documentation. [Database_08_IndexesTransactions.ipynb](Database_08_IndexesTransactions.ipynb) covers ACID vs. BASE. [Database_11_DesignDeployTest.ipynb](Database_11_DesignDeployTest.ipynb) introduces denormalized analytical patterns.
- Missing or weak: OLTP vs. OLAP is implied more than taught. SOP, organizational compliance documentation, maintenance documentation, and third-party compliance are not explicit skills.

**Planned insertion**

- **Target chapters:** Chapter 11 (OLTP/OLAP) and Chapter 13 (documentation packet).

**Chapter 11 piece**

- **Anchor:** Insert as a new H2 section immediately before "The Star Schema Pattern."
- **Cells to add (one H2 section, "OLTP vs. OLAP"):**
  1. *Markdown cell* — Bob Belcher's restaurant runs OLTP (each order is a transaction). Louise's analytics build on top of it is OLAP. Use that as the running example.
  2. *Markdown cell* — Two-column compare-and-contrast table: *Aspect*, *OLTP*, *OLAP*. Rows include workload, schema style, typical query, row vs. column orientation, refresh cadence.
  3. *Markdown cell* — Short closing paragraph that hands off to the star schema as the canonical OLAP pattern.
- **Narrative fit:** Reuses Bob Belcher's restaurant, Louise, Bob, and Jimmy Pesto (already in the chapter's star-schema section).
- **Learning Outcomes additions:**
  - Distinguish OLTP and OLAP workloads and explain when each pattern fits.
- **Chapter Summary additions:**
  - You can tell OLTP and OLAP workloads apart and pick the right schema style for each.
- **Glossary additions:** `OLTP`, `OLAP`.

**Chapter 13 piece (formerly Chapter 12 Final Project)**

- **Anchor:** Insert as a new H3 inside the existing project deliverables list, after the "Schema" requirement.
- **Cells to add:**
  1. *Markdown cell* — H3 **"Project documentation packet"**. Requires students to include:
     - A one-page **standard operating procedure (SOP)** for routine maintenance (backup, monitoring check, index rebuild).
     - A one-paragraph **organizational compliance** note naming the regulation(s) that would apply if the project were real (HIPAA, FERPA, etc.).
     - A one-paragraph **third-party compliance** note describing any vendor agreements the project would need.
     - A short **maintenance documentation** entry describing how schema changes will be tracked over time.
- **Narrative fit:** No new characters needed; the final project is student-selected.
- **Learning Outcomes additions (Chapter 13):**
  - Produce a documentation packet that includes an SOP, an organizational compliance note, a third-party compliance note, and a maintenance documentation entry.
- **Chapter Summary additions (Chapter 13):**
  - You can document a database project with an SOP, compliance notes, and a maintenance log.
- **Glossary additions:** `OLTP`, `OLAP` (Chapter 11); `standard operating procedure (SOP)`, `organizational compliance`, `third-party compliance`, `maintenance documentation` (Chapter 13).

### 2.3 Explain connectivity concepts related to databases.

- Status: `Partial`
- Current coverage: [Database_11_DesignDeployTest.ipynb](Database_11_DesignDeployTest.ipynb) teaches DNS and static/dynamic IP concepts. [Database_09_PokemonAndPostgres.ipynb](Database_09_PokemonAndPostgres.ipynb) reinforces the difference between embedded and server-based databases. [Database_10_DatabaseSecurity.ipynb](Database_10_DatabaseSecurity.ipynb) covers firewalls, segmentation, and common service ports.
- Missing or weak: Load balancing, multizone region design, client/server architecture as a named concept, and a structured ports/protocols lesson are missing or scattered.

**Planned insertion**

- **Target chapter:** Chapter 11.
- **Anchor:** Insert as a new H2 section immediately after the "Hybrid: The Best (or Worst) of Both Worlds" section and before "Database Testing."
- **Cells to add (one H2 section, "Connectivity"):**
  1. *Markdown cell* — Opening paragraph using Rick and Morty's interdimensional infrastructure (already in the chapter). The Council of Ricks's database has to stay reachable across dimensions; Rick explains how.
  2. *Markdown cell* — H3 **"Client/server vs. embedded, named explicitly"**. One paragraph each. Cross-reference Chapter 9 (PostgreSQL is server-based) and SQLite (embedded).
  3. *Markdown cell* — H3 **"Load balancing and multizone deployment"**. Two paragraphs: what load balancing does, what multizone means, when each is appropriate. Includes a textual ASCII-style diagram describing the topology Rick sets up across two Council dimensions.
  4. *Markdown cell* — H3 **"Ports and protocols you'll see"**. Single markdown table with columns *Service*, *Default port*, *Transport*, *Typical client tool*. Rows: PostgreSQL 5432 / TCP, MySQL 3306 / TCP, SQL Server 1433 / TCP, Oracle 1521 / TCP, MongoDB 27017 / TCP, Redis 6379 / TCP.
- **Narrative fit:** Reuses Rick, Morty, and the Council of Ricks (already in the chapter's deployment-models section).
- **Learning Outcomes additions:**
  - Distinguish client/server, embedded, load-balanced, and multizone deployment architectures.
  - Identify the default ports and transport protocols of common DBMSes.
- **Chapter Summary additions:**
  - You can name client/server, embedded, load-balanced, and multizone architectures and pick the right one for a situation.
  - You can list the default port for each common DBMS.
- **Glossary additions:** `client/server architecture`, `embedded database`, `load balancing`, `multizone region`, `database connection string`.

## 3.0 Database Management and Maintenance

### 3.1 Explain the purpose of monitoring and reporting for database management and performance.

- Status: `Partial`
- Current coverage: [Database_08_IndexesTransactions.ipynb](Database_08_IndexesTransactions.ipynb) covers health checks, performance metrics, logs, storage trade-offs, throughput-adjacent monitoring, and deadlock/concurrency concerns.
- Missing or weak: Alerts and notifications, baseline configuration, backup alerts, job completion/failure monitoring, and connection/session monitoring are not taught as a coherent operations discipline.

**Planned insertion**

- **Target chapter:** Chapter 8 (Indexes and Transactions).
- **Anchor:** Insert as a new H2 section immediately after the existing "NoSQL Case Study: Harley's Havoc" section and before "Chapter Summary."
- **Cells to add (one H2 section, "Monitoring as an operations discipline"):**
  1. *Markdown cell* — Opening paragraph at Gotham National Bank: the DBA team has dashboards, not just intuition. Frame the topic as the everyday job of a database administrator.
  2. *Markdown cell* — H3 **"Baselines and thresholds"**. Defines baseline configuration as "what normal looks like." Explains why thresholds make sense only after a baseline.
  3. *Markdown cell* — H3 **"Alerts and notifications"**. Three short paragraphs: what an alert is, how notifications are delivered (email, pager, chat channel), and one example alert specification (e.g., "Page on-call when replication lag exceeds 30 seconds for more than 2 minutes").
  4. *Markdown cell* — H3 **"What DBAs watch every day"**. Bulleted checklist: job completion/failure, backup success or failure, connection/session counts, disk space, replication lag, slow-query growth.
  5. *Markdown cell* — Sample dashboard table for Gotham National Bank with columns *Metric*, *Today's value*, *Baseline*, *Alert threshold*, *Status*. Five rows of fictional data.
- **Narrative fit:** Reuses Gotham National Bank, the existing case study in the chapter.
- **Learning Outcomes additions:**
  - Establish a baseline configuration and design alerts and notifications based on it.
  - List the metrics a DBA monitors daily and connect each to an operational concern.
- **Chapter Summary additions:**
  - You can describe a baseline configuration and explain why alerts depend on one.
  - You can list the daily monitoring tasks of a DBA and explain why each matters.
- **Glossary additions:** `baseline configuration`, `alert`, `notification`, `job monitoring`, `session monitoring`, `replication lag`.

### 3.2 Explain common database maintenance processes.

- Status: `Partial`
- Current coverage: [Database_08_IndexesTransactions.ipynb](Database_08_IndexesTransactions.ipynb) teaches performance tuning, index optimization, query optimization, and log review. [Database_11_DesignDeployTest.ipynb](Database_11_DesignDeployTest.ipynb) teaches partitioning.
- Missing or weak: Patch management, integrity checks, CI/CD, change approval, release schedules, database refresh, and version control as maintenance operations are not sufficiently taught.

**Planned insertion**

- **Target chapter:** Chapter 8.
- **Anchor:** Insert as a new H2 section immediately after the new "Monitoring as an operations discipline" section from §3.1, before "Chapter Summary."
- **Cells to add (one H2 section, "Maintenance operations"):**
  1. *Markdown cell* — Opening paragraph: Commissioner Gordon receives a quarterly maintenance plan from the IT team. Frame the topic as "scheduled change, on purpose, with a paper trail."
  2. *Markdown cell* — H3 **"Patch and release management"**. Defines patch management, release schedule, and change approval; describes a sample quarterly cycle at Gotham National.
  3. *Markdown cell* — H3 **"Integrity checks and database refresh"**. Explains what an integrity check looks for (corruption, broken constraints) and how a database refresh moves production data into a non-production environment for testing.
  4. *Markdown cell* — H3 **"Version control and CI/CD for databases"**. Short paragraph on schema migrations; names Flyway and Liquibase as common tools; outlines a CI/CD pipeline that runs migrations on every deploy.
- **Narrative fit:** Reuses Gotham National Bank, Commissioner Gordon (introduced in the existing chapter framing), and the IT team.
- **Learning Outcomes additions:**
  - Plan a database patch and release cycle including change approval and release schedules.
  - Distinguish integrity checks from database refreshes and describe when to use each.
  - Apply version control and CI/CD concepts to database schema changes.
- **Chapter Summary additions:**
  - You can outline a patch-management cycle that includes change approval and a release schedule.
  - You can run an integrity check and explain when a database refresh is appropriate.
  - You can describe how version control and CI/CD pipelines apply to database schemas.
- **Glossary additions:** `patch management`, `change approval`, `release schedule`, `integrity check`, `database refresh`, `schema migration`, `CI/CD`.

### 3.3 Given a scenario, implement data management tasks.

- Status: `Partial`
- Current coverage: [Database_05_Design.ipynb](Database_05_Design.ipynb), [Database_06_WritingData.ipynb](Database_06_WritingData.ipynb), [Database_07_Views.ipynb](Database_07_Views.ipynb), [Database_08_IndexesTransactions.ipynb](Database_08_IndexesTransactions.ipynb), [Database_09_PokemonAndPostgres.ipynb](Database_09_PokemonAndPostgres.ipynb), and [Database_12_FinalProject.ipynb](Database_12_FinalProject.ipynb) collectively cover defining and modifying data, adding columns, creating views, indexes, tables, and relationships, plus normalization and denormalized analytical design.
- Missing or weak: Create statistics, isolation levels as a configurable implementation topic, and computed columns are not taught directly.

**Planned insertion**

- **Target chapters:** Chapter 8 (statistics, isolation levels) and Chapter 9 (computed columns).

**Chapter 8 piece**

- **Anchor A:** Inside the existing performance section, after the index-impact discussion.
- **Anchor B:** Inside the existing transactions section, after the BEGIN/COMMIT/ROLLBACK walkthrough.
- **Cells to add at Anchor A:**
  1. *Markdown cell* — H3 **"Statistics and the query planner"**. Short paragraph explaining that the planner relies on statistics to choose indexes; outdated statistics produce bad plans.
  2. *Code cell* — A PostgreSQL `ANALYZE customers;` example (Gotham National Bank's `customers` table).
- **Cells to add at Anchor B:**
  1. *Markdown cell* — H3 **"Isolation levels in practice"**. Defines READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, and SERIALIZABLE with one-line examples of the anomaly each one prevents.
  2. *Code cell* — A PostgreSQL `BEGIN; SET TRANSACTION ISOLATION LEVEL SERIALIZABLE; …; COMMIT;` example using a Gotham National Bank transfer between two accounts.
  3. *Markdown cell* — One-paragraph wrap explaining why higher isolation costs more concurrency.

**Chapter 9 piece**

- **Anchor:** Insert as a new H3 inside the existing Postgres data-types section, after the JSONB walkthrough.
- **Cells to add:**
  1. *Markdown cell* — H3 **"Computed columns"**. Defines a computed (generated) column. Uses the Pokémon `pokemon` table: a `display_label` column generated from `name` and `species`.
  2. *Code cell* — `ALTER TABLE pokemon ADD COLUMN display_label TEXT GENERATED ALWAYS AS (name || ' the ' || species) STORED;` followed by a `SELECT name, display_label FROM pokemon LIMIT 5;`.
- **Narrative fit:** Reuses Gotham National Bank (Chapter 8) and Professor Oak's `pokemon` table (Chapter 9).
- **Learning Outcomes additions (Chapter 8):**
  - Update query-planner statistics and explain how stale statistics hurt performance.
  - Choose and configure a transaction isolation level appropriate for a workload.
- **Chapter Summary additions (Chapter 8):**
  - You can refresh query statistics and explain when it matters.
  - You can pick an isolation level and explain the trade-off it makes.
- **Learning Outcomes additions (Chapter 9):**
  - Create and use a computed column.
- **Chapter Summary additions (Chapter 9):**
  - You can add a computed column and explain when it is useful.
- **Glossary additions:** `isolation level`, `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`, `query statistics`, `ANALYZE` (Chapter 8); `computed column`, `generated column` (Chapter 9).

## 4.0 Data and Database Security

### 4.1 Explain data security concepts.

- Status: `Partial`
- Current coverage: [Database_10_DatabaseSecurity.ipynb](Database_10_DatabaseSecurity.ipynb) strongly covers encryption at rest and in transit, client-side vs. transport protection, masking, discovery and classification, destruction, security audits, and code auditing.
- Missing or weak: BYOK, KYOK, confidential computing, and explicit treatment of anonymization and suppression.

**Planned insertion**

- **Target chapter:** Chapter 10 (Database Security).
- **Anchor A:** Insert as a new H3 inside the existing "Where Encryption Is Applied" section.
- **Anchor B:** Insert as a new H3 immediately after the "Data Masking" section.
- **Cells to add at Anchor A:**
  1. *Markdown cell* — H3 **"Advanced key management"**. Three paragraphs:
     - **BYOK (bring your own key)** — what it is, why a regulated hospital like Toad City Hospital might require it.
     - **KYOK (keep your own key)** — what it is, contrast with BYOK.
     - **Confidential computing** — definition, with a one-sentence example of processing patient records inside a trusted execution environment.
- **Cells to add at Anchor B:**
  1. *Markdown cell* — H3 **"Anonymization and suppression"**. Defines both and contrasts with masking. Uses Toad City Hospital's de-identified research export as the worked example.
- **Narrative fit:** Reuses Toad City Hospital and the existing patient-data examples.
- **Learning Outcomes additions:**
  - Compare BYOK, KYOK, and confidential computing as advanced key-management options.
  - Distinguish anonymization, suppression, and masking and pick the right one for a use case.
- **Chapter Summary additions:**
  - You can describe BYOK, KYOK, and confidential computing and explain when each applies.
  - You can tell anonymization, suppression, and masking apart and pick the right one for a situation.
- **Glossary additions:** `BYOK`, `KYOK`, `confidential computing`, `anonymization`, `suppression`.

### 4.2 Explain the purpose of governance and regulatory compliance.

- Status: `Partial`
- Current coverage: [Database_07_Views.ipynb](Database_07_Views.ipynb) and [Database_10_DatabaseSecurity.ipynb](Database_10_DatabaseSecurity.ipynb) cover data loss prevention, retention, classification, GDPR, and sensitive-data handling. The hospital examples also support PII/PHI framing.
- Missing or weak: Data sovereignty, data residency, PCI DSS, and broader regional compliance framing are not explicitly taught.

**Planned insertion**

- **Target chapter:** Chapter 10.
- **Anchor:** Insert as a new H2 section immediately after the threats sections and before "What is encryption."
- **Cells to add (one H2 section, "Compliance frameworks at a glance"):**
  1. *Markdown cell* — Opening paragraph: Toad City Hospital's compliance officer maintains a shelf of binders. Frame the section as a quick tour of the binders.
  2. *Markdown cell* — Compliance table with columns *Framework*, *Region*, *Applies to*, *Sample requirement*. Rows: GDPR, CCPA, PIPL, HIPAA, PCI-DSS, SOX, FERPA.
  3. *Markdown cell* — H3 **"Data sovereignty and residency"**. Defines both terms and uses a Toad City example: storing EU patient records on servers physically located in the EU.
- **Narrative fit:** Reuses Toad City Hospital. Compliance officer is a new minor character, but stays consistent with the established hospital cast.
- **Learning Outcomes additions:**
  - Identify the major data-protection frameworks (GDPR, CCPA, PIPL, HIPAA, PCI-DSS, SOX, FERPA) and the kind of data each one protects.
  - Distinguish data sovereignty from data residency.
- **Chapter Summary additions:**
  - You can match a data-protection framework to the kind of data it covers.
  - You can tell data sovereignty and data residency apart.
- **Glossary additions:** `data sovereignty`, `data residency`, `PCI DSS`, `SOX`, `CCPA`, `PIPL`, `FERPA`.

### 4.3 Given a scenario, implement policies and best practices related to authentication and authorization.

- Status: `Partial`
- Current coverage: [Database_09_PokemonAndPostgres.ipynb](Database_09_PokemonAndPostgres.ipynb) covers users, roles, and privileges. [Database_10_DatabaseSecurity.ipynb](Database_10_DatabaseSecurity.ipynb) covers RBAC, ABAC, 2FA, and SSO conceptually.
- Missing or weak: Kerberos/SPNs, IAM and federated identity, OAuth, OpenID Connect, and SSL certificate management.

**Planned insertion**

- **Target chapter:** Chapter 10.
- **Anchor:** Insert as a new H2 section immediately after the "Three As: Authentication, Authorization, Access Control" section and before "Database: Physical Security."
- **Cells to add (one H2 section, "Advanced identity"):**
  1. *Markdown cell* — Opening paragraph: when Toad City Hospital adds clinic locations, every new login can't be a fresh password. The IT director introduces federated identity.
  2. *Markdown cell* — H3 **"Federated identity, IAM, and SSO in practice"**. Defines IAM, federated identity, and identity provider. Clarifies SSO as a common outcome of federation.
  3. *Markdown cell* — H3 **"OAuth and OpenID Connect"**. One paragraph each. Contrast: OAuth = authorization, OIDC = authentication on top of OAuth.
  4. *Markdown cell* — H3 **"Kerberos and SPNs"**. One paragraph each, with a sentence on the Windows domain context most readers will see them in.
  5. *Markdown cell* — H3 **"SSL/TLS certificate management"**. Defines certificate, certificate authority, certificate lifecycle (issue → install → renew → revoke). Uses Toad City's database server certificate as the example.
- **Narrative fit:** Reuses Toad City Hospital, the IT director (new minor character), and the existing IT team.
- **Learning Outcomes additions:**
  - Explain IAM, federated identity, and SSO and how they relate.
  - Distinguish OAuth from OpenID Connect.
  - Describe how Kerberos authentication and service principal names work in a typical Windows domain.
  - Manage the SSL/TLS certificate lifecycle for a database server.
- **Chapter Summary additions:**
  - You can describe IAM, federated identity, and SSO and how they relate.
  - You can tell OAuth and OpenID Connect apart.
  - You can describe how Kerberos and SPNs work in a Windows-domain environment.
  - You can list the stages of the SSL/TLS certificate lifecycle.
- **Glossary additions:** `IAM`, `federated identity`, `identity provider`, `OAuth`, `OpenID Connect`, `Kerberos`, `service principal name (SPN)`, `certificate authority`, `certificate revocation`.

### 4.4 Explain the purpose of database security.

- Status: `Partial`
- Current coverage: [Database_10_DatabaseSecurity.ipynb](Database_10_DatabaseSecurity.ipynb) covers physical security, logical security, firewalls, network segmentation, SQL injection, malware, phishing, brute force, audits, and vulnerability review.
- Missing or weak: Zero Trust, attack surface management, patch/remediation cycle, and data poisoning.

**Planned insertion**

- **Target chapter:** Chapter 10.
- **Anchor:** Insert as a new H2 section immediately before the existing "Database: Physical Security" section.
- **Cells to add (one H2 section, "Platform security architecture"):**
  1. *Markdown cell* — Opening paragraph framed at Toad City Hospital: the IT director draws a new architecture diagram on the whiteboard. "We don't trust anything by default. Even our own systems."
  2. *Markdown cell* — H3 **"Zero Trust"**. Defines the term, lists three core principles: verify explicitly, least-privilege access, assume breach.
  3. *Markdown cell* — H3 **"Attack surface management"**. Defines attack surface; bullet list of typical attack surfaces (open ports, exposed APIs, third-party libraries, employee endpoints, shared service accounts).
  4. *Markdown cell* — H3 **"Patch and remediation cycle"**. Short narrative (discover → assess → patch → verify) tied to §3.2's patch management. Use a Toad City example: a vulnerability disclosed in the database driver triggers the cycle.
  5. *Markdown cell* — H3 **"Data poisoning"**. Defines the term and gives a short healthcare-flavored ML example: an attacker submits crafted records to skew a hospital readmission-risk model. Forward-references Chapter 12's AI section.
- **Narrative fit:** Reuses Toad City Hospital and its IT director.
- **Learning Outcomes additions:**
  - Explain Zero Trust and its three core principles.
  - Identify and inventory common attack surfaces for a database platform.
  - Outline a patch-and-remediation cycle for a database vulnerability.
  - Describe data poisoning and how it differs from other threats.
- **Chapter Summary additions:**
  - You can explain Zero Trust and its three core principles.
  - You can list common attack surfaces and explain why each matters.
  - You can walk through the patch and remediation cycle.
  - You can define data poisoning and give an example.
- **Glossary additions:** `Zero Trust`, `attack surface`, `attack surface management`, `remediation cycle`, `data poisoning`.

## 5.0 Business Continuity

### 5.1 Given a scenario, implement backup and restoration processes.

- Status: `Partial`
- Current coverage: [Database_04_AdvancedSelect.ipynb](Database_04_AdvancedSelect.ipynb) covers scheduling backups, full/incremental/differential backup types, database dumping, backup validation with hashes, on-site vs. off-site storage, archiving, and retention policy.
- Missing or weak: Snapshots, restore points as a named concept, and reports/alerts around backup operations.

**Planned insertion**

- **Target chapter:** Chapter 4 (Advanced SELECT — includes the Toad Medical Center business-continuity case study).
- **Anchor:** Insert inside the existing "Case Study: Business Continuity at the Toad Medical Center" section, after the backup-types subsection and before the disaster-recovery subsection.
- **Cells to add:**
  1. *Markdown cell* — H3 **"Snapshots and restore points"**. Defines a snapshot (storage-system point-in-time copy) and a restore point (named marker an admin can roll back to). Contrasts both with the backup files already discussed in the chapter.
  2. *Markdown cell* — Short paragraph on **"Backup reporting"** — explains that backup jobs send success/failure reports and alerts, with a cross-reference to §3.1's monitoring section in Chapter 8.
- **Narrative fit:** Reuses Toad Medical Center and the existing disaster-recovery characters from the chapter's case study.
- **Learning Outcomes additions:**
  - Distinguish snapshots, restore points, and backup files.
  - Use backup reports and alerts to confirm backup health.
- **Chapter Summary additions:**
  - You can tell snapshots, restore points, and backup files apart.
  - You can explain how backup reports and alerts fit into routine operations.
- **Glossary additions:** `snapshot`, `restore point`, `backup report`.

### 5.2 Explain the importance of disaster recovery and best practices.

- Status: `Partial`
- Current coverage: [Database_04_AdvancedSelect.ipynb](Database_04_AdvancedSelect.ipynb) covers DR planning, documentation, DR plan testing, RPO, RTO, replication, log shipping, high availability, mirroring, and failover connections.
- Missing or weak: SSP, COOP, and SDD terminology, and failback.

**Planned insertion**

- **Target chapter:** Chapter 4.
- **Anchor:** Insert as a new H3 subsection inside the existing Toad Medical Center case study, near the end of the DR coverage and before the chapter's lab.
- **Cells to add:**
  1. *Markdown cell* — H3 **"DR terminology bridge"**. Four short paragraphs, each one a definition plus a one-line Toad Medical Center example:
     - **System Security Plan (SSP)** — Toad Medical's central security blueprint that auditors review.
     - **Continuity of Operations Plan (COOP)** — the plan that keeps essential services running during disruption.
     - **System Design Document (SDD)** — the architecture document the DR plan refers back to.
     - **Failback** — returning to the primary site after a failover, with the formal checklist that goes with it.
- **Narrative fit:** Reuses Toad Medical Center and its DR team.
- **Learning Outcomes additions:**
  - Define and apply SSP, COOP, SDD, and failback to a disaster recovery scenario.
- **Chapter Summary additions:**
  - You can define SSP, COOP, SDD, and failback and explain how each fits the DR process.
- **Glossary additions:** `System Security Plan (SSP)`, `Continuity of Operations Plan (COOP)`, `System Design Document (SDD)`, `failback`.

### 5.3 Compare and contrast fault tolerance operations.

- Status: `Partial`
- Current coverage: [Database_04_AdvancedSelect.ipynb](Database_04_AdvancedSelect.ipynb) teaches high availability, redundant systems, replication, mirroring, and transaction-log-based continuity techniques.
- Missing or weak: Single point of failure, geo-replication, and multizone region design.

**Planned insertion**

- **Target chapter:** Chapter 4 (with a short cross-reference in Chapter 11's new connectivity section from §2.3).
- **Anchor:** Insert as a new H3 subsection inside the existing Toad Medical Center case study, in the fault-tolerance discussion, before the new "DR terminology bridge" from §5.2.
- **Cells to add:**
  1. *Markdown cell* — H3 **"Eliminating single points of failure"**. Defines SPOF, then a bullet list of common SPOFs (single web server, single database node, single power feed, single network path) paired with the standard mitigation for each.
  2. *Markdown cell* — Short paragraph defining **geo-replication** and **multizone region** with one-sentence Toad Medical examples (e.g., a second medical center across the state takes over read traffic when the primary becomes unreachable).
- **Narrative fit:** Reuses Toad Medical Center.
- **Learning Outcomes additions:**
  - Identify single points of failure in a database architecture and pair each with a mitigation.
  - Compare geo-replication and multizone region designs.
- **Chapter Summary additions:**
  - You can spot single points of failure and propose a fix for each.
  - You can compare geo-replication and multizone region designs.
- **Glossary additions:** `single point of failure (SPOF)`, `geo-replication`, `multizone region`.

## 6.0 Data Integration

### 6.1 Given a scenario, use data acquisition techniques and methods.

- Status: `Partial`
- Current coverage: [Database_07_Views.ipynb](Database_07_Views.ipynb) and [Database_10_DatabaseSecurity.ipynb](Database_10_DatabaseSecurity.ipynb) cover data classification. [Database_11_DesignDeployTest.ipynb](Database_11_DesignDeployTest.ipynb) briefly mentions ETL in the star-schema discussion. JSON and flat-file-adjacent formats appear elsewhere.
- Missing or weak: No dedicated data acquisition chapter. ODBC, JDBC, OData, FTP, NFS, SSH, CIFS, RPC, SOAP, streaming vs. non-streaming sources, scraping, XML, and scenario-based acquisition workflows are largely absent.

**Planned insertion**

- Covered by the new Chapter 12 (see "Planned Chapter 12" section below).

### 6.2 Given a scenario, troubleshoot common data acquisition issues.

- Status: `Not Met`
- Current coverage: Only scattered adjacent concepts exist, such as corruption, timeout, and key-related references in other chapters.
- Missing or weak: Schema mismatch, encoding, permissions, driver/version issues, encryption key handling in acquisition workflows, and syntax/runtime acquisition failures are not a real instructional unit.

**Planned insertion**

- Covered by the new Chapter 12 (see "Planned Chapter 12" section below).

### 6.3 Explain emerging technologies and AI concepts related to data integration.

- Status: `Not Met`
- Current coverage: A few incidental AI references; nothing as part of data integration instruction.
- Missing or weak: ML libraries, hallucinations, prompt engineering, retrieval-augmented generation, human-in-the-loop workflows, virtual data warehouses, and RPA are absent.

**Planned insertion**

- Covered by the new Chapter 12 (see "Planned Chapter 12" section below).

## Planned Chapter 12: Data Integration at Emerald City Clinic

### Premise and theme

The new chapter follows the data team at **Emerald City Clinic** (a Wizard of Oz–themed medical facility on the outskirts of Oz) as they consolidate data from multiple departments and partner organizations into a single SQLite warehouse. Each character represents a real-world data integration challenge:

- **Dorothy** (newly hired data engineer) — leads the integration project.
- **The Scarecrow** (records team) — provides CSV exports of patient demographics.
- **The Tin Man** (lab systems) — exposes lab results through a JSON REST API.
- **The Cowardly Lion** (security/compliance) — owns access control, certificate handling, and encryption-at-rest concerns.
- **The Wizard** (CIO) — sets strategic direction and signs off on the deployment.
- **Glinda** (analytics) — consumes the consolidated warehouse for reporting.

Tone and scope match the rest of the book: pop-culture framing, hands-on code, ~9th grade reading level, lab activity, glossary, and a LotRD review set.

### Tools used

- **SQLite** for the target warehouse, consistent with Chapters 1–8 and 12 (now 13).
- **Python (Pandas)** for transformation. Pandas is introduced minimally — enough to read CSV/JSON, clean columns, and write to SQLite via `to_sql`. No deep dataframe pedagogy; this is a database course.
- **Python's standard library** (`csv`, `json`, `sqlite3`, `urllib.request`) for cases where Pandas would be overkill.
- **A simple data generator** at the top of the chapter that produces all sample files (CSV, JSON, XML, a small SOAP-style response) so students can re-run the chapter from scratch.

### Chapter outline (cell-level)

1. **Colab badge** — standard top-of-notebook cell.
2. **Title and chapter intro** — H1 + subtitle + 2–3 sentence overview of Emerald City Clinic.
3. **Learning Outcomes** — standardized cell, populated from the per-section "Learning Outcomes additions" below.
4. **Brendan's Lecture** — placeholder.
5. **Introduction to Emerald City Clinic** — premise, character map, what we're building.
6. **Generating the source data** — *Code cell* runs `data/emerald_city/generator.py`, producing CSV, JSON, XML, an HTML scraping target, and a short SOAP envelope. Deterministic (seeded), so row counts can be cited in quizzes.
7. **§ 6.1 Acquisition techniques and methods** — one H2 section, broken into eight short H3 subsections, each with one markdown cell + one or two code cells:
   - **File-based: CSV** — Scarecrow's patient roster.
   - **File-based: JSON** — Tin Man's lab results (file form).
   - **File-based: XML** — the Wizard's old chart system.
   - **API-based: REST and OData** — Tin Man's lab API, mocked locally.
   - **Driver-based: ODBC and JDBC** — defined conceptually; one SQLAlchemy example connecting to a separate SQLite source file.
   - **Network protocols** — compare-and-contrast table of FTP, NFS, SSH, CIFS, RPC, SOAP. One short SOAP request/response shown.
   - **Streaming vs. non-streaming** — Python generator that yields one lab result at a time vs. a batch load.
   - **Web scraping** — `requests` + `BeautifulSoup` against a tiny local HTML file the generator writes; ethics paragraph included.
8. **Transforming the data with Pandas** — one H2 section with a focused Pandas minimum: `read_csv`, `read_json`, basic cleanup (column rename, type coercion), `merge`, and `to_sql`. Cross-references Chapter 1's data-types section.
9. **Loading into SQLite: ETL vs. ELT** — one H2 section. Defines both, then shows an ETL example (transform in Pandas before insert) and an ELT example (load raw, transform with SQL views).
10. **§ 6.2 Troubleshooting common data acquisition issues** — one H2 section with seven short H3 subsections, each in a "broken then fixed" structure (markdown setup, broken code cell, markdown diagnosis, fixed code cell):
    - **Schema mismatch** — CSV column rename silently shifts columns.
    - **Encoding** — Windows-1252 CSV opened as UTF-8 throws `UnicodeDecodeError`.
    - **Permissions** — a source file the script cannot read.
    - **Driver and version issues** — Pandas refusing an old `sqlite3` version; how to read the stack trace.
    - **Encryption keys in acquisition** — a key file in the wrong place; cross-link to Chapter 10.
    - **Timeouts and corruption** — a deliberately truncated JSON file; detect, log, recover.
    - **Syntax and runtime errors** — the most common Python and SQL exceptions during ingestion.
11. **§ 6.3 Emerging tech and AI in data integration** — one H2 section with seven short H3 subsections:
    - **Where AI helps in this workflow** — practical uses inside the Emerald City pipeline.
    - **Prompt engineering and human-in-the-loop** — definitions plus Dorothy using a chatbot to draft an XML parser.
    - **Hallucinations and verification** — one realistic hallucinated SQL example, why it fails, why human review matters.
    - **Retrieval-augmented generation (RAG)** — definition; example of Emerald City staff asking questions over the warehouse.
    - **ML libraries** — pandas, scikit-learn, PyTorch, TensorFlow named; data prep vs. model training.
    - **Virtual data warehouses** — definition; contrast with materialized warehouses.
    - **Robotic process automation (RPA)** — definition; one example of automating a recurring CSV pull from a partner organization.
12. **Lab activity** — students extend the pipeline by adding one new source (e.g., a pharmacy CSV) and writing the matching loader. Guided checkpoints provided.
13. **Chapter Summary** — uniform self-check format. Bullets mirror every Learning Outcome.
14. **Practice with the Loop of the Recursive Dragon** — new review set, `database_12_data_integration.json` (or similar), wired into the LotRD link script.
15. **Glossary** — see term list below.

### Learning Outcomes for Chapter 12

- Acquire data from CSV, JSON, XML, REST, OData, ODBC/JDBC, FTP, NFS, SSH, CIFS, RPC, SOAP, streaming sources, and scraped HTML.
- Use Pandas to read source data, clean it, merge it, and load it into SQLite.
- Distinguish ETL from ELT and decide which pattern fits a scenario.
- Diagnose and fix the most common data acquisition failures: schema mismatch, encoding, permissions, driver/version issues, encryption key handling, timeouts, corruption, and syntax/runtime errors.
- Explain where AI and modern tooling — prompt engineering, RAG, virtual data warehouses, ML libraries, RPA — help and where they introduce risk.

### Chapter Summary for Chapter 12 (self-check)

- You can pull data from each of the major acquisition formats and protocols.
- You can use Pandas to transform source data and load it into SQLite.
- You can pick between ETL and ELT for a given scenario.
- You can diagnose and recover from the most common data acquisition failures.
- You can describe how AI tools help with integration work and what their limits are.

### Glossary for Chapter 12

- Includes: `ETL`, `ELT`, `ODBC`, `JDBC`, `OData`, `REST`, `SOAP`, `RPC`, `FTP`, `NFS`, `SSH`, `CIFS`, `streaming source`, `non-streaming source`, `web scraping`, `XML`, `schema mismatch`, `character encoding`, `driver version mismatch`, `data poisoning` (cross-referenced from Chapter 10), `prompt engineering`, `retrieval-augmented generation`, `hallucination`, `human-in-the-loop`, `virtual data warehouse`, `robotic process automation`.

### Cross-chapter impacts

- `_toc.yml`: insert `Database_12_DataIntegration` between Chapter 11 and the existing Final Project.
- Rename the existing `Database_12_FinalProject.ipynb` to `Database_13_FinalProject.ipynb` and update its `_toc.yml` entry.
- Update `index.md`: add a Chapter 12 card and renumber the final-project card to 13.
- Update the LotRD link script and `index.md` to include the new chapter's review set.
- Update Chapter 11's "Star Schema" section to add a one-sentence forward reference to Chapter 12.
- Cross-reference from Chapter 4 fault-tolerance and from Chapter 10's data-poisoning paragraph.

### Companion data generator

A small `data/emerald_city/generator.py` script (added at the same time as the chapter) produces all sample files used in the chapter. It must be deterministic with a seed so quizzes can reference specific row counts and values.

## Immediate Quiz-Writing Guidance

- Quiz-eligible **today** at the full objective level: `1.2`.
- Quiz-eligible at the **subtopic level** after the inserts in §§ 1.1, 1.3, 1.4, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 4.4, 5.1, 5.2, 5.3 are landed: full objective coverage.
- Quiz-eligible at the **full objective level** once Chapter 12 ships: `6.1`, `6.2`, `6.3`.
- Until each insert lands, continue to write quiz items only on the specific subtopics already in the book, not the full CompTIA objective envelope.
