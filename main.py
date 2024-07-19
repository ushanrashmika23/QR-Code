import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    # Get the CSV input from the entry widget
    csv_values = entry.get()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(csv_values)
    qr.make(fit=True)

    qr_image = qr.make_image(fill='black', back_color='white')

    # Convert QR code image to format compatible with Tkinter
    qr_image_tk = ImageTk.PhotoImage(qr_image)

    # Update the label to display the QR code
    qr_label.config(image=qr_image_tk)
    qr_label.image = qr_image_tk  # Keep a reference to avoid garbage collection

def on_generate_button_click():
    csv_values = entry.get()
    if csv_values:
        generate_qr_code()
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

# Create a button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=on_generate_button_click)
generate_button.pack(padx=10, pady=10)

# Create a label to display the generated QR code
qr_label = tk.Label(root)
qr_label.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
