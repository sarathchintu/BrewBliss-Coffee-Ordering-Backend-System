☕ BrewBliss – Coffee Ordering Backend System

A terminal-based backend coffee ordering system built using Python and Oracle 11g.

This project demonstrates database schema design, relational integrity, transaction handling, and backend logic implementation without a frontend interface.

🚀 Tech Stack
Python 3

Oracle 11g

cx_Oracle / oracledb

SQL (DDL, DML, Sequences, Constraints)

🗄 Database Design

Tables

Users

Categories

Products

Orders

Order_Items

Payments

Key Highlights

Foreign Key Constraints

Sequence-Based Alphanumeric IDs (C1, O1, P1, OI1)

Relational Integrity

Transaction Management

🔐 Features

👤 User Module

User Registration

Login Authentication

Address Storage

🛠 Admin Module

Add Products

Delete Products

Manage Categories

🛒 Order Module

Add Multiple Items to Cart

Place Orders

Payment Simulation

OTP Generation

Automatic ID Generation

Order & Payment Recording

🧪 Testing & Validation

Performed 10–15 structured test runs covering:

New user creation

Multi-item order placement

Data insertion via Python

Foreign key validation

Payment recording consistency

Data verification using SELECT queries

📂 Project Structure

BrewBliss/

├── db_connection.py

├── table_creation.sql

├── sequences.sql

├── index.py

├── login.py

├── manager.py

├── user_panel.py

├── otp_generator.py

└── README.md

▶ How to Run

Execute table_creation.sql

Execute sequences.sql

Update DB credentials in db_connection.py

Run:

python index.py

📈 Version 2 Improvements (Planned)

Password Hashing

Order Status Lifecycle

Stock Management

Error Logging

REST API Version

🧠 Concepts Demonstrated

Relational Database Design

Foreign Keys & Constraints

Oracle Sequences

Python-Oracle Integration

Modular Backend Architecture

Transaction Control (Commit / Rollback)

👨‍💻 Author

SARATH CHANDRA

Aspiring Software Developer
