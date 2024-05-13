
class DeliveryMethods():
    def __init__(self, db):
        self.table = 'DeliveryMethods'
        self.db = db.db

    def getAll(self):
        cursor = self.db.cursor()
        cursor.execute(f'''SELECT d_type FROM {self.table}''')

        return cursor.fetchall()
    
    def getByType(self, type):
        cursor = self.db.cursor()
        cursor.execute(f'''SELECT * FROM {self.table} WHERE d_type='{type}';''')

        return cursor.fetchall()