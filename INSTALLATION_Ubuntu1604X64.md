Installation on Ubuntu 14.04.2 x64
---

## Machine Features

```
$ cat /proc/version
Linux version 4.4.0-75-generic (buildd@lgw01-21) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) )
#96-Ubuntu SMP Thu Apr 20 09:56:33 UTC 2017
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

```
$ gcc --version
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```







In case that you need to rename the network interface on Ubuntu 16.04, you can follow this instructions:
[SOURCE](https://askubuntu.com/questions/783457/renaming-network-interface-in-ubuntu-16-04-with-systemd-fails)




## Installation in Desktop Machine

Create path
```
cd && mkdir naosoftware && cd naosoftware
```

Sign in and downdload Choregraphe 2.1.4 Linux 64 Binaries
https://community.ald.softbankrobotics.com/en/resources/software/robot/nao-2

For Python SDK and C++ SDK and other version of Choregraphe go to
https://developer.softbankrobotics.com/us-en/downloads/nao-v5-v4


```
tar -xvzf choregraphe-suite-2.1.4.13-linux64.tar.gz
rm choregraphe-suite-2.1.4.13-linux64.tar.gz
```

When you launch Choregraphe, the license key is requested
[ref](https://developer.softbankrobotics.com/us-en/downloads/nao-v5-v4).
Please copy and paste the following key:
654e-4564-153c-6518-2f44-7562-206e-4c60-5f47-5f45

Launching choregraphe
```
cd choregraphe-suite-2.1.4.13-linux64
 ./choregraphe
```


# IP Configuration

## Ubuntu Local Link [ref](http://doc.aldebaran.com/2-1/nao/connectivity.html#how-to-ubuntu-and-local-link)
1. Edit connections  
2. Add Ethernet Connection Type
3. Select the tab IPv4-Settings, and change the Method to Link-Local Only.
   (Change connection name: NAO)
   and tick Require IPv4 addressing for this connection to complete
4. Click on Save, and close the menu.




## Network Connection

For IP Configuration, go to network connections and select connect to NAO, once established the connection,
you can run
```
$ ip address list
3: enp5s0f1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:1e:67:56:d0:ab brd ff:ff:ff:ff:ff:ff
    inet 169.254.52.160/16 brd 169.254.255.255 scope link enp5s0f1
       valid_lft forever preferred_lft forever
    inet6 fe80::d94b:6ff:3620:1618/64 scope link
       valid_lft forever preferred_lft forever
$ ip r

```


NB. In case of any issues, add a rule for the firewall: "sudo ufw allow in on eth0 from 169.254.0.0/16"





##  Installation of pynaoqo --- Python 2.7 SDK 2.1.4 Linux 64
```
cd ~/naosoftware/
tar -xvzf naoqi-sdk-2.1.4.13-linux64.tar.gz
tar -xvzf pynaoqi-python2.7-2.1.4.13-linux64.tar.gz
rm pynaoqi-python2.7-2.1.4.13-linux64.tar.gz
echo 'export PYTHONPATH=${PYTHONPATH}:/home/map479/naosoftware/pynaoqi-python2.7-2.1.4.13-linux64' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="/home/map479/naosoftware/naoqi-sdk-2.1.4.13-linux64:$LD_LIBRARY_PATH"' >> ~/.bashrc
sudo ldconfig
sudo cp -a /home/map479/naosoftware/naoqi-sdk-2.1.4.13-linux64/lib/libboost_*.so.* /home/map479/naosoftware/naoqi-sdk-2.1.4.13-linux64/
source ~/.bashrc
```
[Source](https://community.ald.softbankrobotics.com/en/forum/import-issue-pynaoqi-214-ubuntu-7956)


##### THIS IS NOT NEEDED -- install boost 1.55.0
```
cd && mkdir boost1.55.0 && cd boost1.55.0
wget -O boost_1_55_0.tar.gz http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.gz/download
tar xzvf boost_1_55_0.tar.gz
cd boost_1_55_0/
```
./bootstrap.sh --prefix=/usr/local
./b2
NO sudo ./b2 install
[Source](http://stackoverflow.com/questions/12578499/how-to-install-boost-on-ubuntu)




### Using Python 2.7.13

```
cd /usr/src
sudo su
wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
tar xzf Python-2.7.13.tgz
rm -rf Python-2.7.13.tgz
cd Python-2.7.13
./configure
make altinstall #make altinstall is used to prevent replacing the default python binary file /usr/bin/python.
```
