# Python Port Scanner

This is a simple Python-based port scanner script that scans a range of ports on a specified target IP address. It uses the `socket` library to check if a port is open by attempting to establish a connection.

## Features

- Scans ports within a specified range (50 to 85 by default).
- Displays information about the target IP and the time the scan started.
- Shows open ports in the specified range.
- Handles common errors, including invalid arguments, unreachable hosts, and interrupted scans.

## Requirements

- **Python 3.x**
  - This script is written in Python 3, so ensure it is installed.
  - Required libraries: `socket`, `sys`, `datetime` (all are included in Python's standard library).

## Usage

### Syntax

```bash
python3 scanner.py <IP Address>
```

### Example

  To scan a target at IP address 192.168.1.1, run:

```bash
python3 scanner.py 192.168.1.1
```
### Output

  The output will display:

  - A banner showing the target IP and the start time of the scan.
  - Open ports in the specified range (e.g., "Port 80 is open").

### Sample Output

```bash
--------------------------------------------------
Scanning Target 192.168.1.1
Time Started: 2023-11-05 13:25:36.123456
--------------------------------------------------
Port 80 is open
Port 53 is open
```

## How It Works

  - Target Definition: The target IP address is specified as a command-line argument. The script converts the domain name to an IP address if a hostname     is given.
  - Port Scanning: It attempts to connect to each port within the range 50-85 using TCP. If a port is open, it prints the port number.
  
### Error Handling
  - If the user doesn’t provide an IP, it shows syntax instructions.
  - Handles cases for unreachable hosts, connectivity issues, and script interruptions (e.g., Ctrl+C).

### Important Notes

  Permission: Ensure you have permission to scan any network or IP. Unauthorized scanning may violate terms of service and is generally illegal without    consent.
  Port Range: The default range is 50-85. You can modify the for port in range(50,85): line in the code to scan other ranges.

## Disclaimer
  
  This script is intended for educational and authorized network testing purposes only. Ensure you have proper authorization before running this script    on any network.
