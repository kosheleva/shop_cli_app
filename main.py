
from db.db import DB

from db.customers import Customers
from db.categories import Categories
from db.deliveryMethods import DeliveryMethods
from db.discounts import Discounts
from db.orders import Orders
from db.paymentMethods import PaymentMethods
from db.products import Products

from cli import CLI

# Initialization DB object to connect to database
db = DB()

# DB models initialization
customers = Customers(db)
categories = Categories(db)
deliveryMethods = DeliveryMethods(db)
discounts = Discounts(db)
orders = Orders(db)
paymentMethods = PaymentMethods(db)
products = Products(db)

# Command line initialization and running
cli = CLI (categories, customers, deliveryMethods, discounts, orders, paymentMethods, products)
cli.start()