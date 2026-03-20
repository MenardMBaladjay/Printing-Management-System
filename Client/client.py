#!/usr/bin/env python3

import sys
import requests

url = "http://127.0.0.1:8000"

def view():
    print("List of all orders...")

    response = requests.get(f"{url}/orders")

    if response.status_code == 200:
        orders = response.json()

        for order in orders:
            cost = order['total_cost']
            print(f"ID: {order['order_id']} | Name: {order['student_name']} | Doc: {order['document_name']} | Type: {order['print_type']} | Pages: {order['pages']} | Cost: ₱{cost:.2f}")

    else:
        print("Fetch Error")

def search(args):
    print("this is the search function")

    try:
        order_id = int(args[1])
    except (ValueError, IndexError):
        print("Invalid ID")
        return 
    
    response = requests.get(f"{url}/orders/{order_id}")

    if response.status_code == 200:
        order = response.json()
        cost = order['total_cost']
        print(f"Name: {order['student_name']} | Doc: {order['document_name']} | Type: {order['print_type']} | Pages: {order['pages']} | Cost: ₱{cost:.2f}")

    else:
        print("Order not found")

def order(args):
    print("this is the order function")

    student_name, document_name, print_type, pages = args[1], args[2], args[3], args[4]

    data = {
        "student_name": student_name,
        "document_name": document_name,
        "print_type": print_type,
        "pages": int(pages)
    }

    print(data)

    response = requests.post(f"{url}/orders", json=data)

    if response.status_code == 200:
        cost = response.json()['total_cost']
        print(f"Order placed successfully, Total Cost: ₱{cost:.2f}")

    else:
        print("Error placing order", response.json().get('detail', 'Unknown error'))

def update(args):
    print("this is the update function")

    order_id = args[1]
    data = {
        "student_name": args[2],
        "document_name": args[3],
        "print_type": args[4],
        "pages": int(args[5])
    }

    response = requests.put(f"{url}/orders/{order_id}", json=data)

    if response.status_code == 200:
        result = response.json()
        cost = result['total_cost']
        print(f"Order {order_id} updated successfully!")
        print(f"New Total Cost: ₱{cost:.2f}")

    else:
        print("Update Error", response.json().get('detail', 'Unknown error'))

def delete(args):
    print("this is the delete function")

    order_id = args[1]
    
    response = requests.delete(f"{url}/orders/{order_id}")

    if response.status_code == 200:
        print(f"Order {order_id} deleted successfully.")

    else:
        print("Delete Error", response.json().get('detail', 'Unknown error'))

def main():
    cmnd = sys.argv[1]
    
    if cmnd == "order":
        order(sys.argv[1:])

    elif cmnd == "search":
        search(sys.argv[1:])

    elif cmnd == "view":
        view()

    elif cmnd == "update":
        update(sys.argv[1:])

    elif cmnd == "delete":
        delete(sys.argv[1:])

if __name__ == "__main__":
    main()