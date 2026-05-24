# CompTIA DataSys+ DS0-002 Unmet Objectives Plan

## Goal

Move the book from its current state of strong topic coverage in core SQL, security, and continuity to a full exam-alignment state where all partial and not-met objectives can support both quizzes and CompTIA-style outcome mapping.

## Planning Principles

- Prefer extending the strongest existing chapters before creating entirely new material.
- Add new chapters only where the current book has a true structural gap, not just a light subsection gap.
- Update chapter learning outcomes, glossary entries, labs, and quiz pools together so coverage does not drift again.
- Use scenario-driven additions, because the CompTIA objectives are heavily phrased as applied tasks rather than pure definitions.

## Recommended Sequence

## Priority 1: Add a dedicated Data Integration chapter

- Target objectives: `6.1`, `6.2`, `6.3`
- Why first: Domain 6 is the clearest coverage gap in the current book. Two objectives are not met, and the remaining objective is only lightly implied.
- Recommended format: add a new notebook such as `Database_13_DataIntegration.ipynb`
- Proposed sections:
  - Why data integration matters: operational systems, analytical systems, and data movement between them
  - ETL vs. ELT with one concrete example
  - Batch vs. streaming acquisition
  - APIs, flat files, JSON, XML, and basic scraping
  - Connectivity methods: ODBC, JDBC, OData, FTP, NFS, SSH, CIFS, RPC, SOAP, and REST-style APIs
  - Data classification during ingestion
  - Common acquisition failures: schema mismatch, encoding problems, permissions, timeouts, versioning, drivers, corrupted files, and runtime errors
  - Emerging tools: pandas, NumPy, scikit-learn, prompt engineering, hallucinations, RAG, human-in-the-loop review, virtual data warehouses, and RPA
- Recommended lab:
  - Ingest CSV, JSON, and XML into SQLite or Postgres
  - Pull data from a simple API
  - Diagnose one schema mismatch, one encoding problem, one permission problem, and one timeout problem
  - Compare ETL and ELT workflows with a simple transformation task
- Quiz impact:
  - This single chapter can close most of Domain 6 and also reinforce parts of `2.2` and `3.3`.

## Priority 2: Expand deployment and connectivity coverage in Chapter 11

- Target objectives: `2.1`, `2.2`, `2.3`, plus parts of `5.3`
- Primary file to expand: [Database_11_DesignDeployTest.ipynb](Database_11_DesignDeployTest.ipynb)
- Why here: Chapter 11 already owns design patterns, deployment models, and testing, so it is the right place to add planning and connectivity detail.
- Proposed additions:
  - Requirements gathering: gap analysis, resource projection, storage sizing, user counts, and user types
  - Service levels: SLA, KPI, escalation, and reporting basics
  - Deployment phases: installation, configuration, provisioning, upgrading, modifying, and importing
  - OLTP vs. OLAP as an explicit concept rather than an implied pattern difference
  - Connectivity architecture: client/server, DNS, static vs. dynamic IP, ports, protocols, load balancing, perimeter network design, and multizone thinking
  - Documentation set: SOPs, maintenance docs, and compliance-oriented design records
- Recommended lab:
  - Present three deployment scenarios and ask students to choose architecture, service model, documentation artifacts, and connectivity plan.
- Outcome improvement:
  - This closes the biggest deployment gaps without breaking the current narrative flow.

## Priority 3: Expand monitoring, maintenance, and operational administration in Chapter 8

- Target objectives: `3.1`, `3.2`, `3.3`
- Primary file to expand: [Database_08_IndexesTransactions.ipynb](Database_08_IndexesTransactions.ipynb)
- Why here: Chapter 8 already handles performance, logs, health checks, and transaction behavior, so it is the natural operational chapter.
- Proposed additions:
  - Alerts and notifications: storage limits, backup alerts, job success/failure, and failed connection tracking
  - Baselines and trend reporting
  - Patch management and integrity checks
  - Change management: release schedules, approvals, refreshes, and version control expectations
  - CI/CD for database changes at a beginner-friendly level
  - Advanced data tasks: create statistics, computed columns, and isolation levels
- Recommended lab:
  - Give students a mock DBA runbook and ask them to investigate slow queries, a storage alert, and a failed job.
- Outcome improvement:
  - This turns Chapter 8 from performance-focused to operations-ready.

## Priority 4: Close advanced security and identity gaps in Chapters 9 and 10

