NAO ()° .°)
---
My [Repository](https://github.com/mxochicale/nao.git) for
[NAO ()° .°) ](https://en.wikipedia.org/wiki/Nao_(robot))


## Version and Body Type
NAO V4  
MODEL T14  
http://doc.aldebaran.com/2-1/family/body_type.html  


## on Ubuntu 14.04 x64


```
$ cat /proc/version
Linux version 3.13.0-117-generic (buildd@lgw01-18)
(gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3) )
#164-Ubuntu SMP Fri Apr 7 11:05:26 UTC 2017
```

```
$ cat /etc/*release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=14.04
DISTRIB_CODENAME=trusty
DISTRIB_DESCRIPTION="Ubuntu 14.04.5 LTS"
NAME="Ubuntu"
VERSION="14.04.5 LTS, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 14.04.5 LTS"
VERSION_ID="14.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
```

* gcc --version
gcc (Ubuntu 4.8.4-2ubuntu1~14.04.3) 4.8.4

* boost version:

dpkg -s libboost-dev | grep 'Version'
Version: 1.54.0.1ubuntu1


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


```
cd choregraphe-suite-2.1.4.13-linux64
 ./choregraphe
```

# Ubuntu Local Link
1. Edit connections  
2. Add Ethernet Connection Type 
3. Select the tab IPv4-Settings, and change the Method to Link-Local Only.
   (Change connection name: NAO)
   and tick Require IPv4 addressing for this connection to complete 
4. Click on Save, and close the menu.


http://doc.aldebaran.com/2-1/nao/connectivity.html#how-to-ubuntu-and-local-link

# IP Configuration


Add a rule for the firewall

```
$ sudo ufw allow in on eth0 from 169.254.0.0/16
```
```
$ ufw status

  Anywhere on eth0           ALLOW       169.254.0.0/16
```


```
$ ip address list
2: em1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 70:71:bc:6b:0a:c5 brd ff:ff:ff:ff:ff:ff
    inet 169.254.8.44/16 brd 169.254.255.255 scope global em1
       valid_lft forever preferred_lft forever
    inet6 fe80::7271:bcff:fe6b:ac5/64 scope link
       valid_lft forever preferred_lft forever

$ ip r
 169.254.0.0/16 dev em1  proto kernel  scope link  src 169.254.8.44  metric 1
```

To change the interface from em1 to eth0, you can follow this instructions
[REF](https://askubuntu.com/questions/680409/problems-setting-up-internet-connection-ubuntu-server-14-04-no-eth0) [REF](https://ask.openstack.org/en/question/59639/how-to-change-interface-from-em1-to-eth0-linux-1404-lts/):  


Edit /etc/default/grub and add biosdevname=0 to the following variables
```
original:
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
to:
GRUB_CMDLINE_LINUX_DEFAULT="biosdevname=0"
GRUB_CMDLINE_LINUX="biosdevname=0"
```
Then run
```
sudo update-grub
reboot
```


```
$ ip address list
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 70:71:bc:6b:0a:c5 brd ff:ff:ff:ff:ff:ff
    inet 169.254.8.44/16 brd 169.254.255.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::7271:bcff:fe6b:ac5/64 scope link
       valid_lft forever preferred_lft forever
```


## Installation of Python 2.7 SDK 2.1.4 Linux 64
[Retrieving software](http://doc.aldebaran.com/2-1/dev/community_software.html#retrieving-software)
[General Instructions](http://doc.aldebaran.com/2-1/dev/python/install_guide.html#linux)

```
tar -xvzf pynaoqi-python2.7-2.1.4.13-linux64.tar.gz
rm pynaoqi-python2.7-2.1.4.13-linux64.tar.gz
echo 'export PYTHONPATH=${PYTHONPATH}:/home/map479-admin/naosoftware/pynaoqi-python2.7-2.1.4.13-linux64' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="/home/map479-admin/naosoftware/naoqi-sdk-2.1.4.13-linux64:$LD_LIBRARY_PATH"' >> ~/.bashrc
sudo ldconfig
source ~/.bashrc
```



There is a problem when importing naoqi
```
$ python
Python 2.7.13 (default, Apr 19 2017, 16:11:37)
[GCC 4.8.4] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import naoqi
Segmentation fault (core dumped)
```

Trying Solution 1: http://stackoverflow.com/questions/38705150/naoqi-library-to-python-sdk-in-ubuntu
```
echo 'export PYTHONPATH=$PYTHONPATH:/home/map479-admin/naosoftware/pynaoqi-python2.7-2.1.4.13-linux64' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/map479-admin/naosoftware/pynaoqi-python2.7-2.1.4.13-linux64' >> ~/.bashrc
source ~/.bashrc
```

By the way, libboost-dev Version is 1.54.0.1ubuntu1

then I tried this but 
```
sudo cp -a /home/map479-admin/naosoftware/naoqi-sdk-2.1.4.13-linux64/lib/libboost_*.so.* /home/map479-admin/naosoftware/naoqi-sdk-2.1.4.13-linux64/
```
but it still the same error:

Segmentation fault (core dumped)





## Using  C++ SDK 2.1.4 Linux 64  
http://doc.aldebaran.com/2-1/dev/cpp/install_guide.html#c-sdk-installation

Extract naoqi-sdk-2.1.4.13-linux64.tar.gz
```
tar -xvzf naoqi-sdk-2.1.4.13-linux64.tar.gz
```



### TODO

* Cross Toolchain 2.1.4 Linux 64  




# on Ubuntu 16.04.4 x64


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





# IP Configuration

```
$ ip address list
3: enp5s0f1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:1e:67:56:d0:ab brd ff:ff:ff:ff:ff:ff
    inet 169.254.52.160/16 brd 169.254.255.255 scope link enp5s0f1
       valid_lft forever preferred_lft forever
    inet6 fe80::68b8:b68:9cd2:eed1/64 scope link 
       valid_lft forever preferred_lft forever
```
You might rename the network interface on Ubuntu 16.04
[SOURCE](https://askubuntu.com/questions/783457/renaming-network-interface-in-ubuntu-16-04-with-systemd-fails)




###  Installation of Python 2.7 SDK 2.1.4 Linux 64
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


#### THIS IS NOT NEECESARY -- install boost 1.55.0 
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




Using Python 2.7.13

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




