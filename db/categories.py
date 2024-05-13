
class Categories():
    def __init__(self, db):
        self.table = 'Categories'
        self.db = db.db

    def getAll(self):
        cursor = self.db.cursor()
        cursor.execute(f'''SELECT * FROM {self.table}''')

        return cursor.fetchall()
