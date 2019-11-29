#! /bin/sh
unzip Authduino.zip
remove Authduino.zip
cp -i -R  Authduino /home/$USER
cd /home/$USER/Authduino
mkdir /home/$USER/AuthduinoDocs

sudo cp -i /home/$USER/Authduino/authduino.py /usr/bin

sudo chmod +r /usr/bin/authduino.py
