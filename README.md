# PortScanner
Port Scanner for macOS (Python GUI)
Features

- Scan a range of ports on a target.
- Displays detailed results in a scrollable text box.
- Uses multithreading to keep the GUI responsive during scans.
- Provides error messages for invalid inputs or unexpected issues.

Requirements

- Python 3.6 or higher
- `tkinter` library (pre-installed with Python)
- `socket` (standard Python library)

Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/kalilinux013/PortScanner.git
   cd port-scanner
   ```

2. Install dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```
   *(No additional libraries are required for this script.)*

3. Run the application:

   ```bash
   python port_scanner.py
   ```

Usage

1. **Target**: Enter the IP address or hostname of the target machine.
2. **Start Port**: Specify the starting port number.
3. **End Port**: Specify the ending port number.
4. Click on the **Start Scan** button to begin scanning.
5. View the results in the scrollable text box.

Example Output

Scanning 192.168.1.1 from port 20 to 25...
[+] Port 22 is OPEN on 192.168.1.1
[-] Port 21 on 192.168.1.1 timed out.
Scan completed for 192.168.1.1.

Notes

- Ensure that you have permission to scan the target to avoid legal or ethical issues.
- Scanning a large range of ports may take time depending on network conditions and target responsiveness.

Improvements and Contributions
Potential Enhancements:

- Add a "Stop Scan" button.
- Improve exception handling for detailed error reporting.
- Validate IP addresses or hostnames before scanning.
- Enhance thread safety by using `queue.Queue`.

Contributing:
Contributions are welcome! Feel free to submit a pull request or open an issue.
License
This project is licensed under the [MIT License](LICENSE).

---
**Disclaimer**: Use this tool responsibly and only on networks you own or have explicit permission to scan.
