# Database: Important Code and Concepts

The following is a curated list of important defintions and code techniques covered during this class. A quizlet deck covering this material lives here: https://quizlet.com/857775002/database-final-review-flash-cards/?i=psvlh&x=1jqt

|Terms | Definition |
|-------|-----------|
| ACID | An acronym standing for Atomicity, Consistency, Isolation, and Durability. It's a set of properties that guarantee database transactions are processed reliably even in the event of errors or system failures. |
| Aggregate Function | A type of function in SQL that processes a set of values and returns a single value summarizing the input. Examples include SUM, AVG, MAX, MIN, and COUNT. |
| Application Programming Interface (API) | A set of rules and protocols that specify how software components should interact. In the context of data collection APIs can be used to retrieve data. |
| Atomic Value | This is a value that can't be broken down any further. For example, a student's full name could be broken down into first and last name, so it's not atomic. But a student's first name alone is atomic, because it can't be broken down without losing its meaning. |
| Atomicity | The property that ensures a transaction is treated as a single, indivisible unit. Either all the operations in the transaction are executed, or none are, ensuring there's no partial data. |
| Attribute | A column in a table. Each attribute represents a specific piece of data, like a name or date, associated with the object modeled by the table. |
| Audit Log | A record keeping track of who accessed a system and what operations they performed. |
| BEGIN; | SQL code to start a new transaction |
| Box Plot | A graphical representation that shows the distribution of data based on a five-number summary: minimum, first quartile, median, third quartile, and maximum. It is useful for identifying outliers and data spread. |
| CHAR(n) | A data type used for character strings of a fixed length, with the number inside the parentheses specifying the exact length of characters the field can hold. |
| Commit (transaction) | The action of making all data modifications performed by a transaction permanent, marking the successful end of a transaction. |
| COMMIT; | SQL code to commit the current transaction, saving all changes made within it |
| Consistency | The principle that all data in a database must meet specified integrity constraints to maintain data accuracy and to prevent data corruption or duplication. |
| Constraint | A rule applied to a column or set of columns in a database table that restricts the data that can be stored in those columns. |
| CREATE INDEX idx_order_details_quantity ON order_details(quantity); | SQL code to create an index named idx_order_details_quantity on the quantity field of order_details table |
| CREATE TABLE Houses (HouseID INT PRIMARY KEY) | Creates a new table called Houses with a single column, HouseID, which is an integer and the primary key of the table. |
| CREATE VIEW total_ordered_products AS SELECT product_id, SUM(quantity) AS total_quantity FROM order_details GROUP BY product_id; | SQL code to create a view named total_ordered_products to see total quantity for each product |
| Data | Raw, unprocessed facts or figures without context, like a list of random numbers. |
| Data Anomaly | An unusual or unexpected piece of data that deviates from the norm or pattern in a dataset, like having a customer's name spelled in two different ways in a datase. |
| Data Classification | The process of organizing data into categories that make it easy to retrieve, sort, and store for effective use. |
| Data Definition Language (DDL) | A subset of SQL used to define and manage database structures, including creating, altering, and dropping tables. |
| Data dictionary | A centralized repository of information about a database such as meaning, relationships to other data, origin, usage, and format. |
| Data Frame | A table-like data structure used in programming for organizing data into rows and columns, making it easier to manipulate and analyze large datasets. |
| Data Independence | The ability to modify the schema of a database without affecting the application layer that uses it, like adding a new table or column without breaking the existing application. |
| Data Integrity | The accuracy, consistency, and reliability of data over its lifecycle, like ensuring a customer's contact information is correct and up-to-date. |
| Data Loss Prevention | Strategies and solutions used to ensure that sensitive data is not lost, misused, or accessed by unauthorized users. |
| Data Manipulation Language (DML) | A subset of SQL used to retrieve, insert, modify, and delete data in a database. |
| Data Masking | The technique of hiding original data with modified content (characters or other data) to protect sensitive information. |
| Data migration | The process of transferring data between storage types, formats, or computer systems, often undertaken when organizations change systems or upgrade hardware. |
| Data Redundancy | The duplication of data in a database or other storage system, like storing the same customer's address in multiple tables. |
| Data Retention Policy | Guidelines established by an organization to manage the preservation and disposal of its data. |
| Data Warehouse | A large system for storing and managing data from different sources, used for analysis and reporting. |
| Database | A structured set of data, stored in a system, that allows for easy access, manipulation, and retrieval, akin to a library with an index system. |
| Database Audit | A process of reviewing operations performed on a database for security, compliance or optimization purposes. It can help detect anomalies and potential security breaches. |
| Database lifecycle | The stages through which a database system passes, from initial requirements gathering to design, implementation, maintenance, and retirement. |
| Database Logs | Files that keep a record of the activities or events that occur in a database, like transactions, for later analysis. For instance, an administrator can check these logs to see when certain changes were made to the database. |
| Database Monitoring | The continuous process of observing a database's operations to ensure its optimal performance and security. |
| Database Normalization Form | Rules used to design tables where the data dependencies are logical, avoiding redundancy and anomalies. |
| Database Reporting | Creating summaries or detailed reports from database data, often for analysis or decision-making purposes. |
| DateOfBirth DATE NOT NULL | Adds a column to the Houses table called DateOfBirth, which is a date and cannot be null. |
| Deadlock | A situation in computing where two processes are unable to proceed because each is waiting for the other. |
| Default value (SQL) | A preset value that a database automatically assigns to a column if no value is specified by the user. |
| Deletion Anomaly | This is when removing data unintentionally deletes other useful data. For example, if you delete a 'Professor' record because they left Hogwarts, but it also removes all the courses they taught from the database. |
| Denial of Service (DoS) | A cyber attack where the perpetrator seeks to make a network resource unavailable to its intended users by temporarily or indefinitely disrupting services. For instance, flooding a company's server with requests, making it inaccessible to employees. |
| Denormalization | A process in databases where data from multiple tables is combined into one to improve read performance, at the cost of making updates more complex. |
| Design documentation | A detailed written account of the technical specifications and the design decisions made in the development of a system. |
| Dictionary Attack | A method of breaking into a password-protected computer or server by systematically entering every word in a dictionary as a password. A classic approach to gain unauthorized access to a system. |
| Differential Backup | A backup that copies all the data changed since the last full backup, allowing for quicker restore times than a full backup. |
| Dimension Table | Tables in a data warehouse that provide descriptive information about the facts in the fact table, like details about customers, products, or time periods. |
| Disjoint (Subtype) | This is when a single item can belong to only one subtype at a time. For example, a 'User' can be either a 'Student', 'Faculty', or 'Administrator', but not more than one at the same time. |
| DROP INDEX idx_order_details_quantity; | SQL code to get rid of the index idx_order_details_quantity |
| DROP TABLE IF EXISTS Houses CASCADE; | Drops the table Houses if it exists, and also drops any tables that reference it. |
| Durability | The property that ensures once a transaction has been committed, it remains so, even in the event of power loss, crashes, or other system failures. |
| Encryption | The process of converting data into a code to prevent unauthorized access. For instance, a company might encrypt sensitive customer data to prevent it from being read if intercepted during a transfer. |
| Entity-Relationship Diagram | A visual representation of different entities within a database and the relationships between them. Entities are typically depicted as rectangles, with relationships illustrated as lines or arrows connecting these rectangles. |
| EXCEPT | An SQL operation that returns the records present in the first SELECT statement but not in the second one. Both SELECT statements must have the same number of columns with compatible data types. |
| Fact Table | A table in a data warehouse that stores the main pieces of information, like sales or transactions, and is linked to other tables that provide additional details. |
| First Normal Form (1NF) | A database normalization form that eliminates duplicate columns from the same table and identifies each piece of data by a unique key. |
| Foreign Key | A field in one table that uniquely identifies a row of another table, establishing a link between them. |
| FOREIGN KEY (StudentID) REFERENCES Students(StudentID) | Creates a foreign key constraint on the StudentID column in the Houses table, which references the StudentID column in the Students table. This means that every StudentID value in the Houses table must exist in the Students table. |
| Full Backup | A complete copy of all data in a system at a specific point in time, used for data restoration. |
| Histogram | A graphical representation that shows the frequency distribution of a dataset. It groups data into bins and displays the number of data points that fall into each bin. |
| HousePoints INT CHECK (HousePoints >= 0) | Adds a column to the Houses table called HousePoints, which is an integer and must be greater than or equal to 0. |
| Identity and Access Management (IAM) | A framework of policies and technologies ensuring that the right individuals access the appropriate resources in an organization. |
| Index | A database object that improves the speed of data retrieval operations on a database table by providing quick random lookups and efficient access of ordered records. |
| Index scan | A method of data retrieval that uses an index to avoid scanning the entire database, which makes it faster than a sequential scan. |
| Information | Data that has been processed or organized in a way that allows it to be useful or meaningful, such as a table showing the average temperature of each month. |
| INNER (NATURAL) JOIN | A type of join operation in SQL that returns rows where there is a match in both tables being joined. If specified as NATURAL, it automatically matches columns between the tables with the same names. |
| Insertion Anomaly | This is when you can't add data to the database due to missing additional data. For example, you can't add a new course unless you also have a professor assigned to it. |
| Integrity | A state of maintaining and assuring the accuracy and consistency of data in a database. It is usually enforced with a set of rules (constraints) on a database. |
| INTERSECT | An SQL operation that returns the common records between two SELECT statements. Both SELECT statements need to have the same number of columns with compatible data types. |
| JSON | JavaScript Object Notation, a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. |
| JSON: Array | An ordered list of zero or more values, enclosed in square brackets, within a JSON document. |
| JSON: Key | A string that identifies a corresponding value in a JSON object. |
| JSON: Object | A collection of key-value pairs enclosed in curly braces, serving as a data structure in JSON. |
| JSON: Value | The actual data assigned to a key in a JSON object. This could be a number, string, boolean, array, or another object. |
| Junction (Join) Table | A table in a database used to resolve many-to-many relationships between two other tables. It typically contains foreign keys that correspond to the primary keys of the related tables. |
| Knowledge | Information that has been processed or interpreted, often involving relationships among multiple pieces of information, like knowing that sales increase when the temperature is warm based on past sales data and weather reports. |
| LEFT (OUTER) JOIN | A join operation that returns all the rows from the left table and matched rows from the right table. If there is no match, the result from the right side will contain NULL values. |
| Malware | Any software intentionally designed to cause damage to a computer, server, client, or computer network. For instance, a malicious program sent via email that infects a system upon opening. |
| Mandatory (Subtype) | This is when every instance of a supertype must be an instance of some subtype. For example, if 'User' is a supertype, then every user must be classified as either a 'Student', 'Faculty', or 'Administrator'. |
| Many-to-Many | A type of relationship where multiple records in a table can be associated with multiple records in another table. |
| Multi-Valued Attribute | This is an attribute that can have more than one value. For example, a student could be part of multiple clubs, like 'Quidditch Club' and 'Potion Club'. |
| NoSQL Database | A database that provides storage and retrieval operations not based on tabular structures typical of relational databases. Often used for unstructured or semi-structured data. |
| NULL | A special marker used in SQL to indicate that a data value does not exist in the database. For example, a missing salary entry for an employee in a company's database would be marked as NULL. |
| Object-Relational mapping | A technique that converts data between incompatible type systems in object-oriented programming languages and relational databases. |
| One-to-Many | A type of relationship where one record in a table can be linked to multiple records in another table. |
| One-to-One | A type of relationship where a single record in one table is linked to a single record in another table. |
| Optional (Subtype) | This is when an instance of a supertype may or may not be an instance of any subtype. For example, if 'Club Member' is a supertype, a student might not be a member of any specific club subtype like 'Quidditch Club' or 'Potion Club'. |
| Overlapping (Subtype) | This is when a single item can belong to more than one subtype at the same time. For example, Harry Potter is both a 'Quidditch Player' and a 'Book Club Member'. |
| Pandas | A software library in Python used for data manipulation and analysis, providing data structures and operations for manipulating numerical tables and time series. |
| Patch | A piece of code designed to improve a system or correct an issue within a software program. |
| Personally Identifiable Information (PII) | Information that can be used on its own or with other data to identify a single person. |
| PL/SQL | A procedural language extension for SQL, adding capabilities for loops, conditions, and variables to SQL's set-based operations. |
| Postgres: -> | An operator in PostgreSQL used to get a JSON object field by key, returning it as a JSON object. |
| Postgres: ->> | An operator in PostgreSQL used to get a JSON object field by key and return it as text. |
| Postgres: @> | An operator in PostgreSQL used for containment tests within JSONB columns, checking whether the left JSONB object contains the right JSONB or JSON value. |
| Postgres: JSONB | A binary JSON data type in PostgreSQL, offering indexing capabilities. Unlike regular JSON, it is not stored as a simple text string and allows for more efficient querying. |
| Primary Key | A field in a table which is used to uniquely identify each record in that table. |
| PRIMARY KEY (StudentID, Course) | Sets the primary key of the Houses table to be the combination of the StudentID and Course columns. |
| Principle of Least Privilege | A computer security concept in which a user is given the minimum levels of access necessary to complete his/her job functions. For example, a customer service representative might only have access to a customer's contact info and purchase history, but not their payment details. |
| Public databases | Databases that are freely available to the public for use and distribution. They can be on various topics like health, science, literature, etc. |
| ransitive Dependency | This is when one piece of information relies on another through a third piece of information. For example, a 'Course ID' could lead you to a 'Professor ID', which could lead you to a 'Department'. |
| Recursive Relationship | A relationship where an entity is related to itself; instances of the same entity are associated with each other. This often models hierarchical structures or mutual relationships. |
| Relational Database | A type of database that organizes data into tables which can be linked to each other based on relationships, for example, a database with separate tables for 'customers' and 'orders' that are linked by 'customer_id'. |
| Relationship Cardinality | The numerical mapping between entities (or tables). It shows the number of instances of one entity that can, or must, be associated with each instance of another entity. |
| Rigid Schema | A strict set of rules about how data must be organized. Changing the rules can be hard and time-consuming. Typical of relational databases. |
| Role-based Access Control | A method of regulating access to computer resources based on the roles of individual users within an enterprise. For instance, a company could ensure that only HR staff can access employee records. |
| Rollback (transaction) | The process of undoing the changes made by an uncommitted transaction, returning the database to its previous state. |
| ROLLBACK; | SQL code to rollback the current transaction, undoing all changes made within it |
| Scatter Plot | A type of graph used to display values for two variables for a set of data. It shows data points on a two-dimensional grid, helping to identify relationships between variables. |
| Second Normal Form (2NF) | A database normalization form that requires a table to be in First Normal Form and also requires that all non-key attributes be fully dependent on the primary key. |
| SELECT * FROM Books ORDER BY Title ASC; | SQL: Select all columns from the Books table, ordered by Title in ascending order |
| SELECT * FROM Books WHERE Author_ID = 3; | SQL: Select all columns from the Books table where Author_ID is 3 |
| SELECT * FROM Books WHERE Num_Pages < 200; | SQL: Select all columns from the Books table where Num_Pages is less than 200 |
| SELECT * FROM Books WHERE Num_Pages BETWEEN 200 AND 300; | SQL: Select all columns from the Books table where Num_Pages is between 200 and 300 |
| SELECT * FROM Books WHERE Title = 'The Abominable Teapot of Terror'; | SQL: Select all columns from the Books table where Title is 'The Abominable Teapot of Terror' |
| SELECT * FROM Books WHERE Title LIKE 'The%'; | SQL: Select all columns from the Books table where Title starts with 'The' |
| SELECT * FROM monsters WHERE data->>'name' LIKE '%Dragon%'; | Postgres SQL/JSON query retrieves all rows from the monsters table where the name key in the data column has 'Dragon' anywhere. |
| SELECT 50 / 5 AS division_result; | SQL code to divide 50 by 5, and call the result "division_result." |
| SELECT author, COUNT(*) AS Books_Per_Author FROM books GROUP BY author | SQL code to retrieve a list of authors and the numbers of books they've written |
| SELECT author, COUNT(*) AS Books_Per_Author FROM books GROUP BY author HAVING Books_Per_Author > 5 | SQL code to get group books by authors, count the number of books per author, only include authors with more than 5 books |
| SELECT AVG((data->>'XP')::numeric) FROM monsters; | Postgres SQL/JSON query calculates the average value of the XP key in the data column for all rows in the monsters table. |
| SELECT AVG(rating) FROM books | SQL code to get the average rating of all books |
| SELECT COUNT(*) FROM books | SQL code to get the number of books |
| SELECT COUNT(*) FROM monsters WHERE data->>'Challenge' = '5'; | Postgres SQL/JSON query counts the number of rows in the monsters table where the Challenge key in the data column is equal to '5'. |
| SELECT COUNT(DISTINCT authors) FROM books | SQL code to find the number of unique authors in books table |
| SELECT data->'Armor Class' AS armor_class FROM monsters WHERE data->>'name' = 'Ogre'; | Postgres SQL/JSON query selects the Armor Class key from the data column in the monsters table for records where the name is 'Ogre'. |
| SELECT data->>'Speed' FROM monsters ORDER BY data->>'Speed' DESC LIMIT 5; | Postgres SQL/JSON query gets the top 5 monster speeds (Speed key) from the data column in the monsters table, ordered in descending order. |
| SELECT DISTINCT(M.name) FROM Movie M JOIN Oscar O ON M.id = O.movie_id WHERE M.genre LIKE '%A%'; | SQL code to finds all 'Action' genre movies that have received an Oscar nomination. |
| SELECT DISTINCT(P.name) FROM Person P JOIN Director D ON P.id = D.director_id JOIN Movie M ON D.movie_id = M.id WHERE M.name LIKE '%Spider-Man%'; | SQL code to find the director(s) of "Spider-Man" movies. |
| SELECT M.name FROM Movie M JOIN Actor A ON M.id = A.movie_id JOIN Person P ON A.actor_id = P.id WHERE P.name LIKE 'Marlon Brando'; | SQL code to find all movies where Marlon Brando has starred. |
| SELECT M.name FROM Movie M JOIN Director D ON M.id = D.movie_id JOIN Person P ON D.director_id = P.id WHERE P.name LIKE 'Steven Spielberg'; | SQL code to find all movies directed by Steven Spielberg. |
| SELECT M.name FROM Movie M JOIN Oscar O ON M.id = O.movie_id WHERE O.type = "BEST-PICTURE" AND M.name LIKE '%War%'; | SQL code to find all movies nominated for Best-picture Oscars with "War" in the title. |
| SELECT MAX(numRatings) FROM books | SQL code to get the maximum number of ratings a book has received |
| SELECT MIN(numRatings) FROM books | SQL code to get the minimum number of ratings a book has received |
| SELECT Name, Birthdate FROM Authors; | SQL: Select the Name and Birthdate columns from the Authors table |
| SELECT p.name FROM Person p INNER JOIN Actor a ON p.id = a.actor_id INTERSECT SELECT p.name FROM Person p INNER JOIN Director d ON p.id = d.director_id; |   |
| SELECT P.name FROM Person P JOIN Actor A ON P.id = A.actor_id JOIN Movie M ON A.movie_id = M.id WHERE M.name LIKE '%Batman%'; | SQL code to find all actors who starred in any movie with "Batman" in the title. |
| SELECT ROUND(42.789); | SQL code to round 42.789. |
| SELECT SUM(pages) FROM books | SQL code to get the total number of pages of all books |
| SELECT TRUNC(42.789); | SQL code to truncate 42.789. |
| Semi-Structured Data | Data that does not conform to the strict structure of data models like in relational databases, but still has some level of organization which could include tags, hierarchies, or other markers. |
| Sequential scan | A method of data retrieval that scans each row in the database table in a sequential order. This method is typically slow, especially for large tables. |
| Snowflake Schema | A more complex database structure where the dimension tables of a star schema are further divided into additional tables, reducing data redundancy but increasing complexity. |
| SQL Injection Attack | A code injection technique that attackers use to insert malicious SQL code into a query. For example, adding 'DROP TABLE Customers;' into a user login field in a web form. |
| Star Schema | A database structure that organizes data into one central table linked to several related tables. It simplifies complex data relationships, making it easier to analyze data. |
| Stress testing | A form of testing that evaluates a system's stability and reliability under extreme conditions or heavy load. |
| Structured Data | Data that is organized and formatted in a specific way, often into rows and columns like a table, making it easier to understand and process. |
| Structured Query Language (SQL) | A standardized programming language specifically used for managing and manipulating relational databases, like retrieving data from a table or inserting a new record into a database. |
| Subquery | A query that is nested inside another query in SQL. It is used to retrieve data that will be used in the main query as a condition, enhancing the flexibility of SQL queries. |
| Table (Relation) | In the context of databases, it is a set of data elements organized using a model of vertical columns (which are identified by their name) and horizontal rows. |
| Third Normal Form (3NF) | A database normalization form that requires a table to be in Second Normal Form and also requires that all columns be directly dependent on the primary key. |
| Transaction | A sequence of one or more database operations (such as reading, updating, inserting, or deleting data) that are treated as a unit. Either all the operations are executed (committed), or none of them are (rolled back), ensuring data consistency. |
| Trigger | A procedural code that is automatically executed in response to certain events on a particular table or view in a database. |
| UNION | An SQL operation that combines rows from two or more SELECT statements into a single result, eliminating duplicate entries. All SELECT statements within the UNION must have the same number of columns with compatible data types. |
| Unstructured Data | Data that lacks a specific format or organization, such as a blog post or an unlabeled photograph, which requires effort to process and understand. |
| Update Anomaly | This is when changing data (like updating an address) in one part of the database doesn't automatically update the same data elsewhere. This can lead to inconsistencies. For example, if a student moves and the address is updated in the 'Student' table but not in the 'Guardian' table. |
| VARCHAR(n) | A data type used for variable-length strings where the number inside the parentheses specifies the maximum number of characters the field can hold. |
| View | A virtual table based on the result-set of an SQL statement. It contains rows and columns, just like a real table, and can be queried like a regular table but does not store data itself. |
| Web scraping | A method of extracting data from websites by downloading and analyzing the HTML code from the webpage. |
| YearLevel INT CHECK (YearLevel BETWEEN 1 AND 7) | Adds a column to the Houses table called YearLevel, which is an integer and must be between 1 and 7. |
|  |  |
