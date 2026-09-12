import requests
import sqlite3

URL = "https://openlibrary.org/search.json?q=the+lord+of+the+rings&limit=5"

DATABASE = "books.db"


def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            author TEXT,
            publication_year INTEGER
        )
    """)


def fetch_books(url):
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data.get("docs", [])


def save_books(cursor, books):
    for book in books:
        title = book.get("title", "Unknown")

        authors = book.get("author_name", [])
        author = ", ".join(authors) if authors else "Unknown"

        publication_year = book.get("first_publish_year")

        cursor.execute("""
            INSERT OR IGNORE INTO books
            (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (title, author, publication_year))


def display_books(cursor):
    cursor.execute("""
        SELECT id, title, author, publication_year
        FROM books
    """)

    books = cursor.fetchall()

    for book in books:
        print("ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Publication Year:", book[3])
        print("-" * 50)


def main():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:
        create_table(cursor)
        books = fetch_books(URL)
        save_books(cursor, books)
        connection.commit()
        display_books(cursor)

    finally:
        connection.close()


if __name__ == "__main__":
    main()
