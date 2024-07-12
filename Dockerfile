FROM debian:latest

RUN mkdir /var/lospollos

####### INSTALLATIONS #######
RUN apt update
RUN apt install -y python3 python3-pip sudo gdb coreutils nano ssh

####### USER ########
RUN useradd Tyrus
RUN useradd -m mike
COPY Mike /home/mike
COPY root.txt /root
RUN gcc /home/mike/message.c -o /home/mike/message -fno-stack-protector -z execstack -no-pie

RUN echo 'mike:Password123' | chpasswd

RUN echo "Tyrus ALL=(root) NOPASSWD: /usr/bin/base64" >> /etc/sudoers
RUN echo "mike ALL=(root) NOPASSWD: /home/mike/message" >> /etc/sudoers

####### WEB SERVER #######
COPY serverweb/requirements.txt /var/lospollos
RUN pip install -r /var/lospollos/requirements.txt --break-system-packages
COPY serverweb /var/lospollos

COPY entrypoint.sh /var/lospollos

WORKDIR /var/lospollos
RUN chmod a+x entrypoint.sh


RUN chown -R Tyrus:Tyrus /var/lospollos
RUN chown -R mike:mike /home/mike
USER Tyrus



ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
