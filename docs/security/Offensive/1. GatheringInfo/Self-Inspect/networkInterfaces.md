
```powershell
$addr='192.168.0.6'; get-wmiobject Win32_NetworkAdapterConfiguration |? {$_.ipaddress -contains $addr} |select Description |% {$_.Description}
```

```sh
netsh interface show interface
netsh int ipv4 show interfaces

powershell "Get-NetConnectionProfile | Select-Object -ExpandProperty Name"
powershell "Get-WMIObject Win32_networkadapter | Select-Object Name, AdapterType, InterfaceIndex | Format-List"
```