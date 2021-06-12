#! /usr/bin/python3

import time as t
import pyttsx3

machine = pyttsx3.init()

card_nos = [123, 456, 789, 369, 258, 147]
pass_codes = [5648, 2563, 8754, 9556, 2663, 5859]
balance = [58469, 25637, 4532, 1623, 45662, 488957]
mobile = [545657, 566331, 233310, 789123, 654821, 321947]

print("************************")
print("*****WELCOME TO ATM*****")
print("************************")

machine.say("WELCOME TO ATM")
machine.runAndWait()
print()
print()
t.sleep(1)

def main():
    machine.say("Enter your card number")
    machine.runAndWait()
    card_no = int(input("Enter your card number\n"))
    print()
    if card_no not in card_nos:
        print("This card does not exist")
        machine.say("This card does not exist")
        machine.runAndWait()
        print()
        t.sleep(1)
        machine.say("Do you want to try again y for yes n for no")
        machine.runAndWait()
        ans = input("Do you want to try again(y/n)\n")

        if ans == 'Y' or ans == 'y':
            main()

        elif ans == 'N' or ans == 'n':
            print("Thankyou visit again")
            machine.say("Thankyou visit again")
            machine.runAndWait()
            quit()

        else:
            print("Invalid input")
            machine.say("Invalid input")
            machine.runAndWait()
            print("Thankyou visit again")
            machine.say("Thankyou visit again")
            machine.runAndWait()
            quit()

    else:
        global index
        index = card_nos.index(card_no)
        machine.say("Enter your pin")
        machine.runAndWait()
        pass_ = int(input("Enter your PIN\n"))

        print()
        if pass_ == pass_codes[index]:
            options()
        else:
            print("Invalid PIN")
            machine.say("Invalid pin")
            machine.runAndWait()
            machine.say("Do you want to try again y for yes n for no")
            machine.runAndWait()
            ans = input("Do you want to try again(y/n)\n")

            if ans == 'Y' or ans == 'y':
                main()

            elif ans == 'N' or ans == 'n':
                print("Thankyou visit again")
                machine.say("Thankyou visit again")
                machine.runAndWait()
                quit()

            else:
                print("Invalid input")
                machine.say("Invalid input")
                machine.runAndWait()
                print("Thankyou visit again")
                machine.say("Thankyou visit again")
                machine.runAndWait()
                quit()

def options():

    print("1:Account Balance")
    machine.say("Enter 1 for Account Balance")
    machine.runAndWait()
    print("2:Withdraw Money")
    machine.say("Enter 2 to Withdraw Money")
    machine.runAndWait()
    print("3:Deposit Money")
    machine.say("Enter 3 to Deposit Money")
    machine.runAndWait()
    print("4:Update Mobile Number")
    machine.say("Enter 4 to Update Mobile Number")
    machine.runAndWait()
    print("5:Change PIN")
    machine.say("Enter 5 to Change pin")
    machine.runAndWait()
    print("0:Exit")
    machine.say("Enter 0 to Exit")
    machine.runAndWait()
    machine.say("Enter Your Choice")
    machine.runAndWait()
    choice = int(input("Enter Your Choice\n"))

    if choice == 1:
        ac_balance()

    elif choice == 2:
        withdraw()

    elif choice == 3:
        deposit()

    elif choice == 4:
        updatemobile()

    elif choice == 5:
        changepin()

    elif choice == 0:
        print("Thank You Visit Again")
        machine.say("Thank You Visit Again")
        machine.runAndWait()
        quit()

    else:
        print("Invalid input try again")
        machine.say("Invalid input try again")
        machine.runAndWait()
        options()


def ac_balance():

    print("Your Account Balance is: " + str(balance[index]))
    machine.say("Your Account Balance is Rupees")
    machine.say(balance[index])
    machine.runAndWait()
    t.sleep(2)
    print()
    print("Thank You Visit Again")
    machine.say("Thank You Visit Again")
    machine.runAndWait()
    quit()


