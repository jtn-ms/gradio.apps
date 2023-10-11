```sh
apt-get install zerofree
df -h
# Replace /dev/sdxX with the ext2, ext3 or ext4 formatted partition in question.
zerofree /dev/sdxX
```
```sh
VBoxManage modifyhd <name>.vdi --compact
```