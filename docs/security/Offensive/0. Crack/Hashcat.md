```sh
# Generate Hash
$ echo -n 123 | md5sum
> 202cb962ac59075b964b07152d234b70  -
# or Fetch Hash from encrypted files

# Guess the encryption algorithms from Hash
$ hashid -m 202cb962ac59075b964b07152d234b70
Analyzing '202cb962ac59075b964b07152d234b70'
[+] MD2
[+] MD5 [Hashcat Mode: 0]
[+] MD4 [Hashcat Mode: 900]
[+] Double MD5 [Hashcat Mode: 2600]
[+] LM [Hashcat Mode: 3000]
[+] RIPEMD-128
[+] Haval-128
[+] Tiger-128
[+] Skein-256(128)
[+] Skein-512(128)
[+] Lotus Notes/Domino 5 [Hashcat Mode: 8600]
[+] Skype [Hashcat Mode: 23]
[+] Snefru-128
[+] NTLM [Hashcat Mode: 1000]
[+] Domain Cached Credentials [Hashcat Mode: 1100]
[+] Domain Cached Credentials 2 [Hashcat Mode: 2100]
[+] DNSSEC(NSEC3) [Hashcat Mode: 8300]

# Crack Hash
$ hashcat -m 0 -a 0 202cb962ac59075b964b07152d234b70 /app/passwords/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 4.0+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 15.0.7, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]  
==================================================================================================================================================  
* Device #1: cpu-skylake-avx512-11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz, 6874/13813 MB (2048 MB allocatable), 8MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 2 MB

Dictionary cache building ../passwords/rockyou.txt: 33553435 bytes (23.98%Dictionary cache building ../passwords/rockyou.txt: 134213745 bytes (95.92Dictionary cache built:
* Filename..: ../passwords/rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 1 sec

202cb962ac59075b964b07152d234b70:123

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
Hash.Target......: 202cb962ac59075b964b07152d234b70
Time.Started.....: Fri Oct  6 09:20:14 2023 (0 secs)
Time.Estimated...: Fri Oct  6 09:20:14 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (../passwords/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   169.1 kH/s (0.30ms) @ Accel:1024 Loops:1 Thr:1 Vec:16
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 8192/14344384 (0.06%)
Rejected.........: 0/8192 (0.00%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> total90

Started: Fri Oct  6 09:19:44 2023
Stopped: Fri Oct  6 09:20:15 2023
```

## Use hashcat 

```
apt install hashcat hashcat-utils
```

| Target | Usage
| ------ | -----
**Office**
| xlsx | python3 office2hashcat.py the_path_to_your_excel_file_here.xls