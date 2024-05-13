class CLI:
    def __init__(self, categories, customers, deliveryMethods, discounts, orders, paymentMethods, products):
        self.categories = categories
        self.customers = customers
        self.deliveryMethods = deliveryMethods
        self.discounts = discounts
        self.orders = orders
        self.paymentMethods = paymentMethods
        self.products = products

        # List of available commands
        self.help = '''
+-------------------------------------\ОO/---------------------------------------+
|                             Shop "Fashionable owl"                             |
|                     A wide selection of jewelry for everyone                   | 
+--------------------------------------------------------------------------------+
| Login to system                             login:name:password                |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| 
| List products                               list_products                      |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| List products in specific category          list_products_in:category          |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| List categories                             list_categories                    |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| List products with discounts                list_products_with_discounts       |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| 
| List available payment methods              list_payment_methods               |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| List delivery types                         list_delivery_types                |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| Buy product                                 buy                                |
|                                                :product                        |
|                                                :payment_method                 |
|                                                :delivery_method                |
|                                                :quantity                       |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| Show cart                                   cart                               | 
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| List available commands                     help                               |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| Logout                                      exit                               |  
+--------------------------------------------------------------------------------+
'''

    # Display data
    def display(self, result):
        if (not len(result)):
            return '--- No data ---'

        print('\n')
        print('~' * 100)

        for row in result:
            line = '';
            
            for item in row:
                line += str(item).strip() + ', '
            

            print(line[:-2])
            print('~' * 100)
        
        print('\n')


    # Run command line
    def start(self):

        # Welcome message
        print(self.help)

        command = ''
        userId = ''

        while True:
            command = input('> ')

            if command == 'help':
                print (self.help)
            elif command == 'exit':
                break
            elif 'login' in command:
                cmd = command.split(':')
                name = cmd[1]
                password = cmd[2]

                data = self.customers.get(name, password)

                if (not data):
                    print("Invalid name or password.")
                else:
                    userId = data[0][0]
                    print(f'''Authorization success! User ID={userId}''')
            elif command == 'list_products':
                data = self.products.getAll()
                self.display(data)
            elif 'list_products_in' in command:
                cmd = command.split(':')
                category = cmd[1]
                data = self.products.getAllByCategory(category)
                self.display(data)
            elif 'list_categories' in command:
                data = self.categories.getAll()
                self.display(data)
            elif 'list_products_with_discounts' in command:
                data = self.products.getAllWithDiscounts()
                self.display(data)
            elif 'list_payment_methods' in command:
                data = self.paymentMethods.getAll()
                self.display(data)
            elif 'list_delivery_types' in command:
                data = self.deliveryMethods.getAll()
                self.display(data)
            elif 'buy' in command:
                cmd = command.split(':')
                productTitle = cmd[1]
                paymentMethodType = cmd[2]
                deliveryMethodType = cmd[3]
                quantity = cmd[4]

                product = self.products.getByTitle(productTitle)
                paymentMethod = self.paymentMethods.getByType(paymentMethodType)
                deliveryMethod = self.deliveryMethods.getByType(deliveryMethodType)

                self.orders.buy(userId, product[0][0], paymentMethod[0][0], deliveryMethod[0][0], quantity, product[0][3], 'Department 140')

                data = self.orders.getAll(userId)
                self.display(data)
            elif 'cart' in command:
                data = self.orders.getAll(userId)
                self.display(data)
            else:
                print("Unknown command")
