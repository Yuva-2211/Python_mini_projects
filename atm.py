import streamlit as st
from datetime import datetime



class Account:
    def __init__(self, acc_no, pin, balance):
        self.acc_no = acc_no
        self.__pin = pin
        self.balance = balance
        self.attempts = 0
        self.locked = False
        self.transactions = []   # transaction history

    def validate_pin(self, pin):
        if self.locked:
            return False

        if pin == self.__pin:
            self.attempts = 0
            return True
        else:
            self.attempts += 1
            if self.attempts >= 3:
                self.locked = True
            return False

    def add_transaction(self, t_type, amount):
        self.transactions.append({
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "type": t_type,
            "amount": amount,
            "balance": self.balance
        })

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.add_transaction("Withdraw", amount)
            return True
        return False


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, pin, balance):
        if acc_no in self.accounts:
            return False
        self.accounts[acc_no] = Account(acc_no, pin, balance)
        return True

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)



if "bank" not in st.session_state:
    st.session_state.bank = Bank()
    st.session_state.logged_in = False
    st.session_state.account = None



st.title("ATM Simulation System")

menu = ["Login", "Create Account"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Account":
    st.subheader(" Create New Account")

    acc_no = st.text_input("Choose Account Number")
    pin = st.text_input("Set PIN", type="password")
    balance = st.number_input("Initial Deposit", min_value=500, step=100)

    if st.button("Create Account"):
        if acc_no and pin:
            if st.session_state.bank.create_account(acc_no, pin, balance):
                st.success("Account created successfully!")
            else:
                st.error("Account number already exists")
        else:
            st.error("All fields are required")


elif choice == "Login" and not st.session_state.logged_in:
    st.subheader(" Login")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Login"):
        account = st.session_state.bank.get_account(acc_no)

        if not account:
            st.error("Account not found")

        elif account.locked:
            st.error("Account locked due to 3 wrong PIN attempts")

        elif account.validate_pin(pin):
            st.session_state.logged_in = True
            st.session_state.account = account
            st.success("Login successful")

        else:
            remaining = 3 - account.attempts
            st.error(f"Wrong PIN! Attempts left: {remaining}")

if st.session_state.logged_in:
    account = st.session_state.account

    st.subheader(" ATM Menu")

    option = st.radio(
        "Select an option:",
        ["Check Balance", "Deposit", "Withdraw", "Transaction History", "Logout"]
    )

    if option == "Check Balance":
        st.info(f" Current Balance: ₹{account.balance}")

    elif option == "Deposit":
        amount = st.number_input("Enter amount", min_value=1, step=1)
        if st.button("Deposit"):
            account.deposit(amount)
            st.success("Amount deposited successfully")

    elif option == "Withdraw":
        amount = st.number_input("Enter amount", min_value=1, step=1)
        if st.button("Withdraw"):
            if account.withdraw(amount):
                st.success("Withdrawal successful")
            else:
                st.error("Insufficient balance")

    elif option == "Transaction History":
        st.subheader(" Transaction History")

        if account.transactions:
            st.table(account.transactions)
        else:
            st.info("No transactions yet")

    elif option == "Logout":
        st.session_state.logged_in = False
        st.session_state.account = None
        st.success("Logged out successfully")
