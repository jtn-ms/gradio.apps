## [How to get access to host wifi interface from docker container](https://stackoverflow.com/questions/62406362/ubuntu-under-windows-subsystem-for-linux-2-wsl2-has-no-internet-access)

```sh
wsl --shutdown
netsh winsock reset
netsh int ip reset all
netsh winhttp reset proxy
ipconfig /flushdns
netsh winsock reset
shutdown /r 

export image_name=kali
export tag_name=full
export container_name=${image_name}-app
docker run -dit --name ${container_name} --net=host --privileged ${image_name}:${tag_name} /bin/bash
docker exec -it ${container_name} bash
```