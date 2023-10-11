```sh
docker volume ls
docker builder prune -a
docker container prune
docker image prune -a
docker volume prune
docker system prune -all

# forfiles /s /m *.vhdx /c "cmd /c echo @fsize @path"
# Get-ChildItem -Recurse -Filter *.vhdx | Measure-Object -Property Length -Sum | ForEach-Object { $_.Sum / 1MB }
find /cygdrive/c/Users -type f -name \*.vhdx -exec du -ah {} \;
# find /cygdrive/c/Users -name "*.vhdx" -exec du -ah {} \; | sort -h
# find /cygdrive/c/Users -name \*.vhdx "%p\t%k KB\n"
# find /cygdrive/c/Users -type f -exec ls -lh \{\} \;
# find /cygdrive/c/Users -type f -exec wc -c \{\} \;

wsl -l -v
wsl --shutdown

diskpart
> select vdisk file="C:\Users\username\AppData\Local\Docker\wsl\data\ext4.vhdx"
> compact vdisk

Enable-WindowsOptionalFeature -Online -FeatureName $("Microsoft-Hyper-V", "Containers") -All
& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon
```