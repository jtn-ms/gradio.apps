image_name=kali
image_tag=full
container_name=${image_name}-app

build:
	@docker build -t ${image_name} . -f Dockerfile.${image_name}

# docker run -dit --name ${container_name} -p 80:8080  ${image_name}:${image_tag} bash
access.bash:
	@docker run -dit --name ${container_name} -p 80:8080 --net="host" --privileged ${image_name}:${image_tag} bash
	@docker container attach ${container_name}

run.exited.container:
	@docker start -p 80:8080 `docker ps -q -l` # restart it in the background
	@docker attach `docker ps -q -l` # reattach the terminal & stdin

create.access.point:
	@docker exec -it ${container_name} /bin/bash

stop:
	@docker stop ${container_name}

clean: stop
	@docker rm ${container_name}

clean.all:
	@docker ps -q | xargs docker stop
	@docker ps -q | xargs docker rm

clean.caches:
	docker builder prune -a
	docker container prune
	docker image prune -a
	docker volume prune

iid_old=refacer
iid_new=face
tid_old=enhanced
tid_new=ready

change.name:
	@docker tag ${iid_old}:${tid_old} ${iid_new}:${tid_new}
	@docker rmi ${iid_old}:${tid_old}


image_name_new=${image_name}
image_tag_new=${image_tag}
container2image:
	@docker commit ${container_name} ${image_name_new}:${image_tag_new}

tar_fn=${image_name}.${image_tag}.tar.gz
img2tar:
	@docker save ${image_name}:${image_tag} > ${tar_fn}

# docker load < ${tar_fn}
image@container:
	@docker load -i ${tar_fn}