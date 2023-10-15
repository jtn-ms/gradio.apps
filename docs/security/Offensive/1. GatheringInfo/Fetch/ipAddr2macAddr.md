```sh
┌──(root㉿docker-desktop)-[/]
└─# nmblookup -A 192.168.0.14
Looking up status of 192.168.0.14
        DESKTOP-28E7H5T <00> -         M <ACTIVE>
        WORKGROUP       <00> - <GROUP> M <ACTIVE>
        DESKTOP-28E7H5T <20> -         M <ACTIVE>

        MAC Address = 8C-1D-96-97-0A-18
```

```sh
┌──(root㉿docker-desktop)-[/]
└─# nbtscan 192.168.0.14
Doing NBT name scan for addresses from 192.168.0.14

IP address       NetBIOS Name     Server    User             MAC address
------------------------------------------------------------------------------
192.168.0.14     DESKTOP-28E7H5T  <server>  <unknown>        8c:1d:96:97:0a:18
```

```sh
┌──(root㉿docker-desktop)-[/]
└─# enum4linux -a 192.168.0.14
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Thu Oct 12 01:39:24 2023

 =========================================( Target Information )=========================================

Target ........... 192.168.0.14
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ============================( Enumerating Workgroup/Domain on 192.168.0.14 )============================


[+] Got domain/workgroup name: WORKGROUP


 ================================( Nbtstat Information for 192.168.0.14 )================================

Looking up status of 192.168.0.14
        DESKTOP-28E7H5T <00> -         M <ACTIVE>  Workstation Service
        WORKGROUP       <00> - <GROUP> M <ACTIVE>  Domain/Workgroup Name
        DESKTOP-28E7H5T <20> -         M <ACTIVE>  File Server Service

        MAC Address = 8C-1D-96-97-0A-18

 ===================================( Session Check on 192.168.0.14 )===================================


[E] Server doesn't allow session using username '', password ''.  Aborting remainder of tests.
```

```sh
msf6 >  use auxiliary/scanner/smb/smb_version
msf6 auxiliary(scanner/smb/smb_version) > set rhost 192.168.0.14
msf6 auxiliary(scanner/smb/smb_version) > run

[*] 192.168.0.14:445      - SMB Detected (versions:2, 3) (preferred dialect:SMB 3.1.1) (compression capabilities:LZNT1, Pattern_V1) (encryption capabilities:AES-256-GCM) (signatures:optional) (guid:{2a651a41-4cc0-439d-8e32-797bec683935}) (authentication domain:DESKTOP-28E7H5T)   
[*] 192.168.0.14:         - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```