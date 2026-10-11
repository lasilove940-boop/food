import sqlite3
from config import DATABASE


class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)

        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    time TEXT,
                    ingredients TEXT
                )
            ''')

    def add_recipe(self, name, time, ingredients):
        conn = sqlite3.connect(self.database)

        with conn:
            conn.execute('''
                INSERT INTO recipes (name, time, ingredients)
                VALUES (?, ?, ?)
            ''', (name, time, ingredients))

    def get_random_recipe(self):
        conn = sqlite3.connect(self.database)

        with conn:
            recipe = conn.execute('''
                SELECT name, time, ingredients
                FROM recipes
                ORDER BY RANDOM()
                LIMIT 1
            ''').fetchone()

        return recipe

    def get_recipe(self, name):
        conn = sqlite3.connect(self.database)

        with conn:
            recipe = conn.execute('''
                SELECT name, time, ingredients
                FROM recipes
                WHERE name = ?
            ''', (name,)).fetchone()

        return recipe