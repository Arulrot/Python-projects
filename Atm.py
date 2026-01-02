import time
import mysql.connector

# ------------------ DATABASE CONNECTION ------------------
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='atm'
)
cursor = conn.cursor()


# ------------------ ATM OPERATIONS ------------------
def withdraw(acc_bal):
    wdth_amt = int(input("\nEnter Withdrawal Amount : "))
    if wdth_amt > acc_bal:
        print("\nInsufficient Balance")
        return acc_bal
    else:
        print("\nPlease wait...")
        time.sleep(1.5)
        print("Please collect your cash")
        return acc_bal - wdth_amt


def deposit(acc_bal):
    dep_amt = int(input("\nEnter Deposit Amount : "))
    print("\nProcessing deposit...")
    time.sleep(1)
    print("Deposit Successful")
    return acc_bal + dep_amt


def balance_check(acc_bal):
    print("\nYour Account Balance is :", acc_bal)
    return acc_bal


def update_balance(card_number, acc_bal):
    qry = "UPDATE customers SET balance = %s WHERE card_number = %s"
    cursor.execute(qry, (acc_bal, card_number))
    conn.commit()


def exit_init():
    print("\nThank you for banking with us!")
    return False


# ------------------ MENU ------------------
def machine_menu(acc_bal, session, card_number):
    print("""
    1 - Cash Withdrawal
    2 - Balance Enquiry
    3 - Deposit
    4 - Exit
    """)

    choice = int(input("Enter your choice : "))

    if choice == 1:
        new_bal = withdraw(acc_bal)
        update_balance(card_number, new_bal)
        return new_bal, session

    elif choice == 2:
        balance_check(acc_bal)
        return acc_bal, session

    elif choice == 3:
        new_bal = deposit(acc_bal)
        update_balance(card_number, new_bal)
        return new_bal, session

    elif choice == 4:
        session = exit_init()
        return acc_bal, session

    else:
        print("\nInvalid option")
        return acc_bal, session


# ------------------ DATABASE FETCH FUNCTIONS ------------------
def get_customer(card_number):
    qry = "SELECT name, pin, balance FROM customers WHERE card_number = %s"
    cursor.execute(qry, (card_number,))
    return cursor.fetchone()


# ------------------ MAIN PROGRAM ------------------
def main():
    session = True
    try_counter = 0

    print("====== ARUL ATM ======")
    card_number = int(input("\nEnter your card number : "))
    print("\nProcessing...")
    time.sleep(1)

    customer = get_customer(card_number)

    if customer is None:
        print("\nInvalid card number")
        return

    name, pin, acc_bal = customer
    print(f"\nHello {name}")

    while session:
        entered_pin = int(input("\nEnter your PIN : "))

        if entered_pin == pin:
            print("\nPIN Accepted")
            acc_bal, session = machine_menu(acc_bal, session, card_number)
            try_counter = 0  # reset attempts after success
        else:
            print("\nIncorrect PIN")
            try_counter += 1

            if try_counter >= 3:
                print("\nToo many wrong attempts")
                print("Card Blocked")
                break


# ------------------ RUN PROGRAM ------------------
if __name__ == "__main__":
    main()
    cursor.close()
    conn.close()
