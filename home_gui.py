import tkinter as tk
import subprocess
import threading
import qr_code_scanner

# Create the main Tkinter window
window = tk.Tk()
window.title("Welcome to campus entrance")
window.geometry("800x600")

# Configure a custom color scheme
bg_color = "#fedfeb"
button_bg_color = "#e0218a"
button_fg_color = "#000000"

window.configure(bg=bg_color)

# Function to stop the QR code scanning
def stop_scan():
    qr_code_scanner.scanning = False

# Function to open the 'showit.py' file
def open_showit():
    subprocess.run(["python", "NoUniqueShow.py"])

# Function to open a duplicate of the 'NoUniqueShow.py' file
def open_duplicate():
    subprocess.run(["python", "uniqueShow.py"])

# Define the font for the button text
button_font = ("Arial", 16, "bold")

# Create a button to start the QR code scanning
scan_button = tk.Button(window, text="Scan QR Code", command=lambda: threading.Thread(target=qr_code_scanner.scan_qr_code).start(), bg=button_bg_color, fg=button_fg_color, width=19, height=2, font=button_font)
scan_button.pack(pady=20)

# Create a button to stop the QR code scanning
stop_button = tk.Button(window, text="Stop", command=stop_scan, bg=button_bg_color, fg=button_fg_color, width=19, height=2, font=button_font)
stop_button.pack(pady=20)

# Create a button to open the 'showit.py' file
showit_button = tk.Button(window, text="Users but looping", command=open_showit, bg=button_bg_color, fg=button_fg_color, width=19, height=2, font=button_font)
showit_button.pack(pady=20)

# Create a button to open a duplicate of the 'NoUniqueShow.py' file
duplicate_button = tk.Button(window, text="Users at diff timestamp", command=open_duplicate, bg=button_bg_color, fg=button_fg_color, width=20, height=3, font=button_font)
duplicate_button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
