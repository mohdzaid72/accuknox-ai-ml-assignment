import pandas as pd
import sqlite3


CSV_FILE = "users.csv"
DB_FILE = "users.db"


def create_database(connection):

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    connection.commit()


def import_users(connection):
    df = pd.read_csv(CSV_FILE)

    
    df = df.dropna(subset=["name", "email"])
    df["name"] = df["name"].astype(str).str.strip()
    df["email"] = df["email"].astype(str).str.strip()


    

    cursor = connection.cursor()

    for _, row in df.iterrows():

        try:
            cursor.execute("""
                INSERT INTO users (name, email)
                VALUES (?, ?)
            """, (row["name"], row["email"]))

        except sqlite3.IntegrityError:
            print(f"Skipping duplicate email: {row['email']}")

    connection.commit()


def display_users(connection):
    query = """
        SELECT id, name, email
        FROM users
        ORDER BY id
    """

    df = pd.read_sql_query(query, connection)

    print("\nUsers stored in database:")
    print("-" * 50)

    print(df.to_string(index=False))


def main():

    connection = sqlite3.connect(DB_FILE)

    try:
        create_database(connection)

        import_users(connection)

        display_users(connection)

    finally:
        connection.close()


if __name__ == "__main__":
    main()
