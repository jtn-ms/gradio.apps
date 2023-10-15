```sh
# List available shares.
$ smbclient -N -L //192.168.0.14
session setup failed: NT_STATUS_ACCESS_DENIED

# Connect to a share if any.
smbclient -N //192.168.0.14/Share

# Mount Shares
mount -t cifs -o username=user,password=password //10.0.0.3/Share /mnt/share

# Download Files
smbclient //10.0.0.3/Share "" -N -Tc backup.tar users/docs
```