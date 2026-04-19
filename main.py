import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def add_user(self, name, age):
        self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def update_age(self, id, new_age):
        self.cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, id))
        self.conn.commit()

    def delete_user(self, id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
```

```python
# Test qilish uchun
db = Database('users.db')
db.add_user('Ali', 25)
db.add_user('Vali', 30)
print(db.get_all())  # [(1, 'Ali', 25), (2, 'Vali', 30)]
db.update_age(1, 26)
print(db.get_all())  # [(1, 'Ali', 26), (2, 'Vali', 30)]
db.delete_user(2)
print(db.get_all())  # [(1, 'Ali', 26)]
db.close()
