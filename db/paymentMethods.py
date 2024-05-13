class PaymentMethods():
    def __init__(self, db):
        self.table = 'PaymentMethods'
        self.db = db.db

    def getAll(self):
        cursor = self.db.cursor()
        cursor.execute(f'''SELECT p_type FROM {self.table}''')

        return cursor.fetchall()
    
    def getByType(self, type):
        cursor = self.db.cursor()
        cursor.execute(f'''SELECT * FROM {self.table} WHERE p_type='{type}';''')

        return cursor.fetchall()