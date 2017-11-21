
notddc@notddc000000:~$ clear
notddc@notddc000000:~$ sudo systemctl stop workserver
notddc@notddc000000:~$ ls
notddc@notddc000000:~$ ls /srv
workserver
notddc@notddc000000:~$ more workserver
more: stat of workserver failed: No such file or directory
notddc@notddc000000:~$ cd workserver
-bash: cd: workserver: No such file or directory
notddc@notddc000000:~$ ls
notddc@notddc000000:~$ cd /srv/workserver
notddc@notddc000000:/srv/workserver$ ls
workserver.py
notddc@notddc000000:/srv/workserver$ nano workserver.py
notddc@notddc000000:/srv/workserver$ more workserver.py
more: cannot open workserver.py: Permission denied
notddc@notddc000000:/srv/workserver$ sudo more workserver.py

notddc@notddc000000:/srv/workserver$  python3 workserver.py
python3: can't open file 'workserver.py': [Errno 13] Permission denied
notddc@notddc000000:/srv/workserver$ sudo py
py3clean             pycompile            pygettext            python2              python3-jsondiff
py3compile           pydoc                pygettext2.7         python2.7            python3-jsonpatch
py3versions          pydoc2.7             pygettext3           python3              python3-jsonpointer
pybuild              pydoc3               pygettext3.5         python3.5            python3m
pyclean              pydoc3.5             python               python3.5m           pyversions

notddc@notddc000000:/srv/workserver$ sudo python3 workserver.py
Traceback (most recent call last):
  File "workserver.py", line 7, in <module>
    from azure.servicebus import ServiceBusService, Message, Queue
ImportError: No module named 'azure'

notddc@notddc000000:/srv/workserver$ sudo apt-get install python3-pip
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package python3-pip is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source
E: Package 'python3-pip' has no installation candidate




notddc@notddc000000:/srv/workserver$ pip3 install azure
The program 'pip3' is currently not installed. You can install it by typing:
sudo apt install python3-pip
notddc@notddc000000:/srv/workserver$ sudo apt-get install python3-pip

notddc@notddc000000:/srv/workserver$ sudo apt-get install python3-pip
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package python3-pip is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'python3-pip' has no installation candidate
notddc@notddc000000:/srv/workserver$ uname -a
Linux notddc000000 4.11.0-1014-azure #14-Ubuntu SMP Tue Oct 17 12:10:56 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
notddc@notddc000000:/srv/workserver$ which python3
/usr/bin/python3
notddc@notddc000000:/srv/workserver$ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
notddc@notddc000000:/srv/workserver$ sudo apt-get update

notddc@notddc000000:/srv/workserver$ sudo apt-get install gfortran

notddc@notddc000000:/srv/workserver$ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import bottle
>>> import requests
>>> exit()
notddc@notddc000000:/srv/workserver$ pip3
The program 'pip3' is currently not installed. You can install it by typing:
sudo apt install python3-pip
notddc@notddc000000:/srv/workserver$ sudo apt install gfortran

notddc@notddc000000:/srv/workserver$ sudo apt install python3-pip

notddc@notddc000000:/srv/workserver$ sudo apt install gfortran


