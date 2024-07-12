-- Create the messages table if it does not already exist
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    content TEXT
);

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- Create the posts table with a foreign key to the users table
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create the comments table with foreign keys to the posts and users tables
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY,
    content TEXT,
    post_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

