- Shrink

```sh
apt-get install zerofree
df -h
# Replace /dev/sdxX with the ext2, ext3 or ext4 formatted partition in question.
zerofree /dev/sdxX
```
```sh
VBoxManage modifyhd <name>.vdi --compact
```

- Resize

```sh
VBoxManage.exe modifyhd kali-linux.vdi " --resize 20480

sudo aptitude install qemu-utils
sudo modprobe nbd
VBoxManage modifyhd <vdi-file> --resize <new_size>
sudo qemu-nbd -c /dev/nbd0 <vdi-file>
sudo gparted /dev/nbd0
sudo qemu-nbd -d /dev/nbd0
```