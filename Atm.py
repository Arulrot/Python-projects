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

# ------------------ ATM BALANCE FUNCTIONS ------------------
def get_atm_balance():
    qry = "SELECT n500, n200, n100 FROM atmbal WHERE id = 1"
    cursor.execute(qry)
    n500, n200, n100 = cursor.fetchone()
    return n500, n200, n100


def update_atm_balance(n500, n200, n100):
    qry = "UPDATE atmbal SET n500=%s, n200=%s, n100=%s WHERE id=1"
    cursor.execute(qry, (n500, n200, n100))
    conn.commit()


def calculate_notes(amount, n500, n200, n100):
    given_500 = min(amount // 500, n500)
    amount -= given_500 * 500

    given_200 = min(amount // 200, n200)
    amount -= given_200 * 200

    given_100 = min(amount // 100, n100)
    amount -= given_100 * 100

    if amount != 0:
        return None

    return given_500, given_200, given_100


# ------------------ ATM OPERATIONS ------------------
def withdraw(card_number, acc_bal):
    wdth_amt = int(input("\nEnter Withdrawal Amount : "))

    if wdth_amt > acc_bal:
        print(" Insufficient Account Balance")
        return acc_bal

    n500, n200, n100 = get_atm_balance()
    atm_total = n500*500 + n200*200 + n100*100

    if wdth_amt > atm_total:
        print(" ATM has insufficient cash")
        return acc_bal

    notes = calculate_notes(wdth_amt, n500, n200, n100)

    if notes is None:
        print(" Cannot dispense requested amount")
        return acc_bal

    g500, g200, g100 = notes

    print("\nPlease wait...")
    time.sleep(1)
    print("Collect your cash")
    print(f"500 x {g500}, 200 x {g200}, 100 x {g100}")

    update_atm_balance(n500-g500, n200-g200, n100-g100)

    acc_bal -= wdth_amt
    update_balance(card_number, acc_bal)
    return acc_bal


def deposit(card_number, acc_bal):
    dep_amt = int(input("\nEnter Deposit Amount : "))
    acc_bal += dep_amt
    update_balance(card_number, acc_bal)
    print(" Deposit Successful")
    return acc_bal


def balance_check(acc_bal):
    print("\n Your Account Balance:", acc_bal)
    return acc_bal


def update_balance(card_number, acc_bal):
    qry = "UPDATE customers SET balance=%s WHERE card_number=%s"
    cursor.execute(qry, (acc_bal, card_number))
    conn.commit()


# ------------------ MENU ------------------
def machine_menu(acc_bal, card_number):
    print("""
1 - Cash Withdrawal
2 - Balance Enquiry
3 - Deposit
4 - Exit
""")

    choice = int(input("Enter choice : "))

    if choice == 1:
        return withdraw(card_number, acc_bal)

    elif choice == 2:
        return balance_check(acc_bal)

    elif choice == 3:
        return deposit(card_number, acc_bal)

    elif choice == 4:
        print(" Thank you for using ARUL ATM")
        return None

    else:
        print(" Invalid option")
        return acc_bal


# ------------------ CUSTOMER FETCH ------------------
def get_customer(card_number):
    qry = "SELECT name, pin, balance FROM customers WHERE card_number=%s"
    cursor.execute(qry, (card_number,))
    return cursor.fetchone()


# ------------------ MAIN PROGRAM ------------------
def main():
    print("====== ARUL ATM ======")
    card_number = int(input("Enter Card Number : "))

    customer = get_customer(card_number)

    if customer is None:
        print(" Invalid Card")
        return

    name, pin, acc_bal = customer
    print(f"\nWelcome {name}")

    attempts = 0

    while attempts < 3:
        entered_pin = int(input("Enter PIN : "))

        if entered_pin == pin:
            while True:
                acc_bal = machine_menu(acc_bal, card_number)
                if acc_bal is None:
                    return
        else:
            print(" Wrong PIN")
            attempts += 1

    print(" Card Blocked")


# ------------------ RUN ------------------
if __name__ == "__main__":
    main()
    cursor.close()
    conn.close()
