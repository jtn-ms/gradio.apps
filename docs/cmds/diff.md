| linux | windows | 
| ----- | ------- |
utilities
| `cat x.lst` | `type x.lst` |
| `diff 1.txt 2.txt` | `fc /C 1.txt 2.txt` |
| `clear` | `cls` |
| `pwd` | `pwd` |
| `whoami` | `` |
| `which python` | `` |
time
| `timedatectl \| grep "Time zone"` <br> `cat /etc/timezone`  | `tzutil /g` |
| `ln -sf /usr/share/zoneinfo/Africa/Nairobi /etc/localtime` | `tzutil /s "Eastern Standard Time"` |
| `date` | `date` |
network
| `traceroute google.com` | `tracert -d google.com` |
| `host google.com` | `` |
| `lsof -i` | `netstat` |
file
| `shred -u <filename>` | `cipher /w:driveletter:\foldername` |
process
| `ls -d`
| `ps -ef` | `tasklist` |
| `pkill python.exe` | `taskkill /f /im python` |
| `kill -9 2212` | `taskkill /f /pid 2212` |
file system
| `lsb_release -a` | `systeminfo` |
| `du -hs` | `` |
| `df -h` | `` |

## Encrypting & Decrypting

### Windows - `cipher /?`

| usage | linux | windows | 
| ----- | ------- | ----- |
| encrypt | `gpg -c [file_name]` | `cipher /e sysinfo.txt` |
| decrypt | `gpg [file_name.gpg]`| `cipher /d sysinfo.txt` |
| overwrite | `shred -u [file_name]` | `cipher /w:driveletter:\foldername` |