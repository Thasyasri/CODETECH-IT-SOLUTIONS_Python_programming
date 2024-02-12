import tkinter as tk

# Function to update the entry widget with the clicked button value
def button_click(symbol):
    current = entry_display.get()
    if symbol == 'C':
        entry_display.delete(0, tk.END)
    elif symbol == '=':
        try:
            result = eval(current)
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, str(result))
        except Exception as e:
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, "Error")
    else:
        entry_display.insert(tk.END, symbol)

# Create main application window
root = tk.Tk()
root.title("Calculator")

# Create and place entry widget for displaying calculations
entry_display = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button symbols and their positions on the calculator
button_symbols = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create and place buttons
for symbol, row, column in button_symbols:
    button = tk.Button(root, text=symbol, padx=20, pady=20, font=("Arial", 14),
                       command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=column, padx=5, pady=5)

# Run the main event loop
root.mainloop()
