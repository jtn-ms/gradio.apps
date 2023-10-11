## Detect OS on a specific IP

```bash
┌──(root㉿9a73a20e769d)-[/app/tools/wesng]
└─# nmap -O 192.168.0.6
Not shown: 990 filtered tcp ports (no-response)
PORT     STATE  SERVICE
53/tcp   closed domain
80/tcp   open   http
135/tcp  open   msrpc
139/tcp  open   netbios-ssn
445/tcp  open   microsoft-ds
2179/tcp open   vmrdp
3389/tcp open   ms-wbt-server
6666/tcp open   irc
7070/tcp open   realserver
8080/tcp open   http-proxy
Device type: WAP
Running (JUST GUESSING): Linux 2.6.X|2.4.X (86%)
OS CPE: cpe:/o:linux:linux_kernel:2.6.22 cpe:/o:linux:linux_kernel:2.4
Aggressive OS guesses: OpenWrt Kamikaze 7.09 (Linux 2.6.22) (86%), OpenWrt 0.9 - 7.09 (Linux 2.4.30 - 2.4.34) (85%), OpenWrt White Russian 0.9 (Linux 2.4.30) (85%)
No exact OS matches for host (test conditions non-ideal).

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .        
Nmap done: 1 IP address (1 host up) scanned in 20.30 seconds
```

## How to use nmap to detect my OS

Nmap is a versatile network scanning tool that can be used to detect the operating system of a target host. Nmap uses a variety of techniques and signatures to perform OS detection. Here's how you can use Nmap to detect the OS of a target host:

Important: Always obtain proper authorization before scanning a network or system that you don't own or have permission to test.

Install Nmap:

If you haven't already, install Nmap on your system. You can download and install it from the official Nmap website (https://nmap.org/download.html) or by using your system's package manager.

Run an OS Detection Scan:

To perform an OS detection scan, use the -O option followed by the target IP address or hostname. For example:

```bash
nmap -O <target_ip>
```

Replace <target_ip> with the IP address or hostname of the target you want to scan.

Review the Results:

Nmap will initiate the OS detection scan and display the results. It will provide information about the probable operating system based on the responses it receives from the target host.

The output will include information such as the OS family (e.g., Windows, Linux, macOS), the likelihood of accuracy, and any specific details about the OS version if it can be determined.

Example output:

```bash
Nmap scan report for <target_ip>
Host is up (0.045s latency).
Not shown: 991 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
Device type: general purpose
Running: Microsoft Windows XP|7
OS CPE: cpe:/o:microsoft:windows_xp::sp3 cpe:/o:microsoft:windows_7
OS details: Microsoft Windows XP SP3, Windows 7 SP1, or Windows Server 2012
In this example, Nmap has identified the target as running Microsoft Windows XP SP3, Windows 7 SP1, or Windows Server 2012.
```


Keep in mind that while Nmap is a powerful tool for OS detection, it may not always provide accurate results, especially if the target host is configured to intentionally hide its OS characteristics. Additionally, Nmap may require root or administrator privileges to perform certain types of OS detection. Always use Nmap responsibly and with proper authorization.