def withdraw():
    machine.say("Enter the Amount You Want to Withdraw in Multiples of 100")
    machine.runAndWait()
    ans = int(input("Enter the Amount You Want to Withdraw in Multiples of 100\n"))

    if ans % 100 != 0:
        print("Please Enter a Multiple of 100")
        machine.say("Please Enter a Multiple of 100")
        machine.runAndWait()
        print()
        withdraw()

    else:
        if ans > balance[index]:
            print("Insufficient Balance")
            machine.say("Insufficient Balance")
            machine.runAndWait()
            print("Thank You Visit Again")
            machine.say("Thank You Visit Again")
            machine.runAndWait()
            quit()

        else:
            amount = ans
            print("Processing Your Transaction")
            machine.say("Processing Your Transaction")
            machine.runAndWait()

            note2t = amount // 2000
            amount = amount % 2000
            note5h = amount // 500
            amount = amount % 500
            note2h = amount // 200
            amount = amount % 200
            note1h = amount // 100
            t.sleep(1)
            balance[index] = balance[index] - ans
            print("Transaction Successfull")
            machine.say("Transaction Successfull")
            machine.runAndWait()
            print()
            print("Please Collect Your: \n" + str(note2t) + " Notes of 2000 \n" + str(note5h) +
                  " Notes of 500 \n" + str(note2h) + " Notes of 200\n" + str(note1h) + " Notes of 100\n")
            machine.say("Please Collect Your " + str(note2t) + " Notes of 2000 " + str(note5h) +
                        " Notes of 500 " + str(note2h) + " Notes of 200 " + str(note1h) + " Notes of 100")
            machine.runAndWait()
            print()
            print("Your Updated Balance is: " + str(balance[index]))
            machine.say("Your Updated Balance is Rupees ")
            machine.say(balance[index])
            machine.runAndWait()
            print()
            print("Thank You Visit Again")
            machine.say("Thank You Visit Again")
            machine.runAndWait()
            quit()

def deposit():
    machine.say("Enter the Amount You Want to Deposit")
    machine.runAndWait()
    ans = int(input("Enter the Amount You Want to Deposit\n"))
    balance[index] = balance[index] + ans
    print("Amount Deposited Successfully")
    machine.say("Amount Deposited Successfully")
    machine.runAndWait()
    print()
    print("Your Updated Balance is: " + str(balance[index]))
    machine.say("Your Updated Balance is ")
    machine.say(balance[index])
    machine.runAndWait()
    print()
    print("Thank You Visit Again")
    machine.say("Thank You Visit Again")
    machine.runAndWait()
    quit()

def updatemobile():
    machine.say("Enter Old Mobile Number")
    machine.runAndWait()
    ans = int(input("Enter Old Mobile Number\n"))
    if ans == mobile[index]:
        machine.say("Enter New Mobile Number")
        machine.runAndWait()
        new = int(input("Enter New Mobile Number\n"))
        new = str(new)
        if len(new) < 6 or len(new) > 6:
            print("Invalid Input Only 6 Digits Allowed")
            machine.say("Invalid Input Only 6 Digits Allowed")
            machine.runAndWait()
            print()
            print("Transaction Cancelled")
            machine.say("Transaction Cancelled")
            machine.runAndWait()
            print()
            print("Thank You Visit Again")
            machine.say("Thank You Visit Again")
            machine.runAndWait()
            quit()

        else:
            new = int(new)
            mobile[index] = new
            print()
            print("Mobile Number Updated Successfully")
            machine.say("Mobile Number Updated Successfully")
            machine.runAndWait()
            print()
            print("Thank You Visit Again")
            machine.say("Thank You Visit Again")
            machine.runAndWait()
            quit()

    else:
        print("Invalid Input")
        machine.say("Invalid Input")
        machine.runAndWait()
        print("Thank You Visit Again")
        machine.say("Thank You Visit Again")
        machine.runAndWait()
        quit()

def changepin():

    machine.say("Please Enter the old pin")
    machine.runAndWait()
    old = int(input("Please Enter the Old PIN\n"))
    if old != pass_codes[index]:
        print("Invalid Input")
        machine.say("Invalid Input")
        machine.runAndWait()
        print()
        print("Transaction Cancelled")
        machine.say("Transaction Cancelled")
        machine.runAndWait()
        print()
        print("Thank You Visit Again")
        machine.say("Thank You Visit Again")
        machine.runAndWait()
        quit()

    else:
        machine.say("Enter New pin")
        machine.runAndWait()
        new = int(input("Enter New PIN\n"))
        print()
        machine.say("Enter New pin Again")
        machine.runAndWait()
        new_ = int(input("Enter New PIN Again\n"))
        if new == new_:
            pass_codes[index] = new
            print("PIN Updated SuccessFully")
            machine.say("pin Updated SuccessFully")
            machine.runAndWait()
            print()
            print("Thank You Visit Again")
            machine.say("Thank You Visit Again")
            machine.runAndWait()
            quit()

        else:
            print("Invalid Input")
            machine.say("Invalid Input")
            machine.runAndWait()
            print("Both the Entries Should Match")
            machine.say("Both the Entries Should Match")
            machine.runAndWait()
            print()
            print("Transaction Cancelled")
            machine.say("Transaction Cancelled")
            machine.runAndWait()
            print()
            print("Thank You Visit Again")
            machine.say("Thank You Visit Again")
            machine.runAndWait()
            quit()

main()
