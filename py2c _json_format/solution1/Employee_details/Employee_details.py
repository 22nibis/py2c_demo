import array
import socket
import json
import tkinter as tk
from tkinter import messagebox
from tokenize import Double

# Server IP and port
SERVER_IP = '127.0.0.1'  # Change this if needed
SERVER_PORT = 8080

# Function to send JSON data to the server
def send_data():
    # Retrieve data from entry fields
    name = name_entry.get()
    age = age_entry.get()
    height = height_entry.get()
    scores = scores_entry.get().split(',')
    addrs = address_entry.get()

    # Validate input data
    if not name or not age or not height or not scores or not addrs:
        messagebox.showerror("Input Error", "All fields must be filled out.")
        return

    # Create JSON data
    data = {
        "name": name,
        "age": int(age),
        "height": height,
        "scores":scores,
        "addrs": addrs
    }

    # Convert to JSON format
    json_data = json.dumps(data)

    try:
        # Create a socket and connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_IP, SERVER_PORT))
            sock.sendall(json_data.encode('utf-8'))
            messagebox.showinfo("Success", "Data sent to the server successfully.")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to connect to server: {e}")

# Create the main application window
app = tk.Tk()
app.title("JSON Data Sender")

# Create UI labels and entry fields
tk.Label(app, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Age:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(app)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Height:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
height_entry = tk.Entry(app)
height_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="Scores(comma-separated):").grid(row=3, column=0, padx=10, pady=10, sticky="e")
scores_entry = tk.Entry(app)
scores_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(app, text="Address:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
address_entry = tk.Entry(app)
address_entry.grid(row=4, column=1, padx=10, pady=10)

# Send Data button
send_button = tk.Button(app, text="Send Data", command=send_data)
send_button.grid(row=5, column=0, columnspan=2, pady=20)

# Start the GUI loop
app.mainloop()