```sh
# office2john
$ office2john test.xlsx > hash.txt
> 
test.xlsx:$office$*2013*100000*256*16*28af71850e64b0f8a12ad564fec06981*fc28746504e05ce8e9538e8b089e8cf6*3a4bb449b04e2582dc9bd9730c7c1068ac111789234b58ddcf6d34074ab38af7

# office2hashcat
$ cd /app/tools/crackers/office2hashcat && python3 office2hashcat.py /tmp/test.xlsx > hash.txt
$office$*2013*100000*256*16*28af71850e64b0f8a12ad564fec06981*fc28746504e05ce8e9538e8b089e8cf6*3a4bb449b04e2582dc9bd9730c7c1068ac111789234b58ddcf6d34074ab38af7
```

- office2john
- ssh2john
- pdf2john