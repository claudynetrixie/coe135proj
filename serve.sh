#! /bin/sh

echo $USER

echo "[Unit]" >> authduino.service
echo "Description=Dummy Service" >> authduino.service
echo "After=multi-user.target" >> authduino.service
echo "Conflicts=getty@tty1.service" >> authduino.service
echo " " >> authduino.service
echo " " >> authduino.service
echo "[Service]" >> authduino.service
echo "Type=simple" >> authduino.service
echo "User=$USER" >> authduino.service
echo "ExecStart=/usr/bin/python -u /usr/bin/authduino.py" >> authduino.service
echo " " >> authduino.service
echo " " >> authduino.service
echo "[Install]" >> authduino.service
echo "WantedBy=multi-user.target" >> authduino.service
sudo cp -i authduino.service /lib/systemd/system
rm authduino.service
