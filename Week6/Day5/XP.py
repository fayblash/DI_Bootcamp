import sqlite3
from tabulate import tabulate

def show_user_menu():
    flag=True
    while flag:
        choice=input('''
        MENU
(a) Add an Item
(u) Update an Item
(d) Delete an Item
(v) View the Menu
(x) Exit
    ''')
        if choice=="a":
            add_item()
        elif choice=='u':
            update_item()
        elif choice=="d":
            remove_item()
        elif choice=="v":
            show_restaurant_menu()
        elif choice=="x":
            flag=False
        else:
            raise Exception("invalid data entered")
            break

def add_item():
    item=input("Enter the name of an item to add to the menu: ")
    price=int(input("Enter the price of the item: "))
    query=f"INSERT INTO menu_item(item,price) VALUES ('{item}',{price});"
    return run_query(query)

def update_item():
    name=input("Enter the name of an item you wish to update: ")
    item=input("Enter the name of the updated item: ")
    price=int(input("Enter the price of the updated item: "))
    query=f"UPDATE menu_item SET item='{item}',price={price} WHERE item='{name}';"
    return run_query(query)

    
def remove_item():
    del_item=input("Enter the name of the item you wish to delete")
    query=f"DELETE {del_item} FROM menu_item;"
    return run_query(query)

def show_restaurant_menu():
    query = "SELECT item, price FROM menu_item ORDER BY item ASC;"
    menu=run_query(query)
    print(tabulate(menu, headers=['Item', 'Price']))

def run_query(query):
    connection = sqlite3.connect("menu.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results

show_user_menu()

