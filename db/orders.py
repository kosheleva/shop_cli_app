
class Orders():
    def __init__(self, db):
        self.table = 'Orders'
        self.db = db.db


    def buy(self, customerId, productId, paymentMethodId, deliveryMethodId, quantity, price, address):
        cursor = self.db.cursor()
        cursor.execute(f'''
            INSERT INTO {self.table} (
                customer_id,
                product_id, 
                payment_method_id, 
                delivery_method_id, 
                quantity, 
                price, 
                currency, 
                payment_status, 
                delivery_address, 
                delivery_status, 
                order_date
            ) VALUES (
                {customerId}, 
                {productId}, 
                {paymentMethodId}, 
                {deliveryMethodId}, 
                {quantity}, 
                {price}, 
                'USD', 
                'pending', 
                '{address}', 
                'in_progress', 
                CURDATE()
            );
        ''')
        self.db.commit()


    def getAll(self, customerId):
        cursor = self.db.cursor()
        cursor.execute(f'''
            SELECT 
                c.name, 
                c.surname, 
                o.order_date, 
                p.title, 
                p.price, 
                p.currency, 
                dm.d_type, 
                o.delivery_address, 
                o.delivery_status, 
                pm.p_type, 
                o.payment_status  
            FROM {self.table} o
            INNER JOIN Products p ON p.id=o.product_id
            INNER JOIN Customers c ON o.customer_id=c.id
            INNER JOIN DeliveryMethods dm  ON o.delivery_method_id=dm.id
            INNER JOIN PaymentMethods pm ON o.payment_method_id=pm.id
            WHERE customer_id={customerId};
        ''')

        return cursor.fetchall()
