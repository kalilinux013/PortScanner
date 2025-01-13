import tkinter as tk
from tkinter import messagebox, scrolledtext
import socket
import threading

# Function to scan a specific port
def scan_port(ipaddress, port, result_box):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)
		sock.connect((ipaddress, port))
		result_box.insert(tk.END, f"[+] Port {port} is OPEN on {ipaddress}\n")
		sock.close()
	except socket.timeout:
		result_box.insert(tk.END, f"[-] Port {port} on {ipaddress} timed out.\n")
	except:
		pass  # Ignore other errors

# Function to scan a range of ports on a target
def scan_ports(target, start_port, end_port, result_box):
	result_box.insert(tk.END, f"Scanning {target} from port {start_port} to {end_port}...\n")
	for port in range(start_port, end_port + 1):
		scan_port(target, port, result_box)
	result_box.insert(tk.END, f"Scan completed for {target}.\n\n")

# Function to start scanning (called when "Start Scan" is clicked)
def start_scan():
	target = target_entry.get().strip()
	try:
		start_port = int(start_port_entry.get().strip())
		end_port = int(end_port_entry.get().strip())
	except ValueError:
		messagebox.showerror("Input Error", "Ports must be valid numbers.")
		return

	if not target:
		messagebox.showerror("Input Error", "Please enter a target address.")
		return

	if start_port > end_port:
		messagebox.showerror("Input Error", "Start port must be less than or equal to end port.")
		return

	result_box.delete(1.0, tk.END)  # Clear previous results

	# Run the scan in a separate thread to keep the GUI responsive
	threading.Thread(target=scan_ports, args=(target, start_port, end_port, result_box)).start()

# GUI Setup
root = tk.Tk()
root.title("Port Scanner for macOS")
root.geometry("600x400")

# Target Entry
tk.Label(root, text="Target (IP/Hostname):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
target_entry = tk.Entry(root, width=40)
target_entry.grid(row=0, column=1, padx=10, pady=5)

# Start Port Entry
tk.Label(root, text="Start Port:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
start_port_entry = tk.Entry(root, width=10)
start_port_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# End Port Entry
tk.Label(root, text="End Port:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
end_port_entry = tk.Entry(root, width=10)
end_port_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Scan Button
scan_button = tk.Button(root, text="Start Scan", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2, pady=10)

# Results Box
result_box = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD)
result_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
