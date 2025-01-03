import tkinter as tk
from tkinter import messagebox


# Function to handle button clicks
def on_button_click(label):
    if label == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
    elif label == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, label)


# Create the main application window
root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg="black")
root.geometry("400x500")  # Set the window size

# Input Field
entry = tk.Entry(root, font=("Arial", 18), bg="#000000", fg="white", justify="right", bd=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Button Labels
button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create Buttons Dynamically
row, col = 1, 0
for label in button_labels:
    button = tk.Button(root, text=label, font=("Arial", 16, "bold"), bg="#a65ef1", fg="#8e46d6",
                       activebackground="#8e46d6", activeforeground="#a65ef1",
                       relief="ridge", bd=2, command=lambda lbl=label: on_button_click(lbl))
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        row += 1

# Adjust row and column weights for responsiveness
for i in range(5):  # 5 rows (1 for input field + 4 for buttons)
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns for buttons
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
