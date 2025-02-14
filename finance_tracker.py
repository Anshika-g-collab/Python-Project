import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Initialize main data structure
data = []  # List to store transactions
categories = ["Food", "Transport", "Bills", "Entertainment", "Others"]

# Function to add a transaction
def add_transaction():
    try:
        date = entry_date.get()
        category = category_var.get()
        amount = float(entry_amount.get())
        transaction_type = transaction_type_var.get()

        if not date or not category or not transaction_type:
            raise ValueError("All fields are required!")

        data.append({"Date": date, "Category": category, "Amount": amount, "Type": transaction_type})
        messagebox.showinfo("Success", "Transaction added successfully!")
        clear_entries()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to clear input fields
def clear_entries():
    entry_date.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    category_var.set("")
    transaction_type_var.set("")

# Function to generate monthly report
def generate_report():
    if not data:
        messagebox.showwarning("Warning", "No transactions to analyze!")
        return

    df = pd.DataFrame(data)
    df["Amount"] = df["Amount"].astype(float)

    # Calculate totals for income and expenses
    income = df[df["Type"] == "Income"]["Amount"].sum()
    expenses = df[df["Type"] == "Expense"]["Amount"].sum()

    # Display totals
    messagebox.showinfo("Monthly Report", f"Total Income: {income}\nTotal Expenses: {expenses}\nNet Savings: {income - expenses}")

# Function to visualize income vs expenses
def visualize_data():
    if not data:
        messagebox.showwarning("Warning", "No transactions to visualize!")
        return

    df = pd.DataFrame(data)
    df["Amount"] = df["Amount"].astype(float)

    # Group data by type
    summary = df.groupby("Type")["Amount"].sum()

    # Plot data
    summary.plot(kind="bar", color=["green", "red"], title="Income vs Expenses")
    plt.ylabel("Amount")
    plt.show()

# Initialize the main application window
root = tk.Tk()
root.title("Personal Finance Tracker")

# Entry widgets for input
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0)
category_var = tk.StringVar()
category_menu = tk.OptionMenu(root, category_var, *categories)
category_menu.grid(row=1, column=1)

tk.Label(root, text="Amount:").grid(row=2, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1)

tk.Label(root, text="Type:").grid(row=3, column=0)
transaction_type_var = tk.StringVar()
type_menu = tk.OptionMenu(root, transaction_type_var, "Income", "Expense")
type_menu.grid(row=3, column=1)

# Buttons for actions
tk.Button(root, text="Add Transaction", command=add_transaction).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Generate Monthly Report", command=generate_report).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Visualize Income vs Expenses", command=visualize_data).grid(row=6, column=0, columnspan=2)

# Run the application
root.mainloop()
