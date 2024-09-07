import sqlite3

conn = sqlite3.connect('local_database.db')
cursor = conn.cursor()

def check_if_user_exists(cookies):
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE cookies=?)", (str(cookies),))
    result = cursor.fetchone()[0]
    return result == 1

def remove_user_table():
    # Option 1: Delete all rows
    cursor.execute("DELETE FROM users")
    conn.commit()

def add_user_table(headers, cookies):
    exists = check_if_user_exists(cookies)

    if exists:
        print("user exists")
    else:
        remove_user_table()
        # Insert data into the table
        cursor.execute(f'''
        INSERT INTO users (headers, cookies)
        VALUES (?, ?)
        ''', (str(headers), str(cookies)))
    print()
    conn.commit()

    # Fetch the result

def check_table_exists(table_name):
    # Query to check if the table exists
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))

    # Fetch the result
    table_exists = cursor.fetchone() is not None
    return table_exists

def set_user(user):
    # Execute a query to select data
    cursor.execute("SELECT * FROM users")
    # Fetch the first row of the result set
    first_row = cursor.fetchone()
    if first_row:
        headers_string = first_row[1]
        cookies_string = first_row[2]
        headers_dict = eval(headers_string)
        cookies_dict = eval(cookies_string)
        user.headers = headers_dict
        user.cookies = cookies_dict
    # Commit the changes
    conn.commit()

def db_start(user):

    users_exists = check_table_exists('users')
    print("users_exists", users_exists)
    if users_exists == False:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                headers TEXT NOT NULL UNIQUE,
                cookies TEXT NOT NULL UNIQUE
            );
        ''')
        conn.commit()  # Don't forget to commit the transaction
    else:
        set_user(user)
        if user.cookies:
            return 200
        else:
            return 500

