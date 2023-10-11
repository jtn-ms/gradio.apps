## wmic

```bat
> wmic
rem hard drive health check
wmic:root:\cli> diskdrive get status
```

```sh
# or just run online query
wmic /?
wmic bios get serialnumber
wmic bios get version
wmic os get version
wmic product get name
wmic csproduct get name
wmic cpu get numberofcores
wmic CPU Get DeviceID,NumberOfCores,NumberOfLogicalProcessors
wmic systemslot get slotdesignation,currentusage,description,status
wmic port get name
wmic temperature get deviceid,name,status
wmic process list
wmic process where ExecutablePath='C:\\windows\\system32\\notepad.exe' get ProcessId
wmic process where "name='chrome.exe'" get ProcessID, ExecutablePath
wmic process get ProcessID,ExecutablePath
## How to Check all the logs related to Explorer 
wmic ntevent where (message like "%explorer%") list brief
## How to Get All the Users logged in to a Remote System
wmic /node:192.168.27.103 /user:admin /password:pass123 computersystem get username
## How to Count the number of Installed Updates in Windows
wmic qfe list | find /c /v ""
## How to Display the State of all the Global Switches in Windows
wmic context
```

## net

```sh
net help

# How to Get the List of all Users in the System
net user
# How to Change User Password in Windows using net command
net user cyberithub pass123
# How to Add a Local User in the System
net user cyberithub pass123 /add
# How to Delete a User from the System
net user cyberithub /delete
# How to Save all the group members of current domain User in a File
net user /domain john.wick >> groupname.txt
# How to Check If a User Account is Locked
net user /domain john.wick | find /i "Account active"
# How to Unlock a Domain User Account
net user john.wick /DOMAIN /ACTIVE:YES
# How to Check If the Domain User is Active
net user john.wick /DOMAIN | FIND /I "Account active"
# How to Check Last Login time of User in Current Domain
net user john /domain | findstr /C:"Last logon"

# How to Check the List of Configurable Services
net config

# How to Check the Workstation Stats
net stats workstation

# How to remove a currently mapped drive
net use e: /delete

# How to List all the workgroups in current Domain
net view /domain

# How to Get the List of All Local Groups
net localgroup
# How to Get the List of all the members of a Local Group
net localgroup Administrators
# How to Add a User into a Local Group
net localgroup administrators cyberithub /add
# How to Remove User from a Local Group
net localgroup administrators cyberithub /delete

# How to Add a Group to Domain User
net group "Internet Access Group" john.wick /add /domain
# How to Save all the members of a Group in a File
net group ITGroup /domain >c:\abc.txt

# How to Check all the Shared Folders
net share
# How to Share a Folder with Specific Permission 
net share Public=s:\Public /GRANT:Everyone,FULL
# How to Share a Folder with Alias
net share list="c:\art lst"
# How to Stop Sharing a Folder
net share DataShare /delete

# How to Copy the Contents from another System 
net use \\DESKTOP-THKO9\c$ * /USER:mx\john.wick

# How to Start a Service in Windows using net command
net start wuauserv
# How to Stop a Service in Windows using net command

```