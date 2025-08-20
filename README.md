Python Port Scanner with Banner Grabbing
Project Overview

This is a Python-based port scanner that lets you check for open ports on any IP address or domain and also attempts banner grabbing to identify the services running on those ports.

I built this as part of my cybersecurity journey to create hands-on tools for penetration testing, vulnerability assessment, and automation. Testing it with scanme.nmap.org confirmed that it works perfectly!

 Features

Scan a target IP or domain across common ports (20–1024)

Detect open ports

Perform banner grabbing to identify services like SSH, HTTP, etc.

Includes exception handling for smooth operation

Tools & Technologies

Python 3 (socket module)

Kali Linux

VS Code (code-oss)

 How to Use
- Clone the repository
git clone https://github.com/claret-Cyber/automated-vuln-scanner.git

cd automated-vuln-scanner

- Run the scanner
python3 scanner.py


- Input a target IP or domain (e.g., scanme.nmap.org)

- View the open ports and service banners

 Example Output
Enter target IP/Domain: scanme.nmap.org

[+] Scanning target: scanme.nmap.org

[OPEN] Port 22
    Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13

[OPEN] Port 80
    Banner: HTTP/1.1 400 Bad Request
    Date: Wed, 20 Aug 2025 12:13:18 GMT
    Server: Apache/2.4.7 (Ubuntu)
    Content-Length: 306
    Connection: close
    Content-Type: text/html; charset=iso-8859-1

What We Achieved

Built a Python port scanner that successfully detects open ports on any IP or domain.

Implemented banner grabbing, allowing the tool to identify running services such as SSH and HTTP.

Demonstrated real-world results by scanning scanme.nmap.org, showing open ports and detailed server information.

Gained hands-on experience with socket programming and network protocols.

Learned to structure and run Python projects efficiently in Kali Linux using VS Code.

Strengthened problem-solving skills through handling errors and exceptions gracefully.

Laid the groundwork for extending the tool into an Automated Vulnerability Checker that could cross-reference services with known CVEs.
