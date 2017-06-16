Installation on Ubuntu 16.04.2 x64 at Desktop Machine
---

## Machine Features

```
$ cat /proc/version
Linux version 4.4.0-79-generic (buildd@lcy01-30) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) )
#100-Ubuntu SMP Wed May 17 19:58:14 UTC 2017


```

```
$ cat /etc/*release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.2 LTS"
NAME="Ubuntu"
VERSION="16.04.2 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.2 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
```


## Installation in Desktop Machine

Create path
```
cd && mkdir naosoftware && cd naosoftware
```

For Python SDK and C++ SDK and other version of Choregraphe, sign in to
https://community.ald.softbankrobotics.com/en/resources/software/robot/nao-2

Sign in
https://developer.softbankrobotics.com/us-en/downloads/nao-v5-v4
to download
* Choregraphe 2.1.4 Linux 64 Binaries
* Python 2.7 SDK 2.1.4 Linux 64
* C++ SDK 2.1.4 Linux 64
* Cross Toolchain 2.1.4 Linux 64



```
tar -xvzf choregraphe-suite-2.1.4.13-linux64.tar.gz
```

Launching choregraphe
```
cd choregraphe-suite-2.1.4.13-linux64
 ./choregraphe
```


When you launch Choregraphe the first time, the following license key is requested
[ref](https://developer.softbankrobotics.com/us-en/downloads/nao-v5-v4).
Please copy and paste the following key:
654e-4564-153c-6518-2f44-7562-206e-4c60-5f47-5f45




##  Installation of pynaoqo --- Python 2.7 SDK 2.1.4 Linux 64
```
cd ~/naosoftware/
tar -xvzf naoqi-sdk-2.1.4.13-linux64.tar.gz
tar -xvzf pynaoqi-python2.7-2.1.4.13-linux64.tar.gz
echo 'export PYTHONPATH=${PYTHONPATH}:/home/map479/naosoftware/pynaoqi-python2.7-2.1.4.13-linux64' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="/home/map479/naosoftware/naoqi-sdk-2.1.4.13-linux64:$LD_LIBRARY_PATH"' >> ~/.bashrc
sudo ldconfig
sudo cp -a /home/map479/naosoftware/naoqi-sdk-2.1.4.13-linux64/lib/libboost_*.so.* /home/map479/naosoftware/naoqi-sdk-2.1.4.13-linux64/
source ~/.bashrc
```
[Source](https://community.ald.softbankrobotics.com/en/forum/import-issue-pynaoqi-214-ubuntu-7956)




# IP Configuration

## Ubuntu Local Link [ref](http://doc.aldebaran.com/2-1/nao/connectivity.html#how-to-ubuntu-and-local-link)
1. Edit connections  
2. Add Ethernet Connection Type [CREATE]
3. Select the tab IPv4-Settings, and change the Method (Automatic DHCP) to (Link-Local Only).
   (Change connection name to NAO)
   and tick Require IPv4 addressing for this connection to complete
4. Click on Save, and close the menu.


## Network Connection

For IP Configuration, go to network connections and select connect to NAO, once established the connection,
you can run
```
$ ip address list
2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 70:71:bc:0c:1e:ed brd ff:ff:ff:ff:ff:ff
    inet 169.254.164.69/16 brd 169.254.255.255 scope link eno1
       valid_lft forever preferred_lft forever
    inet6 fe80::2d0f:c8e3:534c:b6ab/64 scope link
       valid_lft forever preferred_lft forever
```

```
$ ip r
169.254.0.0/16 dev eno1  proto kernel  scope link  src 169.254.164.69  metric 100
224.0.0.0/4 dev eno1  proto static  scope link  metric 100
```






NB. In case of any issues, add a rule for the firewall: "sudo ufw allow in on eth0 from 169.254.0.0/16"
In case that you need to rename the network interface on Ubuntu 16.04, you can follow this instructions:
[SOURCE](https://askubuntu.com/questions/783457/renaming-network-interface-in-ubuntu-16-04-with-systemd-fails)


# TESTING


## With choregraphe
```
cd ~/naosoftware/choregraphe-suite-2.1.4.13-linux64
./choregraphe
```

1. connect to ...
2. nao.local
3. Open project
4. Upload to the robot and play
5. Stop and disconnect


## With python
```
cd ~/mxochicale/github/nao/examples/python/testing
$ ./sayingsth.py
[I] 5131 qimessaging.session: Session listener created on tcp://0.0.0.0:0
[I] 5131 qimessaging.transportserver: TransportServer will listen on: tcp://169.254.164.69:39124
[I] 5131 qimessaging.transportserver: TransportServer will listen on: tcp://127.0.0.1:39124
sys.version_info(major=2, minor=7, micro=12, releaselevel='final', serial=0)
```


DONE :)
Fri 16 Jun 15:32:03 BST 2017
@UoB UK
