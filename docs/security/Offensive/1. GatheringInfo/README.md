## Info Category

- domainName2ipAddr: ping
- ipAddr2openPorts: nmap
- ipAddr2osInfo: using nmap with custom scripts
- ipAddr2vulnerabilities: rapidscan, vulscan, nuclei, sniper, ...
- ipAddr2userNames: accessing /etc/shadow using exploiting mysql backdoor

## Examples

- [x] [`nmap -sV --script=vulscan/vulscan.nse  192.168.0.14`](https://github.com/scipag/vulscan)
- [ ] `nmap -p0-65535 192.168.0.14`
- [x] [python3 rapidscan.py 192.168.0.14](https://github.com/skavngr/rapidscan)
- `nuclei -u 192.168.0.14`
- `wapiti -u 192.168.0.14`
- `whatweb github.com`
- `webanalyze -host www.github.com  -crawl 1`
- `seoanalyze https://www.sethserver.com/ -f html > results.html`
- [`python3 nettacker.py -i 192.168.0.14 -m all -t 5`](https://github.com/OWASP/Nettacker)


## Logs

```sh
  /__)_   ●_/(  _ _
                                / ( (//)/(/__)( (//)
                                     /
                     (The Multi-Tool Web Vulnerability Scanner)

                     Check out our new software, NetBot for simulating DDoS attacks - https://github.com/skavngr/netbot


[ Checking Available Security Scanning Tools Phase... Initiated. ]
        Some of these tools ['dirb', 'uniscan', 'xsser', 'amass', 'dnswalk', 'sslyze', 'dmitry', 'fierce', 'dnsmap', 'lbd', 'golismero', 'davtest'] are unavailable or will be skipped. RapidScan will still perform the rest of the tests. Install these tools to fully utilize the functionality of RapidScan.
[ Checking Available Security Scanning Tools Phase... Completed. ]


[ Preliminary Scan Phase Initiated... Loaded 80 vulnerability checks. ]
[● < 15s] Deploying 1/80 | Nmap - Checks for ORACLE DB

Scan Completed in 14s

[● < 30s] Deploying 2/80 | Golismero Zone Transfer - Attempts Zone Transfer.    

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 3/80 | DMitry - Passively Harvests Subdomains from the Domain.

Scanning Tool Unavailable. Skipping Test...

[● < 15s] Deploying 4/80 | Host - Checks for existence of IPV6 address.

Scan Completed in 1s

[● <  2m] Deploying 5/80 | Uniscan - Brutes for Filenames on the Domain.        

Scanning Tool Unavailable. Skipping Test...

[● < 75m] Deploying 6/80 | Fierce Subdomains Bruter - Brute Forces Subdomain Discovery.

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 7/80 | Nikto - Checks the Domain Headers.

Scan Completed in 41s

[● < 40s] Deploying 8/80 | Nmap - Checks for IIS WebDAV

Scan Completed in 14s

[● < 45m] Deploying 9/80 | Nmap [Slowloris DoS] - Checks for Slowloris Denial of Service Vulnerability.

Scan Completed in 1m 44s

Vulnerability Threat Level
         critical  Vulnerable to Slowloris Denial of Service.
Vulnerability Definition
        This attack works by opening multiple simultaneous connections to the web server and it keeps them alive as long as possible by continously sending partial HTTP requests, which never gets completed. They easily slip through IDS by sending partial requests.
Vulnerability Remediation
        If you are using Apache Module, `mod_antiloris` would help. For other setup you can find more detailed remediation on this resource. https://www.acunetix.com/blog/articles/slow-http-dos-attacks-mitigate-apache-http-server/
[● < 30s] Deploying 10/80 | Nmap - Checks for SNMP Service

Scan Completed in 14s

Vulnerability Threat Level
         medium  SNMP Service Detected.
Vulnerability Definition
        Hackers will be able to read community strings through the service and enumerate quite a bit of information from the target. Also, there are multiple Remote Code Execution and Denial of Service vulnerabilities related to SNMP services.
Vulnerability Remediation
        Use a firewall to block the ports from the outside world. The following article gives wide insight on locking down SNMP service. https://www.techrepublic.com/article/lock-it-down-dont-allow-snmp-to-compromise-network-security/      
[● < 30s] Deploying 11/80 | ASP.Net Misconfiguration - Checks for ASP.Net Misconfiguration.

Scan Completed in 22s

[● < 30s] Deploying 12/80 | Drupal Checker - Checks for Drupal Installation.    

Scan Completed in 22s

[● <  9m] Deploying 13/80 | Uniscan - Checks for XSS, SQLi, BSQLi & Other Checks.

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 14/80 | Nikto - Checks for HTTP PUT DEL.

Scan Completed in 41s

[● < 35s] Deploying 15/80 | Nikto - Performs SSL Checks.

Scan Completed in 41s

[● < 35m] Deploying 16/80 | DirB - Brutes the target for Open Directories.      

Scanning Tool Unavailable. Skipping Test...

[● < 30s] Deploying 17/80 | WordPress Checker - Checks for WordPress Installation.

Scan Completed in 22s

[● < 30m] Deploying 18/80 | DNSMap - Brutes Subdomains.

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 19/80 | Nmap [POODLE] - Checks only for Poodle Vulnerability.

Scan Completed in 12s

[● < 45s] Deploying 20/80 | Golismero - SQLMap [Retrieves only the DB Banner]   

Scanning Tool Unavailable. Skipping Test...

[● > 75m] Deploying 21/80 | Nmap - Performs a Full UDP Port Scan

Scan Completed in 14m 8s

Vulnerability Threat Level
         low  UDP Ports are Open
Vulnerability Definition
        Open Ports give attackers a hint to exploit the services. Attackers try to retrieve banner information through the ports and understand what type of service the host is running
Vulnerability Remediation
        It is recommended to close the ports of unused services and use a firewall to filter the ports wherever necessary. This resource may give more insights. https://security.stackexchange.com/a/145781/6137
[● < 15s] Deploying 22/80 | Nmap - Checks for Remote Desktop Service over UDP   

Scan Completed in 14s

Vulnerability Threat Level
         high  RDP Server Detected over UDP.
Vulnerability Definition
        Attackers may launch remote exploits to either crash the service or tools like ncrack to try brute-forcing the password on the target.
Vulnerability Remediation
        It is recommended to block the service to outside world and made the service accessible only through the a set of allowed IPs only really neccessary. The following resource provides insights on the risks and as well as the steps to block the service. https://www.perspectiverisk.com/remote-desktop-service-vulnerabilities/
[● < 30m] Deploying 23/80 | Golismero Subdomains Bruter - Brute Forces Subdomain Discovery.

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 24/80 | Nikto - Checks for Shellshock Bug.

Scan Completed in 41s

[● < 35s] Deploying 25/80 | Nmap [LOGJAM] - Checks for LOGJAM Vulnerability.    

Scan Completed in 12s

[● < 35s] Deploying 26/80 | Nikto - Enumerates CGI Directories.

Scan Completed in 41s

[● < 40s] Deploying 27/80 | Uniscan - Checks for robots.txt & sitemap.xml       

Scanning Tool Unavailable. Skipping Test...

[● < 15s] Deploying 28/80 | Nmap [FTP] - Checks if FTP service is running.      

Scan Completed in 14s

[● <  8m] Deploying 29/80 | Uniscan - Checks for LFI, RFI and RCE.

Scanning Tool Unavailable. Skipping Test...

[● < 30s] Deploying 30/80 | Joomla Checker - Checks for Joomla Installation.    

Scan Completed in 22s

[● < 20s] Deploying 31/80 | Checks for SMB Service over UDP

Scan Completed in 15s

[● < 15s] Deploying 32/80 | Nmap - Checks for Remote Desktop Service over TCP   

Scan Completed in 1s

Vulnerability Threat Level
         high  RDP Server Detected over TCP.
Vulnerability Definition
        Attackers may launch remote exploits to either crash the service or tools like ncrack to try brute-forcing the password on the target.
Vulnerability Remediation
        It is recommended to block the service to outside world and made the service accessible only through the a set of allowed IPs only really neccessary. The following resource provides insights on the risks and as well as the steps to block the service. https://www.perspectiverisk.com/remote-desktop-service-vulnerabilities/
[● < 30s] Deploying 33/80 | SSLyze - Checks for Session Resumption Support with [Session IDs/TLS Tickets].

Scanning Tool Unavailable. Skipping Test...

[● < 30s] Deploying 34/80 | Nmap [Heartbleed] - Checks only for Heartbleed Vulnerability.

Scan Completed in 16s

[● < 30s] Deploying 35/80 | DMitry - Passively Harvests Emails from the Domain. 

Scanning Tool Unavailable. Skipping Test...

[● < 20s] Deploying 36/80 | DNSRecon - Attempts Multiple Zone Transfers on Nameservers.

Scan Completed in 10s

[● < 25s] Deploying 37/80 | WHOis - Checks for Administrator's Contact Information.

Scan Completed in 1s

[● < 20s] Deploying 38/80 | Checks for SMB Service over TCP

Scan Completed in 13s

Vulnerability Threat Level
         medium  SMB Ports are Open over TCP
Vulnerability Definition
        Cyber Criminals mainly target this service as it is very easier for them to perform a remote attack by running exploits. WannaCry Ransomware is one such example.
Vulnerability Remediation
        Exposing SMB Service to the outside world is a bad idea, it is recommended to install latest patches for the service in order not to get compromised. The following resource provides a detailed information on SMB Hardening concepts. https://kb.iweb.com/hc/en-us/articles/115000274491-Securing-Windows-SMB-and-NetBios-NetBT-Services
[● < 30s] Deploying 39/80 | WebDAV - Checks if WEBDAV enabled on Home directory.

Scanning Tool Unavailable. Skipping Test...

[● < 45s] Deploying 40/80 | Golismero SSL Scans - Performs SSL related Scans.   

Scanning Tool Unavailable. Skipping Test...

[● < 20s] Deploying 41/80 | Nmap [STUXNET] - Checks if the host is affected by STUXNET Worm.

Scan Completed in 1s

Vulnerability Threat Level
         critical  Vulnerable to STUXNET.
Vulnerability Definition
        The StuxNet is level-3 worm that exposes critical information of the target organization. It was a cyber weapon that was designed to thwart the nuclear intelligence of Iran. Seriously wonder how it got here? Hope this isn't a false positive Nmap ;)
Vulnerability Remediation
        It is highly recommended to perform a complete rootkit scan on the host. For more information refer to this resource. https://www.symantec.com/security_response/writeup.jsp?docid=2010-071400-3123-99&tabid=3
[● > 50m] Deploying 42/80 | Nmap - Performs a Full TCP Port Scan

Scan Completed in 11m 57s

Vulnerability Threat Level
         low  TCP Ports are Open
Vulnerability Definition
        Open Ports give attackers a hint to exploit the services. Attackers try to retrieve banner information through the ports and understand what type of service the host is running
Vulnerability Remediation
        It is recommended to close the ports of unused services and use a firewall to filter the ports wherever necessary. This resource may give more insights. https://security.stackexchange.com/a/145781/6137
[● < 40s] Deploying 43/80 | Golismero - BruteForces for certain directories on the Domain.

Scanning Tool Unavailable. Skipping Test...

[● < 15s] Deploying 44/80 | Nmap [TELNET] - Checks if TELNET service is running.

Scan Completed in 14s

[● < 35s] Deploying 45/80 | Nikto - Checks for HTTP Options on the Domain.      

Scan Completed in 41s

[● < 40s] Deploying 46/80 | SSLyze - Checks only for Heartbleed Vulnerability.  

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 47/80 | Nikto - Checks for Server Issues.

Scan Completed in 41s

[● < 30s] Deploying 48/80 | Checks for ASP.net Elmah Logger

Scan Completed in 22s

[● < 35s] Deploying 49/80 | Nikto - Checks for Apache Expect XSS Header.        

Scan Completed in 41s

[● <  9m] Deploying 50/80 | Uniscan - Stress Tests the Domain.

Scanning Tool Unavailable. Skipping Test...

[● < 45s] Deploying 51/80 | DNSEnum - Attempts Zone Transfer.

Scan Completed in 46s

[● < 35s] Deploying 52/80 | Nikto - Brutes Subdomains.

Scan Completed in 41s

[● < 40s] Deploying 53/80 | Golismero - Checks only for Heartbleed Vulnerability.

Scanning Tool Unavailable. Skipping Test...

[● <  2m] Deploying 54/80 | Nmap - Fast Scan [Only Few Port Checks]

Scan Completed in 14s

Vulnerability Threat Level
         low  Some ports are open. Perform a full-scan manually.
Vulnerability Definition
        Open Ports give attackers a hint to exploit the services. Attackers try to retrieve banner information through the ports and understand what type of service the host is running
Vulnerability Remediation
        It is recommended to close the ports of unused services and use a firewall to filter the ports wherever necessary. This resource may give more insights. https://security.stackexchange.com/a/145781/6137
[● < 25s] Deploying 55/80 | SSLyze - Checks for Secure Renegotiation Support and Client Renegotiation.

Scanning Tool Unavailable. Skipping Test...

[● < 15s] Deploying 56/80 | Nmap - Checks for MySQL DB

Scan Completed in 3s

[● <  5m] Deploying 57/80 | Uniscan - Brutes Directories on the Domain.

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 58/80 | Nmap [OpenSSL CCS Injection] - Checks only for CCS Injection.

Scan Completed in 1s

[● < 35s] Deploying 59/80 | DNSWalk - Attempts Zone Transfer.

Scanning Tool Unavailable. Skipping Test...

[● < 45s] Deploying 60/80 | Golismero - Checks if the domain is spoofed or hijacked.

Scanning Tool Unavailable. Skipping Test...

[● <  3m] Deploying 61/80 | The Harvester - Scans for emails using Google's passive search.

Scan Completed in 1s

[● < 15m] Deploying 62/80 | AMass - Brutes Domain for Subdomains

Scanning Tool Unavailable. Skipping Test...

[● < 20s] Deploying 63/80 | Nmap [XSS Filter Check] - Checks if XSS Protection Header is present.

Scan Completed in 14s

[● <  4m] Deploying 64/80 | XSSer - Checks for Cross-Site Scripting [XSS] Attacks.

Scanning Tool Unavailable. Skipping Test...

[● < 15s] Deploying 65/80 | Nmap - Checks for MS-SQL Server DB

Scan Completed in 3s

[● < 15s] Deploying 66/80 | Golismero - Does a fingerprint on the Domain.       

Scanning Tool Unavailable. Skipping Test...

[● < 45s] Deploying 67/80 | Golismero - BruteForces for certain files on the Domain.

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 68/80 | Nikto - Checks if Server is Outdated.

Scan Completed in 41s

[● <  4m] Deploying 69/80 | LBD - Checks for DNS/HTTP Load Balancers.

Scanning Tool Unavailable. Skipping Test...

[● < 35s] Deploying 70/80 | Nikto - Checks for any interesting files on the Domain.

Scan Completed in 41s

[● < 5m] Deploying 71/80 | Wapiti - Checks for SQLi, RCE, XSS and Other Vulnerabilities

Scan Completed in 2s

[● <  4m] Deploying 72/80 | Golismero Nikto Scans - Uses Nikto Plugin to detect vulnerabilities.

Scanning Tool Unavailable. Skipping Test...

[● < 45s] Deploying 73/80 | Wafw00f - Checks for Application Firewalls.

Scan Completed in 1s

Vulnerability Threat Level
         medium  No Web Application Firewall Detected
Vulnerability Definition
        Without a Web Application Firewall, An attacker may try to inject various attack patterns either manually or using automated scanners. An automated scanner may send hordes of attack vectors and patterns to validate an attack, there are also chances for the application to get DoS`ed (Denial of Service)
Vulnerability Remediation
        Web Application Firewalls offer great protection against common web attacks like XSS, SQLi, etc. They also provide an additional line of defense to your security infrastructure. This resource contains information on web application firewalls that could suit your application. https://www.gartner.com/reviews/market/web-application-firewall
[● < 30s] Deploying 74/80 | SSLyze - Checks for ZLib Deflate Compression.       

Scanning Tool Unavailable. Skipping Test...

[● < 30s] Deploying 75/80 | Nmap [FREAK] - Checks only for FREAK Vulnerability. 

Scan Completed in 13s

Vulnerability Threat Level
         high  FREAK Vulnerability Detected.
Vulnerability Definition
        With this vulnerability the attacker will be able to perform a MiTM attack and thus compromising the confidentiality factor.
Vulnerability Remediation
        Upgrading OpenSSL to latest version will mitigate this issue. Versions prior to 1.1.0 is prone to this vulnerability. More information can be found in this resource. https://bobcares.com/blog/how-to-fix-sweet32-birthday-attacks-vulnerability-cve-2016-2183/
[● < 35s] Deploying 76/80 | Nikto - Checks for MS10-070 Vulnerability.

Scan Completed in 41s

[● < 25s] Deploying 77/80 | SSLyze - Checks for OCSP Stapling.

Scanning Tool Unavailable. Skipping Test...

[● < 3m] Deploying 78/80 | WhatWeb - Checks for X-XSS Protection Header

Scan Completed in 16s

Vulnerability Threat Level
         medium  X-XSS Protection is not Present
Vulnerability Definition
        As the target is lacking this header, older browsers will be prone to Reflected XSS attacks.
Vulnerability Remediation
        Modern browsers does not face any issues with this vulnerability (missing headers). However, older browsers are strongly recommended to be upgraded.    
[● < 35s] Deploying 79/80 | Nikto - Checks for Internal IP Leak.

Scan Completed in 41s

[● < 35s] Deploying 80/80 | Nikto - Checks for Injectable Paths.

Scan Completed in 41s

[ Preliminary Scan Phase Completed. ]


[ Report Generation Phase Initiated. ]
        Complete Vulnerability Report for 192.168.0.14 named rs.vul.192.168.0.14.2023-10-11 is available under the same directory RapidScan resides.
        Total Number of Vulnerability Checks        : 80
        Total Number of Vulnerability Checks Skipped: 31
        Total Number of Vulnerabilities Detected    : 12
        Total Time Elapsed for the Scan             : 43m 22s


        For Debugging Purposes, You can view the complete output generated by all the tools named rs.dbg.192.168.0.14.2023-10-11 under the same directory.      
[ Report Generation Phase Completed. ]
```



```sh
┌──(root㉿docker-desktop)-[/app/collections/vulnerability.scan]    
└─# nmap -sV --script=vulscan/vulscan.nse  192.168.0.14
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-10-11 18:48 UTC 
Nmap scan report for 192.168.0.14
Host is up (0.0093s latency).
Not shown: 987 filtered tcp ports (no-response)
PORT     STATE  SERVICE            VERSION
53/tcp   closed domain
135/tcp  open   msrpc              Microsoft Windows RPC
| vulscan: VulDB - https://vuldb.com:
| No findings
|
| MITRE CVE - https://cve.mitre.org:
| No findings
|
| SecurityFocus - https://www.securityfocus.com/bid/:
| No findings
|
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| No findings
|
| Exploit-DB - https://www.exploit-db.com:
| No findings
|
| OpenVAS (Nessus) - http://www.openvas.org:
| No findings
|
| SecurityTracker - https://www.securitytracker.com:
| No findings
|
| OSVDB - http://www.osvdb.org:
| No findings
|_
139/tcp  open   netbios-ssn        Microsoft Windows netbios-ssn   
| vulscan: VulDB - https://vuldb.com:
| No findings
|
| MITRE CVE - https://cve.mitre.org:
| No findings
|
| SecurityFocus - https://www.securityfocus.com/bid/:
| No findings
|
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| No findings
|
| Exploit-DB - https://www.exploit-db.com:
| No findings
|
| OpenVAS (Nessus) - http://www.openvas.org:
| No findings
|
| SecurityTracker - https://www.securitytracker.com:
| No findings
|
| OSVDB - http://www.osvdb.org:
| No findings
|_
443/tcp  open   ssl/http           Apache httpd
|_http-server-header: Apache
| vulscan: VulDB - https://vuldb.com:
| No findings
|
| MITRE CVE - https://cve.mitre.org:
| No findings
|
| SecurityFocus - https://www.securityfocus.com/bid/:
| No findings
|
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| No findings
|
| Exploit-DB - https://www.exploit-db.com:
| No findings
|
| OpenVAS (Nessus) - http://www.openvas.org:
| No findings
|
| SecurityTracker - https://www.securitytracker.com:
| No findings
|
| OSVDB - http://www.osvdb.org:
| No findings
|_
445/tcp  open   microsoft-ds?
902/tcp  open   ssl/vmware-auth    VMware Authentication Daemon 1.10 (Uses VNC, SOAP)
| vulscan: VulDB - https://vuldb.com:
| No findings
|
| MITRE CVE - https://cve.mitre.org:
| No findings
|
| SecurityFocus - https://www.securityfocus.com/bid/:
| No findings
|
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| No findings
|
| Exploit-DB - https://www.exploit-db.com:
| No findings
|
| OpenVAS (Nessus) - http://www.openvas.org:
| No findings
|
| SecurityTracker - https://www.securitytracker.com:
| No findings
|
| OSVDB - http://www.osvdb.org:
| No findings
|_
912/tcp  open   vmware-auth        VMware Authentication Daemon 1.0 (Uses VNC, SOAP)
| vulscan: VulDB - https://vuldb.com:
| No findings
|
| MITRE CVE - https://cve.mitre.org:
| No findings
|
| SecurityFocus - https://www.securityfocus.com/bid/:
| No findings
|
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| No findings
|
| Exploit-DB - https://www.exploit-db.com:
| No findings
|
| OpenVAS (Nessus) - http://www.openvas.org:
| No findings
|
| SecurityTracker - https://www.securitytracker.com:
| No findings
|
| OSVDB - http://www.osvdb.org:
| No findings
|_
1947/tcp open   sentinelsrm?
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.0 403 Forbidden
|     Server: HASP LM/25.02
|     Date: Wed, 11 Oct 2023 18:53:01 GMT
|     X-Frame-Options: SAMEORIGIN
|     Strict-Transport-Security: max-age=0;
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: strict-origin
|     Content-Type: text/html
|     Content-Length: 137
|     <title>403 Forbidden</title>
|     <h1>403 Forbidden</h1>
|     Access to this resource has been denied to you.
|     <p>Please contact the administrator.
|   GetRequest:
|     HTTP/1.0 403 Forbidden
|     Server: HASP LM/25.02
|     Date: Wed, 11 Oct 2023 18:52:18 GMT
|     X-Frame-Options: SAMEORIGIN
|     Strict-Transport-Security: max-age=0;
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: strict-origin
|     Content-Type: text/html
|     Content-Length: 137
|     <title>403 Forbidden</title>
|     <h1>403 Forbidden</h1>
|     Access to this resource has been denied to you.
|     <p>Please contact the administrator.
|   HTTPOptions, RTSPRequest:
|     HTTP/0.0 501 Not Implemented
|     Server: HASP LM/25.02
|     Date: Wed, 11 Oct 2023 18:52:18 GMT
|     X-Frame-Options: SAMEORIGIN
|     Strict-Transport-Security: max-age=0;
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: strict-origin
|     Content-Type: text/html
|     Content-Length: 164
|     <title>501 Not Implemented</title>
|     <h1>501 Not Implemented</h1>
|     Your request was not understood or not allowed by this server.
|_    <p>Please contact the administrator.
3389/tcp open   ssl/ms-wbt-server?
5280/tcp open   flexlm             FlexLM license manager
| vulscan: VulDB - https://vuldb.com:
| No findings
|
| MITRE CVE - https://cve.mitre.org:
| No findings
|
| SecurityFocus - https://www.securityfocus.com/bid/:
| No findings
|
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| No findings
|
| Exploit-DB - https://www.exploit-db.com:
| No findings
|
| OpenVAS (Nessus) - http://www.openvas.org:
| No findings
|
| SecurityTracker - https://www.securitytracker.com:
| No findings
|
| OSVDB - http://www.osvdb.org:
| No findings
|_
5357/tcp open   http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
| vulscan: VulDB - https://vuldb.com:
| No findings
|
| MITRE CVE - https://cve.mitre.org:
| No findings
|
| SecurityFocus - https://www.securityfocus.com/bid/:
| No findings
|
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| No findings
|
| Exploit-DB - https://www.exploit-db.com:
| No findings
|
| OpenVAS (Nessus) - http://www.openvas.org:
| No findings
|
| SecurityTracker - https://www.securitytracker.com:
| No findings
|
| OSVDB - http://www.osvdb.org:
| No findings
|_
7070/tcp open   ssl/realserver?
8082/tcp open   blackice-alerts?
| fingerprint-strings:
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, RTSPRequest, SIPOptions:
|     HTTP/1.1 400 Error
|     Server: QQ/1.0.0 (Tencent)
|     Content-Length: 18
|     Connection: close
|_    unkown the request
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port1947-TCP:V=7.94SVN%I=7%D=10/11%Time=6526EDF6%P=x86_64-unknown-linux
SF:-gnu%r(GetRequest,192,"HTTP/1\.0\x20403\x20Forbidden\r\nServer:\x20HASP
SF:\x20LM/25\.02\r\nDate:\x20Wed,\x2011\x20Oct\x202023\x2018:52:18\x20GMT\
SF:r\nX-Frame-Options:\x20SAMEORIGIN\r\nStrict-Transport-Security:\x20max-
SF:age=0;\r\nX-Content-Type-Options:\x20nosniff\r\nReferrer-Policy:\x20str
SF:ict-origin\r\nContent-Type:\x20text/html\r\nContent-Length:\x20137\r\n\
SF:r\n<title>403\x20Forbidden</title>\n<h1>403\x20Forbidden</h1>\nAccess\x
SF:20to\x20this\x20resource\x20has\x20been\x20denied\x20to\x20you\.\n<p>Pl
SF:ease\x20contact\x20the\x20administrator\.\n")%r(HTTPOptions,1B3,"HTTP/0
SF:\.0\x20501\x20Not\x20Implemented\r\nServer:\x20HASP\x20LM/25\.02\r\nDat
SF:e:\x20Wed,\x2011\x20Oct\x202023\x2018:52:18\x20GMT\r\nX-Frame-Options:\
SF:x20SAMEORIGIN\r\nStrict-Transport-Security:\x20max-age=0;\r\nX-Content-
SF:Type-Options:\x20nosniff\r\nReferrer-Policy:\x20strict-origin\r\nConten
SF:t-Type:\x20text/html\r\nContent-Length:\x20164\r\n\r\n<title>501\x20Not
SF:\x20Implemented</title>\n<h1>501\x20Not\x20Implemented</h1>\nYour\x20re
SF:quest\x20was\x20not\x20understood\x20or\x20not\x20allowed\x20by\x20this
SF:\x20server\.\n<p>Please\x20contact\x20the\x20administrator\.\n")%r(RTSP
SF:Request,1B3,"HTTP/0\.0\x20501\x20Not\x20Implemented\r\nServer:\x20HASP\
SF:x20LM/25\.02\r\nDate:\x20Wed,\x2011\x20Oct\x202023\x2018:52:18\x20GMT\r
SF:\nX-Frame-Options:\x20SAMEORIGIN\r\nStrict-Transport-Security:\x20max-a
SF:ge=0;\r\nX-Content-Type-Options:\x20nosniff\r\nReferrer-Policy:\x20stri
SF:ct-origin\r\nContent-Type:\x20text/html\r\nContent-Length:\x20164\r\n\r
SF:\n<title>501\x20Not\x20Implemented</title>\n<h1>501\x20Not\x20Implement
SF:ed</h1>\nYour\x20request\x20was\x20not\x20understood\x20or\x20not\x20al
SF:lowed\x20by\x20this\x20server\.\n<p>Please\x20contact\x20the\x20adminis
SF:trator\.\n")%r(FourOhFourRequest,192,"HTTP/1\.0\x20403\x20Forbidden\r\n
SF:Server:\x20HASP\x20LM/25\.02\r\nDate:\x20Wed,\x2011\x20Oct\x202023\x201
SF:8:53:01\x20GMT\r\nX-Frame-Options:\x20SAMEORIGIN\r\nStrict-Transport-Se
SF:curity:\x20max-age=0;\r\nX-Content-Type-Options:\x20nosniff\r\nReferrer
SF:-Policy:\x20strict-origin\r\nContent-Type:\x20text/html\r\nContent-Leng
SF:th:\x20137\r\n\r\n<title>403\x20Forbidden</title>\n<h1>403\x20Forbidden
SF:</h1>\nAccess\x20to\x20this\x20resource\x20has\x20been\x20denied\x20to\
SF:x20you\.\n<p>Please\x20contact\x20the\x20administrator\.\n");   
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port8082-TCP:V=7.94SVN%I=7%D=10/11%Time=6526EDFB%P=x86_64-unknown-linux
SF:-gnu%r(GetRequest,6D,"HTTP/1\.1\x20400\x20Error\x20\r\nServer:\x20QQ/1\
SF:.0\.0\x20\(Tencent\)\x20\r\nContent-Length:\x2018\r\nConnection:\x20clo
SF:se\r\n\r\nunkown\x20the\x20request")%r(FourOhFourRequest,6D,"HTTP/1\.1\
SF:x20400\x20Error\x20\r\nServer:\x20QQ/1\.0\.0\x20\(Tencent\)\x20\r\nCont
SF:ent-Length:\x2018\r\nConnection:\x20close\r\n\r\nunkown\x20the\x20reque
SF:st")%r(GenericLines,6D,"HTTP/1\.1\x20400\x20Error\x20\r\nServer:\x20QQ/
SF:1\.0\.0\x20\(Tencent\)\x20\r\nContent-Length:\x2018\r\nConnection:\x20c
SF:lose\r\n\r\nunkown\x20the\x20request")%r(HTTPOptions,6D,"HTTP/1\.1\x204
0close\
SF:r\n\r\nunkown\x20the\x20request")%r(SIPOptions,6D,"HTTP/1\.1\x20400\x20        
SF:Error\x20\r\nServer:\x20QQ/1\.0\.0\x20\(Tencent\)\x20\r\nContent-Length        
SF::\x2018\r\nConnection:\x20close\r\n\r\nunkown\x20the\x20request");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 174.07 seconds
```

```sh
#$ seoanalyze https://www.sethserver.com/ -f html > results.html

$ whatweb github.com

http://github.com [301 Moved Permanently] Country[UNITED STATES][US], IP[192.30.255.112], RedirectLocation[https://github.com/]
https://github.com/ [200 OK] Content-Language[en-US], Cookies[_gh_sess,_octo,logged_in], Country[UNITED STATES][US], Email[eyebrow-23@2x.png], HTML5, HTTPServer[GitHub.com], HttpOnly[_gh_sess,logged_in], IP[192.30.255.112], Open-Graph-Protocol[object][1401488693436528], OpenSearch[/opensearch.xml], Script[application/javascript,application/json], Strict-Transport-Security[max-age=31536000; includeSubdomains; preload], Title[GitHub: Let’s build from here · GitHub], UncommonHeaders[x-content-type-options,referrer-policy,content-security-policy,x-github-request-id], X-Frame-Options[deny], X-XSS-Protection[0]
```

```sh
$ webanalyze -host www.github.com  -crawl 1
 :: webanalyze        : v0.3.9
 :: workers           : 4
 :: technologies      : technologies.json
 :: crawl count       : 1
 :: search subdomains : true
 :: follow redirects  : false

https://docs.github.com (1.8s):
    Azure Front Door,  (Load balancers)
    Azure,  (PaaS)
    Varnish,  (Caching)
    Next.js,  (JavaScript frameworks, Web frameworks, Web servers, Static site generator)
    React,  (JavaScript frameworks)
    Webpack,  (Miscellaneous)
    Node.js,  (Programming languages)
    HSTS,  (Security)
    Azure Edge Network,  (Miscellaneous)
http://github.com (3.2s):
    GitHub Pages,  (PaaS)
    HSTS,  (Security)
    Amazon S3,  (CDN)
    Amazon Web Services,  (PaaS)
```

```bash
wapiti -u 
```

```bash
nuclei -u 192.168.0.14

                     __     _
   ____  __  _______/ /__  (_)
  / __ \/ / / / ___/ / _ \/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\__,_/\___/_/\___/_/   v2.9.15

                projectdiscovery.io

[INF] Your current nuclei-templates v9.6.4 are outdated. Latest is v9.6.5
[INF] Successfully updated nuclei-templates (v9.6.5) to /root/nuclei-templates. GoodLuck!
[INF] Current nuclei version: v2.9.15 (latest)
[INF] Current nuclei-templates version: v9.6.5 (latest)
[INF] New templates added in latest release: 75
[INF] Templates loaded for current scan: 6967
[INF] Targets loaded for current scan: 1
[INF] Running httpx on input host
[INF] Found 1 URL from httpx
[INF] Templates clustered: 1218 (Reduced 1156 Requests)
[INF] Using Interactsh Server: oast.me
[basic-auth-detect] [http] [info] https://192.168.0.14
[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] https://192.168.0.14
[http-missing-security-headers:content-security-policy] [http] [info] https://192.168.0.14
[http-missing-security-headers:permissions-policy] [http] [info] https://192.168.0.14
[http-missing-security-headers:x-content-type-options] [http] [info] https://192.168.0.14
[http-missing-security-headers:referrer-policy] [http] [info] https://192.168.0.14
[http-missing-security-headers:cross-origin-resource-policy] [http] [info] https://192.168.0.14
[http-missing-security-headers:strict-transport-security] [http] [info] https://192.168.0.14
[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] https://192.168.0.14
[http-missing-security-headers:clear-site-data] [http] [info] https://192.168.0.14
[http-missing-security-headers:cross-origin-opener-policy] [http] [info] https://192.168.0.14
[waf-detect:apachegeneric] [http] [info] https://192.168.0.14/
[self-signed-ssl] [ssl] [low] 192.168.0.14:443
[ssl-dns-names] [ssl] [info] 192.168.0.14:443 [DESKTOP-28E7H5T]        
[tls-version] [ssl] [info] 192.168.0.14:443 [tls10]
[deprecated-tls] [ssl] [info] 192.168.0.14:443 [tls10]
[weak-cipher-suites:tls-1.0] [ssl] [low] 192.168.0.14:443 [[tls10 TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA]]
[tls-version] [ssl] [info] 192.168.0.14:443 [tls11]
[deprecated-tls] [ssl] [info] 192.168.0.14:443 [tls11]
[weak-cipher-suites:tls-1.1] [ssl] [low] 192.168.0.14:443 [[tls11 TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA]]
[tls-version] [ssl] [info] 192.168.0.14:443 [tls12]
```