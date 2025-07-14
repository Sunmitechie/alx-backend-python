# Python Generators - Seed Script

This directory contains a Python script for seeding a MySQL database with user data from a CSV file.

## Files

- `seed.py`: Script to create a database, table, and insert user data from a CSV file.
- `README.md`: Project documentation.

## Usage

1. **Configure MySQL Credentials**  
   Edit `seed.py` and update the `user` and `password` fields to match your MySQL setup.

2. **Prepare CSV File**  
   Ensure you have a CSV file with columns: `user_id`, `name`, `email`, `age`.

3. **Run the Script**  
   ```sh
   python3 seed.py