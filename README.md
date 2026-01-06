# Disaster Relief Resource Allocation System
A web-based DBMS project built using Flask and MySQL to manage disaster relief operations efficiently. 
The system centralizes data related to relief centers, victims, supplies, and donations, and automates 
resource allocation with alerts and reports.
## Database (MySQL)
The MySQL database design and implementation for this project are provided in the file:
- **MySQL.pdf** — contains table structures, triggers, and stored procedures used in the project.
The database logic is implemented using:
- Normalized relational tables
- Triggers for low-inventory alerts
- Stored procedures for automated resource allocation and reporting
## Tech Stack
- Frontend: HTML, CSS
- Backend: Python (Flask)
- Database: MySQL
## Features
- Centralized resource management
- Automated demand–supply allocation
- Low inventory alerts
- Disaster report generation
## Database Setup
1. Create a MySQL database named `disaster_db`.
2. Refer to **MySQL.pdf** for:
   - Table creation queries
   - Triggers
   - Stored procedures
3. Execute the SQL queries in MySQL Workbench or phpMyAdmin.
4. Update database credentials in `database.py`.

