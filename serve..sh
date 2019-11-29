#! /bin/sh
echo "[Unit]\nDescription=Dummy Service\nAfter=multi-user.target\nConflicts=getty@tty1.service\n\n[Service]\nType=simple\nUser=$USER\nExecStart=/usr/bin/python -u /usr/bin/authduino.py\n\n[Install]\nWantedBy=multi-user.target"  > test.service
echo $USER
