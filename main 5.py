# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    import json
    import os.path
    from collections import defaultdict
    import webbrowser
    def print_hi(name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # class Groceriy(object):

    # def __init__(self, name:str, number:int):

    class Customer(object):

        def __init__(self, username: str, kode: str):
            self.groceries = []
            self.username = username
            self.kode = kode

    def del_grocery(customer: Customer):
        grocery_name = input("Enter grocery name: ")
        amount = int(input("Enter grocery amount: "))
        for x in customer.groceries:
            if grocery_name == x["name"]:
                if amount == 0:
                    print(x)
                    customer.groceries.remove(x)
                else:
                    x["amount"] = amount

    def add_grocery(customer: Customer):
        grocery_name = input("Enter grocery name: ")
        amount = input("Enter grocery amount: ")

        # grocery = Grocery(grocery_name, int(amount))
        customer.groceries.append(
            {
                "name": grocery_name,
                "amount": int(amount)
            }
        )

        return customer

    def wrongcode(customer: Customer):
        r = 5
        for s in range(r):
            print(customer.kode)
            print("wrong password enter again you left ", r - s, "trais")
            your_kode = str(input())
            if your_kode == customer.kode:
                customer.kode = your_kode
                return your_kode

    def main():

        print("Login, enter your name: ")
        username = input()
        kode = input("please enter your kode")
        customer = Customer(username, kode)

        if os.path.isfile(f"{username}.txt"):
            mid = customer.kode
            with open(f"{username}.txt", "r") as file:
                customer_data = file.read()
                if len(customer_data) != 0:
                    customer_data_as_dict = json.loads(customer_data)
                    customer.__dict__.update(customer_data_as_dict)

                    if customer.kode == mid:
                        print(customer_data_as_dict)
                    else:
                        if wrongcode(customer) != customer.kode:
                            print("your acount is bloke for naw")
                            exit(0)

        else:
            with open(f"{username}.txt", "a+") as file:
                r = file.read()

        while True:
            choice = input("Enter choice:\n1 - add product\n2 - remove/change count product\n\nenter choice: ")
            if choice == "1":
                customer = add_grocery(customer)
            if choice == "2":
                del_grocery(customer)

            with open(f"{customer.username}.txt", "w") as file:
                jsonStr = json.dumps(customer.__dict__)
                file.write(jsonStr)

    # customer = # Convert dict to class

    if __name__ == '__main__':
        main()

    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        print_hi('PyCharm')

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
