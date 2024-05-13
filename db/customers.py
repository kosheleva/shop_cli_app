
class Customers():
    def __init__(self, db):
        self.table = 'Customers'
        self.db = db.db

    def get(self, name, password):
        cursor = self.db.cursor()
        cursor.execute(f'''
            SELECT * FROM {self.table} WHERE name='{name}' AND password='{password}';
        ''')

        return cursor.fetchall()



