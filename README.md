# meter data analytics
Open Source project to generator device energy consumption from (P1) meter data 

## installation

To install the p1 USB reader run the following commands

"git clone https://github.com/arnekaas/meterdataanalytics/"

"crontab -e" and the add "@reboot /usr/bin/python /path/to/loggers/usb_p1_logger/schedule_p1_reader.py 2>&1" to run the script after each reboot. The file will record alle data every 10 seconds, which leads to about 1Mb per day. Make sure you have enough space

## hardware requirements
- raspberry pi
- usb to serial cable (https://www.sossolutions.nl/slimme-meter-kabel)

## data storage
The data will be stored to a sqlite file 'data/yourmeterserialnumber.db'

# disaggregation
This repository will soon be updates with a working disaggregation model that determines which subload are behind your meter.

