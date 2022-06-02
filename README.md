# pylogger:
A simple python keylogger (mouse and keyboard)
you'll need to install the two packages (keyboard, mouse) with the following commands: <br />
```bash
sudo pip2 install keyboard
sudo pip2 install mouse
```
this script registers keys pressed and mouse clicks and sends the resulting file to a mail that was already created for test purposes (projettpsecu@outlook.com, the password is located in the script)
the project was set to work with gmail too, but google eliminated the possiblity to use third party apps (or less secure apps) such as this python script on may, 30th 2022 (three days ago), that is why we changed it to a hotmail account. This should work with other mail providers too.
```bash
sudo python2 pylogger.py
```
# This script should run as sudo. (sudo python2 pylogger.py)

