- BruteForce
- Positioning: 
  * [bssid2position](https://www.mylnikov.org/)
  * mac2position
- ipAddr2vulnerability: 
- Session Hijacking

## Procedures

### 1. Gathering Info(IPs, open Ports, OS info, Computer Name, User Name, Password, Vulnerabilities - Missing Patches)

  * Windows: `$ systeminfo > sysinfo.txt`
  - Detect Vulnerabilities - Missing Patches
    * [wesng](https://github.com/bitsadmin/wesng.git): `python3 wes.py -e sysinfo.txt`

### 2. Exploit Vulnerabilities
  
  * Select Payload/Module: ``
  * Set Target IP: 
  * Exploit: `msf6> exploit` 

## Tools

### All-In-One Tools

- [x] [hackingtools](https://github.com/Z4nzu/hackingtool.git)
- [ ] [lockdoor](https://github.com/SofianeHamlaoui/Lockdoor-Framework)
- [ ] [Offensive Docker](https://github.com/aaaguirrep/offensive-docker)
- [x] [sniper](https://github.com/1N3/Sn1per)

### Kali Linux Tools

- all-in-one: hackingtool, sniper, lockdoor, pythem, 
- exploit: msfconsole
- nikto
- sqlmap
- bruteforce: hashcat,john,hydra,aircrack-ng

```
apt install -y set hashcat john

| Target | Usage
| ------ | - 
login   |  hydra -l user -P passlist.txt ftp://192.168.0.1
website | sniper -t 192.168.0.6
find windows vulnerability | cd /app/tools/tmp/wesng && python3 wes.py -e sysinfo.txt
```

