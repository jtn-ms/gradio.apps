FROM python:3.10.11

RUN apt update && apt install  -y --no-install-recommends vim nmap lsof zip git-lfs

RUN mkdir /app

EXPOSE 8080

WORKDIR /app
CMD ["bash"]