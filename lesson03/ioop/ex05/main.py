from bank import BankAccount

def main():
    bankaccount = BankAccount("12345", 10000.0)
    select = input("what do you want to do?\npress 1 to deposit\npress 2 to withdraw\npress 3 to see balance\npress x to exit\n")
    while select != 'x':
        if select == '1':
            amount = input("how much you want to deposit\n")
            if type(amount) != str:
                bankaccount.deposit(float(amount))
            else:
                print("Enter only numbers")
        if select == '2':
            amount = input("how much you want to withdraw\n")
            if type(amount) != str:
                bankaccount.withdraw(float(amount))
            else:
                print("Enter only numbers")
        if select == '3':
            print(bankaccount.balance)
        select = input("anything else?\n")
    print('Good Bye')

main()