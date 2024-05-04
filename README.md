AirBnB Clone with MySQL

This project is an AirBnB clone implemented using MySQL as the database management system. It provides a simplified version of AirBnB's functionality, allowing users to create listings, make bookings, and leave reviews.

## Prerequisites

- MySQL installed on your system.
- Basic understanding of SQL queries.

## Setting Up the Database

1. **Create a Database**: Start by creating a new database in MySQL. You can use the MySQL command line or any GUI tool like phpMyAdmin.

   ```sql
   CREATE DATABASE airbnb_clone;
   ```

2. **Create Tables**: Define the tables needed for your AirBnB clone. These tables may include `users`, `listings`, `bookings`, `reviews`, etc. Below is an example of creating a `listings` table:

   ```sql
   CREATE TABLE listings (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       description TEXT,
       price DECIMAL(10, 2) NOT NULL,
       location VARCHAR(255) NOT NULL,
       host_id INT NOT NULL,
       FOREIGN KEY (host_id) REFERENCES users(id)
   );
   ```

   You can create similar tables for other entities like users, bookings, and reviews.

3. **Insert Sample Data (Optional)**: If you want to populate your database with sample data, you can use INSERT statements.

## CRUD Operations

Implement CRUD operations to interact with the database:

- **Create**: Insert new records into the tables.
- **Read**: Retrieve data from the tables.
- **Update**: Modify existing records.
- **Delete**: Remove records from the tables.

## Running Queries

You can execute SQL queries using MySQL command line or GUI tools. For example, to view all listings, run:

```sql
SELECT * FROM listings;
```

## Conclusion

This README provides a basic outline for setting up an AirBnB clone using MySQL.
