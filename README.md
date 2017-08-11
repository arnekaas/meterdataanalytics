# meter data analytics
Open Source project to generator device energy consumption from (P1) meter data 

## installation

To install the p1 USB reader run the following commands

"apt-get https://github.com/arnekaas/meterdataanalytics/loggers/usblogger"
"crontab -e" and the add "* * * * * /usr/bin/python /path/to/usblogger/p1logger.py" to run the script every minute

## hardware requirements
- raspberry pi
- usb to serial cable (https://www.sossolutions.nl/slimme-meter-kabel)

## data storage
The data will be stored to a sqlite file 'yourmeterserialnumber.db'
