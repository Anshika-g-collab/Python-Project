import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to plot the user-defined function
def plot_function():
    try:
        # Get function expression and range inputs
        expression = entry_function.get()
        x_min = float(entry_x_min.get())
        x_max = float(entry_x_max.get())

        if x_min >= x_max:
            raise ValueError("x_min should be less than x_max.")

        x = np.linspace(x_min, x_max, 500)
        y = eval(expression, {"x": x, "np": np})

        # Clear the previous plot
        ax.clear()

        # Plot the function
        ax.plot(x, y, color=color_var.get(), label="y = " + expression)
        ax.set_title("Function Plot")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to save the plot as an image
def save_plot():
    try:
        filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if filepath:
            fig.savefig(filepath)
            messagebox.showinfo("Success", "Plot saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save plot: {e}")

# Initialize the main application window
root = tk.Tk()
root.title("Interactive Plotting Tool")

# Input fields for function and range
tk.Label(root, text="Function (in terms of x):").grid(row=0, column=0)
entry_function = tk.Entry(root, width=30)
entry_function.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="x_min:").grid(row=1, column=0)
entry_x_min = tk.Entry(root, width=10)
entry_x_min.grid(row=1, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="x_max:").grid(row=2, column=0)
entry_x_max = tk.Entry(root, width=10)
entry_x_max.grid(row=2, column=1, sticky="w", padx=10, pady=5)

# Dropdown for color selection
tk.Label(root, text="Line Color:").grid(row=3, column=0)
color_var = tk.StringVar(value="blue")
color_menu = tk.OptionMenu(root, color_var, "blue", "red", "green", "black", "orange")
color_menu.grid(row=3, column=1, sticky="w", padx=10, pady=5)

# Buttons for actions
tk.Button(root, text="Plot Function", command=plot_function).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Save Plot", command=save_plot).grid(row=5, column=0, columnspan=2, pady=10)

# Matplotlib Figure and Canvas for displaying the plot
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