- Target objectives: `4.1`, `4.2`, `4.3`, `4.4`
- Primary files to expand:
  - [Database_09_PokemonAndPostgres.ipynb](Database_09_PokemonAndPostgres.ipynb)
  - [Database_10_DatabaseSecurity.ipynb](Database_10_DatabaseSecurity.ipynb)
- Why here: Chapter 9 already handles DBMS users and roles, while Chapter 10 owns security, governance, and defensive design.
- Proposed Chapter 10 additions:
  - BYOK and KYOK
  - Confidential computing
  - Data sovereignty and data residency
  - PCI DSS as a contrast with GDPR and PHI-driven compliance
  - Zero Trust and attack surface management
  - Data poisoning and remediation workflows
  - SSL certificate basics in database communication
  - OAuth, OpenID Connect, IAM, federated identity, and Kerberos as concept-level coverage
- Proposed Chapter 9 additions:
  - A short implementation bridge from roles and privileges to enterprise identity integration
- Recommended lab:
  - Map a hospital or finance scenario to RBAC, ABAC, MFA, SSO, and compliance controls.
- Outcome improvement:
  - This raises security from strong partial alignment to near-complete alignment.

## Priority 5: Patch the remaining fundamentals gaps in Chapters 1 and 6

- Target objectives: `1.1`, `1.3`, `1.4`
- Primary files to expand:
  - [Database_01_StarShipSQL.ipynb](Database_01_StarShipSQL.ipynb)
  - [Database_06_WritingData.ipynb](Database_06_WritingData.ipynb)
- Why here: These are concept-adjacent gaps, not missing domains.
- Proposed Chapter 1 additions:
  - Key-value, vector, time-series, and object-oriented databases
  - Structured, semistructured, and unstructured data
- Proposed Chapter 6 additions:
  - Client-side vs. server-side scripting
  - PowerShell, Python, Unix shell, and Perl comparison at a survey level
  - IDE scripting vs. command-line scripting
  - ORM-generated SQL inspection and performance impact
- Recommended lab:
  - Show one inefficient ORM-style query and have students compare it with a hand-written alternative.
- Outcome improvement:
  - This finishes the remaining foundational gaps without requiring a new chapter.

## Lowest-Friction Insertion Map

- [Database_01_StarShipSQL.ipynb](Database_01_StarShipSQL.ipynb): add missing database types and data-shape taxonomy
- [Database_04_AdvancedSelect.ipynb](Database_04_AdvancedSelect.ipynb): add a short backup/DR terminology bridge for snapshots, restore points, failback, and fault-tolerance wording
- [Database_06_WritingData.ipynb](Database_06_WritingData.ipynb): add scripting/runtime comparison and ORM impact section
- [Database_08_IndexesTransactions.ipynb](Database_08_IndexesTransactions.ipynb): add maintenance operations and monitoring workflow content
- [Database_09_PokemonAndPostgres.ipynb](Database_09_PokemonAndPostgres.ipynb): add enterprise identity bridge content
- [Database_10_DatabaseSecurity.ipynb](Database_10_DatabaseSecurity.ipynb): add advanced security, governance, and identity topics
- [Database_11_DesignDeployTest.ipynb](Database_11_DesignDeployTest.ipynb): add planning, OLTP/OLAP, connectivity, and documentation depth
- New chapter recommended: `Database_13_DataIntegration.ipynb`

## Suggested Rollout Order

### Phase A: Quick alignment pass inside existing chapters

- Update Chapters 1, 4, 6, 8, 10, and 11
- Refresh learning outcomes after each chapter update
- Add glossary terms for the new exam vocabulary
- Outcome: most partial objectives become stronger, even before a new chapter is added

### Phase B: Add the new Data Integration chapter

- Build `Database_13_DataIntegration.ipynb`
- Add at least one hands-on ingestion lab and one troubleshooting lab
- Outcome: closes the largest structural gap in the current book

### Phase C: Refresh assessments and tracking

- Update the quiz authoring plan so every `Met` objective has a question pool
- Re-run this tracker and move statuses from `Partial` to `Met` where justified
- Outcome: certification alignment, learning outcomes, and quizzes stay synchronized

## Minimum Viable Completion Definition

The book is ready for objective-level quiz alignment when all of the following are true:

- No objective remains `Not Met`
- Domain 6 has a dedicated instructional path and lab support
- Chapters 8, 10, and 11 contain the missing exam vocabulary now absent from the current book
- Learning outcomes are refreshed after the new content lands
- Quiz pools are written only after the tracker is rerun against the revised notebooks