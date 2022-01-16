import sqlite3


conn = sqlite3.connect('amit.db')
c = conn.cursor()


class Store:


    def customer_information(self):
        name=str(input("Enter your name: "))
        email=str(input("Enter your email: "))
        address=str(input("Enter your address: "))
        phone=int(input("Enter your phone number: "))
        password=str(input("Enter your password: "))

        c.execute("INSERT INTO User(name,email,address,phone,password) VALUES(?,?,?,?,?)", (name, email, address, phone,password))
        conn.commit()


        self.login()







    def insert_product(self):
        while True:
            product_name=str(input("Enter the name of product: "))
            quantity=int(input("Enter the quantity: "))
            price=int(input("Enter the price: "))
            description=str(input("Enter the description: "))

            c.execute("INSERT INTO Product(name,quantity,price,description)  VALUES(?,?,?,? )", (product_name, quantity, price, description))
            conn.commit()

            add = str(input("Do you want to add more item .If yes press y .If no press n: "))
            if add=='n':
                self.admin()


    def customer_buying(self):
        print(" Amit is full of \n")
        c.execute("SELECT name FROM Product")
        product_list=c.fetchall()

        print("ITEAM")
        print("-----------------------")
        for product in product_list:
            for p in product:
                print(p)

        self.buy = str(input("Enter product name for viewing deatil of product: "))
        name = ('name', 'price', 'quantity_available', 'description')
        c.execute("SELECT * FROM Product  WHERE name=:buy", {'buy': self.buy})
        product_detail = c.fetchall()
        self.nam = dict(zip(name, product_detail[0]))

        for key, value in self.nam.items():
            print(key, ' : ', value)

        self.processing()


    def processing(self):
            while True:
                choice = str(input("Press confirm to buy the product. To cancle buying type cancel: "))


                if choice=='confirm' or choice=='Confirm':
                    quantity = int(input("Enter the quantity you want to buy: "))
                    c.execute("SELECT * FROM User WHERE email=:email", {'email': self.email})



                    c.execute("INSERT INTO Customer_buy(email, product,quantity, price)  VALUES(?,?,?,?,?,? )", (self.email, self.buy, quantity,self.nam['price']))
                    conn.commit()
                    print("Congratulation you have bought the item from our store.")

                    while True:
                        choice=int(input("Press 1 for viewing purchase detail till date\nPress 2 for logout:"))
                        if choice==1:
                            self.detail()
                        elif choice==2:
                            self.start()
                        else:
                            print("Invalid Input")

                elif choice=='cancel' or choice=='Cancel':
                    self.customer_buying()
                else:
                    print('Invalid Input')

    def detail(self):
        self.email='y'
        c.execute("SELECT * FROM Customer_buy  WHERE email=:email", {'email': self.email})
        cus_data=c.fetchall()

        print("email\t\t product name\t\t quantity\t\t Marked Price total \t\t discount amount\t\t total_amount ")
        for data in cus_data:

            print(f'{data[0]}\t\t{data[1]}\t\t\t{data[2]}\t\t\t{data[3]}\t\t\t{data[4]}\t\t\t{data[5]}')

        while True:
            choice=int(input("Press 1 for logout \nPress 2 for continue buying: "))

            if choice==1:
                self.start()
            elif choice ==2:
                self.customer_buying()
            else:
                print("Invalid Input ")




    def notification(self):
        c.execute("SELECT name,quantity FROM Product")
        product_data=c.fetchall()
        # import pdb;pdb.set_trace()
        print(product_data)

        flag=True
        for data in product_data:
            if data[1]<10:
                print(f'{data[0]} is going to be out of stock. Only 10 are left')
                flag=False

        if flag==True:
            print("Every product is above 10 quantity")
        while True:
            choice=int(input("Press 1 for home."))
            if choice==1:
                self.admin()
            else:
                print("Invalid Input")
    def login(self):
        while True:
            print("Please login !!!")

            self.email = str(input("Enter your email: "))
            self.password = str(input("Enter your password: "))

            c.execute("SELECT email, password FROM User")
            users = c.fetchall()

            user_flag = False
            for user in users:

                if user[0] == self.email and user[1] == self.password:
                    user_flag = True
                    print("Accese granted")
                    print('--------------------------------------------------')

                    break

            if user_flag == False:
                print("Either username or password is incorrect. OR not register in the system")


            else:
                if self.user_type=='admin'or self.user_type=='Admin':
                    self.admin()
                else:
                    self.customer_buying()

    def start(self):
        while True:
            print("Welcome to AMit Nepal Online Store")
            want=int(input("To Login .Press 1. \nTo SignIn. Press 2\nPress 3 for change user: "))

            if want==1:
                self.login()
            elif want==2:
                self.customer_information()
            elif want==3:
                self.first()
            else:
                print("Invalid Input")

    def first(self):
        while True:
            self.user_type=str(input("Enter admin to login as Admin\nEnter user to login as normal user: "))
            self.start()
            # if self.user_type=='admin'or self.user_type=='Admin':
            #     self.admin()
            # elif self.user_type=='user'or self.user_type=='User':
            #     self.start()
            # else:
            #     print('Invalid Input')

    def admin(self):
        while True:
            print("WELCOME TO  Amit ADMIN PANNEL")
            print("------------------------------------------------------------")
            choice = int(input("Press 1 to insert product \nPress 2 to get out of stock notification\n Press 3 for change user: "))
            if choice == 1:
                self.insert_product()
            elif choice == 2:
                self.notification()
            elif choice == 3:
                self.first()
            else:
                print("Invalid input")



obj=Store()
obj.first()

