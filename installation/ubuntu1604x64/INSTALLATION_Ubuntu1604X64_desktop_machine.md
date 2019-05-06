Installation on Ubuntu 16.04.2 x64 at Desktop Machine
---


# 1. Create path to have nao software

```
mkdir -p $HOME/hri/naosoftware && cd $HOME/hri/naosoftware
```

# 2. download files


For Python SDK and C++ SDK and other version of Choregraphe, 

Sign in to
https://community.ald.softbankrobotics.com/en/resources/software/robot/nao-2
and download 

* Choregraphe 2.1.4 Linux 64 Binaries
https://community.ald.softbankrobotics.com/en/dl/ZmllbGRfY29sbGVjdGlvbl9pdGVtLTc3OC1maWVsZF9zb2Z0X2RsX2V4dGVybmFsX2xpbmstMC1mMjIwOWY%3D?width=500&height=auto


* Python 2.7 SDK 2.1.4 Linux 64
https://community.ald.softbankrobotics.com/en/dl/ZmllbGRfY29sbGVjdGlvbl9pdGVtLTc5MS1maWVsZF9zb2Z0X2RsX2V4dGVybmFsX2xpbmstMC01ZTRiYTE%3D?width=500&height=auto


* naoqi-sdk-2.1.4.13-linux64.tar.gz



```
├── [  430850260]  choregraphe-suite-2.1.4.13-linux64.tar.gz
├── [  333867205]  naoqi-sdk-2.1.4.13-linux64.tar.gz
└── [   11753966]  pynaoqi-python2.7-2.1.4.13-linux64.tar.gz
```




# 3. choregraphe installation


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




# 4. naoqi installation 


```
tar -xvzf naoqi-sdk-2.1.4.13-linux64.tar.gz
tar -xvzf pynaoqi-python2.7-2.1.4.13-linux64.tar.gz
```


# 5. export libs

```
cd $HOME/hri/naosoftware

echo 'export PYTHONPATH=${PYTHONPATH}:$HOME/hri/naosoftware/pynaoqi-python2.7-2.1.4.13-linux64' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="$HOME/hri/naosoftware/naoqi-sdk-2.1.4.13-linux64:$LD_LIBRARY_PATH"' >> ~/.bashrc
sudo ldconfig
sudo cp -a $HOME/hri/naosoftware/naoqi-sdk-2.1.4.13-linux64/lib/libboost_*.so.* $HOME/hri/naosoftware/naoqi-sdk-2.1.4.13-linux64/
source ~/.bashrc
```
[Source](https://community.ald.softbankrobotics.com/en/forum/import-issue-pynaoqi-214-ubuntu-7956)




# 6. IP Configuration

## Ubuntu Local Link [ref](http://doc.aldebaran.com/2-1/nao/connectivity.html#how-to-ubuntu-and-local-link)
1. Edit connections  
2. Add Ethernet Connection Type [CREATE]
3. Select the tab IPv4-Settings, and change the Method (Automatic DHCP) to (Link-Local Only).
   (Change connection name to NAO)
   and tick Require IPv4 addressing for this connection to complete
4. Click on Save, and close the menu.


## Network Connection

Add a rule for the firewall: 

```
sudo ufw allow in on eth0 from 169.254.0.0/16
```
In case that you need to rename the network interface on Ubuntu 16.04, you can follow this instructions:
[SOURCE](https://askubuntu.com/questions/783457/renaming-network-interface-in-ubuntu-16-04-with-systemd-fails)



For IP Configuration, go to network connections and select connect to NAO, once established the connection,
you can run

```
ip address list


2: enp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether e8:03:9a:b4:a3:4b brd ff:ff:ff:ff:ff:ff
    inet 169.254.228.66/16 brd 169.254.255.255 scope link enp2s0
       valid_lft forever preferred_lft forever
    inet6 fe80::73e1:4cb0:ee78:4d7c/64 scope link 
       valid_lft forever preferred_lft forever

```

```
ip r

169.254.0.0/16 dev enp2s0  proto kernel  scope link  src 169.254.228.66  metric 100 
169.254.0.0/16 dev wlp1s0  scope link  metric 1000 

```











# TESTING


## With choregraphe
```

cd $HOME/hri/naosoftware/choregraphe-suite-2.1.4.13-linux64
./choregraphe
```

1. connect to ...
2. nao.local
3. Open project
4. Upload to the robot and play
5. Stop and disconnect


## With python
```
cd $HOME/hri/nao/examples/python/testing 
$ python sayingsth.py
[I] 5131 qimessaging.session: Session listener created on tcp://0.0.0.0:0
[I] 5131 qimessaging.transportserver: TransportServer will listen on: tcp://169.254.164.69:39124
[I] 5131 qimessaging.transportserver: TransportServer will listen on: tcp://127.0.0.1:39124
sys.version_info(major=2, minor=7, micro=12, releaselevel='final', serial=0)
```


DONE :-)
Mon  6 May 03:18:09 BST 2019
@UoB UK
