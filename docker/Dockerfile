FROM williamyeh/ansible:ubuntu16.04

RUN apt update -y && apt install -y docker.io
RUN pip install molecule docker-py

WORKDIR /root/build
CMD ["/bin/bash"]
