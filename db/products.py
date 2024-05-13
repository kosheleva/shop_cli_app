class Products():
    def __init__(self, db):
        self.table = 'Products'
        self.db = db.db
    
    def getAll(self):
        cursor = self.db.cursor()
        cursor.execute(f'''SELECT * FROM {self.table}''')

        return cursor.fetchall()
    
    def getAllByCategory(self, category):
        cursor = self.db.cursor()
        cursor.execute(f'''
            SELECT * FROM {self.table} p
            INNER JOIN Categories c 
            ON c.id=p.category_id AND c.title='{category}';
        ''')

        return cursor.fetchall()
    
    def getAllWithDiscounts(self):
        cursor = self.db.cursor()
        cursor.execute(f'''
            SELECT 
                p.code, 
                p.title, 
                p.price, 
                d.discount,
                p.price - ((p.price * d.discount) / 100) as final_price, 
                p.currency
            FROM {self.table} p
            INNER JOIN Discounts d ON p.id=d.product_id;
        ''')

        return cursor.fetchall()
        

    def getByTitle(self, title):
        cursor = self.db.cursor()
        cursor.execute(f'''SELECT * FROM {self.table} WHERE title='{title}';''')

        return cursor.fetchall()
    



    