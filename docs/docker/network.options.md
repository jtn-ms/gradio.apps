Remember one point that the host networking driver only works on Linux hosts, and is not supported on Docker Desktop for Mac, Docker Desktop for Windows, or Docker EE for Windows Server

```sh
$ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
3e22fe306f72   bridge    bridge    local
28fe6947ceb7   host      host      local
76aefbca5f8b   none      null      local
```

Q & A: bridge vs. host

| Feature	|   Bridge	|   Host    |
| --------- | --------- | --------- |
| Driver	| The Bridge network is provided by the Bridge driver |	The host network is provided by the host driver.
| Default	| bridge is the default network and provided by a bridge driver |	Host does not default.
| Connectivity |	The bridge driver provides intercontainer connectivity for all containers running on the same machine.	| The host driver instructs Docker not to create any special networking namespace or resources for attached containers.

```sh
eval image_name=kali
eval tag_name=full
eval container_name=${image_name}-app


docker stop ${container_name}
docker container prune

# host:
# bridge:
# none or any: isolate the services from different container
eval network=bridge

docker run -dit --name ${container_name} --net=${network} --privileged ${image_name}:${tag_name} /bin/bash

docker exec -it ${container_name} bash
```

- bridge is default, bridge (docker0)

```sh
$ docker run -dit --name ${container_name} --cap-add=NET_ADMIN --privileged=true ${image_name}:${tag_name} /bin/bash
┌──(root㉿644c3769e3cb)-[/]
└─# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet) 
        RX packets 74  bytes 56863 (55.5 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0       
        TX packets 46  bytes 3588 (3.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0       
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

- isolate container from internet & other containers
  
```sh
# Creating a network:
docker network create -d bridge --internal hostonly

# Running a container:
docker run --network hostonly ... 
```