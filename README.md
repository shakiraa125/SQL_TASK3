**Name:SHAKIRA\
Company:CODETECH IT SOLUTION\
ID:CT12FDE\
Domain:SQL\
Duration:December 20th, 2024 to February 20th, 2025**\


## Database Backup and Recovery
________________________________________
Objective
The objective of this project is to demonstrate how to back up a MySQL database and restore it in case of failure using mysqldump for backup and MySQL CLI for restoration. The deliverables include the backup and restore scripts that can be executed in a Windows environment using Git Bash.
________________________________________
Tools and Technologies
•	Database: MySQL
•	Backup Utility: mysqldump
•	Scripting: Shell scripts (backup.sh, restore.sh)
•	Environment: Git Bash on Windows
________________________________________
Steps to Implement the Project
1. Backup Script
A shell script (backup.sh) was created to back up the database using mysqldump.
Script Content:
#!/bin/bash

# Variables
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_DIR="C:/DataEngineer/POSTGRESQL/BACKUP_DIR"
DB_NAME="TestDB"
USER="root"
PASSWORD="password"

# Create the backup directory if it does not exist
mkdir -p $BACKUP_DIR

# Perform the database backup
mysqldump -u $USER -p$PASSWORD $DB_NAME > $BACKUP_DIR/${DB_NAME}_$TIMESTAMP.sql

# Notify success
echo "Backup completed: $BACKUP_DIR/${DB_NAME}_$TIMESTAMP.sql"
Execution Steps:
1.	Open Git Bash.
2.	Navigate to the directory containing backup.sh:
cd /c/DataEngineer/POSTGRESQL
3.	Make the script executable:
chmod +x backup.sh
4.	Run the script:
./backup.sh
5.	Verify the backup file is created in the specified directory.
2. Restore Script
A shell script (restore.sh) was created to restore the database from a backup file.
Script Content:
#!/bin/bash

# Variables
BACKUP_FILE="C:/DataEngineer/POSTGRESQL/BACKUP_DIR/TestDB_2025-01-10_15-09-00.sql"
DB_NAME="TestDB"
USER="root"
PASSWORD="password"

# Confirm before proceeding
echo "You are about to restore the database $DB_NAME from the backup file $BACKUP_FILE."
read -p "Are you sure? (y/n): " CONFIRM

if [[ "$CONFIRM" != "y" ]]; then
  echo "Restore canceled."
  exit 1
fi
# Restore the database
mysql -u $USER -p$PASSWORD $DB_NAME < $BACKUP_FILE

# Notify success
echo "Database $DB_NAME restored successfully from $BACKUP_FILE."
Execution Steps:
1.	Open Git Bash.
2.	Navigate to the directory containing restore.sh:
cd /c/DataEngineer/POSTGRESQL
3.	Make the script executable:
chmod +x restore.sh
4.	Run the script:
./restore.sh
5.	Confirm the restoration process when prompted.
6.	Verify the restored database using MySQL Workbench or CLI.
________________________________________
Results
•	Backup files were successfully generated in the specified directory with timestamps.
•	The database was restored successfully using the backup files.
•	Both processes were automated using shell scripts, making it easy to replicate the steps.
________________________________________
Conclusion
This project demonstrates the importance of implementing regular database backups and reliable restoration mechanisms to ensure data integrity and availability in case of failures. The provided scripts offer a simple yet effective solution for database backup and recovery in a MySQL environment.
