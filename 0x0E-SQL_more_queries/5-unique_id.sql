--  creates a table called unique_id in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 NOT NULL, name VARCHAR(256), UNIQUE (id));
