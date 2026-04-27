import customtkinter as ctk
from tkinter import messagebox

# Theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Encryption function
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Decryption function
def decrypt(text, shift):
    return encrypt(text, -shift)

# Process function
def process():
    message = text_box.get("1.0", "end").strip()

    if message == placeholder or message == "":
        messagebox.showerror("Error", "Please enter a valid message!")
        return

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be a number!")
        return

    if mode.get() == "Encrypt":
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)

    output_box.delete("1.0", "end")
    output_box.insert("1.0", result)

# Copy result
def copy_result():
    result = output_box.get("1.0", "end").strip()
    if result == "":
        messagebox.showerror("Error", "Nothing to copy!")
        return
    app.clipboard_clear()
    app.clipboard_append(result)
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# Placeholder functions
def add_placeholder():
    if text_box.get("1.0", "end").strip() == "":
        text_box.insert("1.0", placeholder)
        text_box.configure(text_color="gray")

def remove_placeholder(event):
    if text_box.get("1.0", "end").strip() == placeholder:
        text_box.delete("1.0", "end")
        text_box.configure(text_color="white")

# App window
app = ctk.CTk()
app.title("🔐 Caesar Cipher Tool")
app.geometry("500x520")

# Title
title = ctk.CTkLabel(app, text="Caesar Cipher Tool", font=("Arial", 22, "bold"))
title.pack(pady=15)

# Input box with placeholder
text_box = ctk.CTkTextbox(app, height=100, width=420)
text_box.pack(pady=10)

placeholder = "Enter your message here..."
add_placeholder()

text_box.bind("<FocusIn>", remove_placeholder)
text_box.bind("<FocusOut>", lambda e: add_placeholder())

# Shift input
shift_entry = ctk.CTkEntry(app, placeholder_text="Enter shift value")
shift_entry.pack(pady=10)

# Mode selection
mode = ctk.StringVar(value="Encrypt")

frame = ctk.CTkFrame(app)
frame.pack(pady=10)

ctk.CTkRadioButton(frame, text="Encrypt", variable=mode, value="Encrypt").pack(side="left", padx=10)
ctk.CTkRadioButton(frame, text="Decrypt", variable=mode, value="Decrypt").pack(side="left", padx=10)

# Buttons
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=15)

process_btn = ctk.CTkButton(btn_frame, text="Process", command=process)
process_btn.pack(side="left", padx=10)

copy_btn = ctk.CTkButton(btn_frame, text="Copy", command=copy_result)
copy_btn.pack(side="left", padx=10)

# Output box
output_box = ctk.CTkTextbox(app, height=100, width=420)
output_box.pack(pady=10)

# Run app
app.mainloop()
