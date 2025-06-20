ATM = 0
balance = 1000

pin = int(input("Please enter your pin: "))

if pin == 1234:

    while ATM != "exit":
        ATM = input("Withdraw, deposit, balance or exit? ")
        if ATM == "balance":
            print("Your balance is:", balance)
        elif ATM == "withdraw":
            withdraw = int(input("How much do you want to withdraw? "))
            balance -= withdraw
            print("Your balance is:", balance)
        elif ATM == "deposit":
            deposit = int(input("How much do you want to deposit? "))
            balance += deposit
            print("Your balance is:", balance)
        elif ATM == "exit":
            print("Thanks for using me! Bye bye :)")
        else:
            print("Please type one of valid operations")
else:
    print("Wrong password")
