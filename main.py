import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user= "username",
    password= "password",
    database= "Client_and_Product_Management_System",
)

choice = None
mycursor = mydb.cursor()

def show_tables():
    mycursor.execute("SHOW TABLES")
    for table in mycursor:
        print("-----------------------")
        print(f"|Table name | {table[0]}|")

def check_table_exist(table_name):
    mycursor.execute("SHOW TABLES")
    for table in mycursor:
        if str(table[0]) == table_name:
            return True
    return False

def insert_table_clients(table_name, name, city, email, phone):
    query = f"INSERT INTO {table_name} (name, city, email, phone) VALUES (%s, %s, %s, %s)"
    values = (name, city, email, phone)
    mycursor.execute(query, values)
    mydb.commit()

def insert_table_products(table_name, name, price, stock, sales):
    query = f"INSERT INTO {table_name} (name, price, stock, sales) VALUES (%s, %s, %s, %s)"
    values = (name, price, stock, sales)
    mycursor.execute(query, values)
    mydb.commit()

def print_tables(table_name):
    query = f"SELECT * FROM {table_name}"
    mycursor.fetchall()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)

def update_info(table_name, name, what_to_change, new_change):
    query = f"UPDATE {table_name} SET {what_to_change} = %s WHERE nameLIKE %s"
    name_with_wildcards = f"%{name}%"
    values = (new_change, name_with_wildcards)
    mycursor.execute(query, values)
    mydb.commit()

def delete_info(table_name, name):
    query = f"DELETE FROM {table_name} WHERE name LIKE %s"
    name_with_wildcards = f"%{name}%"
    values = (name_with_wildcards,)
    mycursor.fetchall()
    mycursor.execute(query, values)
    mydb.commit()

while choice != 0:
    print("Choose an option:")
    print("1. Show tables")
    print("2. Insert new client")
    print("3. Insert new product")
    print("4. Print table(s)")
    print("5. Update info")
    print("6. Delete info")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            show_tables()
            print("\n")
        case 2:
            table_name = "clients"
            name = input("Enter client's name: ")
            city = input("Enter city: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            insert_table_clients(table_name, name, city, email, phone)
            print("Table inserted successfully!")

        case 3:
            table_name  = "products"
            name = input("Enter product's name: ")
            price = input("Enter product's price: ")
            stock = input("Enter product's stock: ")
            sales = input("Enter product's sales: ")
            insert_table_products(table_name, name, price, stock, sales)
            print("Table inserted successfully!")
        case 4:
            choice_table = input("Please enter table name: ")
            if check_table_exist(choice_table):
                print_tables(choice_table)
            print(f"Table with name {choice_table} does not exists.")

        case 5:
            table_name = input("Enter table name: ")
            name = input("Enter client's/product's id: ")
            what_to_change = input("Enter what to change: ")
            new_change = input("Enter new value: ")
            if check_table_exist(table_name):
                 update_info(table_name, name, what_to_change, new_change)
                 print("Table updated successfully!")
            else:
                print("Table does not exist.")

        case 6:
            table_name = input("Enter table name: ")
            name = input("Enter product's/client's name: ")
            if check_table_exist(table_name):
                delete_info(table_name, name)
                print("Table deleted successfully!")
            else:
                print("Table does not exist.")

        case 0:
            print("Exiting")
        case _:
            print("Invalid choice, try again!")


