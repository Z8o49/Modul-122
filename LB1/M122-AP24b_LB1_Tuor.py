import webbrowser
import argparse
import urllib.parse
import sqlite3
from datetime import datetime
 
def open_google_search(query):
    query_encoded = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={query_encoded}&oq={query_encoded}"
    print(f"Generierte URL: {url}")
    try:
        webbrowser.open(url)
        print(f"Öffne Google-Suche für: {query}")
    except Exception as e:
        print(f"Fehler beim Öffnen des Browsers: {e}")
    save_to_db(query)
 
def save_to_db(query):
    conn = sqlite3.connect("search_queries.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            date TEXT
        )
    """)
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO search_queries (query, date) VALUES (?, ?)", (query, current_date))
    conn.commit()
    conn.close()
 
def main():
    parser = argparse.ArgumentParser(description="Öffnet eine Google-Suche für den angegebenen Begriff")
    parser.add_argument("query", type=str, help="Suchbegriff")
    args = parser.parse_args()
    open_google_search(args.query)
 
if __name__ == "__main__":
    main()