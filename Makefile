SHELL=/bin/sh

route-add:
	sudo route add -net 192.168.12.0/24 192.168.11.1

route-add2:
	sudo route add -net 192.168.12.0/24 gw 192.168.11.1

rp0:
	ssh 192.168.12.100 -l pi


rp3:
	ssh 192.168.12.103 -l pi

