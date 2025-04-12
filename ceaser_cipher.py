import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Logic
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Button Actions
def encrypt_action():
    try:
        shift = int(shift_entry.get())
        text = input_entry.get("1.0", tk.END).strip()
        encrypted = encrypt(text, shift)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, encrypted)
    except:
        messagebox.showerror("Error", "Please enter a valid shift number.")

def decrypt_action():
    try:
        shift = int(shift_entry.get())
        text = input_entry.get("1.0", tk.END).strip()
        decrypted = decrypt(text, shift)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, decrypted)
    except:
        messagebox.showerror("Error", "Please enter a valid shift number.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher - GUI")
root.geometry("500x400")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter Message:", bg="#f0f0f0", font=('Arial', 12)).pack()
input_entry = tk.Text(root, height=4, width=50)
input_entry.pack(pady=5)

tk.Label(root, text="Enter Shift Value (1-25):", bg="#f0f0f0", font=('Arial', 12)).pack()
shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)

tk.Button(root, text="Encrypt", command=encrypt_action, width=20, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt_action, width=20, bg="#2196F3", fg="white").pack(pady=5)

tk.Label(root, text="Output Message:", bg="#f0f0f0", font=('Arial', 12)).pack()
output_entry = tk.Text(root, height=4, width=50)
output_entry.pack(pady=5)

root.mainloop()
