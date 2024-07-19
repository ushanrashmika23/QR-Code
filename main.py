import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_codes():
    # Clear previous QR codes
    for widget in qr_frame.winfo_children():
        widget.destroy()
    
    # Get the CSV input from the entry widget
    csv_values = entry.get()
    values = [value.strip() for value in csv_values.split(',')]

    for value in values:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(value)
        qr.make(fit=True)

        qr_image = qr.make_image(fill='black', back_color='white')
        qr_image_tk = ImageTk.PhotoImage(qr_image)

        # Create a label for the QR code
        qr_code_label = tk.Label(qr_frame, image=qr_image_tk)
        qr_code_label.image = qr_image_tk  # Keep a reference to avoid garbage collection
        qr_code_label.pack(pady=5)

        # Create a label for the meaning
        meaning_label = tk.Label(qr_frame, text=value)
        meaning_label.pack(pady=5)

def on_generate_button_click():
    csv_values = entry.get()
    if csv_values:
        generate_qr_codes()
    else:
        messagebox.showwarning("Input Error", "Please enter comma-separated values.")

# Create the main window
root = tk.Tk()
root.title("CSV to QR Code Generator")

# Create a label and entry to get CSV input from the user
label = tk.Label(root, text="Enter comma-separated values:")
label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Create a button to generate the QR codes
generate_button = tk.Button(root, text="Generate QR Codes", command=on_generate_button_click)
generate_button.pack(padx=10, pady=10)

# Create a frame to display the generated QR codes
qr_frame = tk.Frame(root)
qr_frame.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
