```sh
# Extract hash from file
$ office2john test.xlsx > hash.txt
> 
test.xlsx:$office$*2013*100000*256*16*28af71850e64b0f8a12ad564fec06981*fc28746504e05ce8e9538e8b089e8cf6*3a4bb449b04e2582dc9bd9730c7c1068ac111789234b58ddcf6d34074ab38af7

#
$ john --rules --wordlist=/app/passwords/rockyou.txt hash.txt
>
Using default input encoding: UTF-8
Loaded 1 password hash (Office, 2007/2010/2013 [SHA1 512/512 AVX512BW 16x / SHA512 512/512 AVX512BW 8x AES])
Cost 1 (MS Office version) is 2013 for all loaded hashes
Cost 2 (iteration count) is 100000 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
111              (test.xlsx)     
1g 0:00:03:35 DONE (2023-10-06 09:51) 0.004633g/s 667.7p/s 667.7c/s 667.7C/s 12181988..110199
Use the "--show" option to display all of the cracked passwords reliably      
Session completed.
```