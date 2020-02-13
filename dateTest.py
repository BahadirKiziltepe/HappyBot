from datetime import datetime
from time import sleep

lastUpdated=datetime(2020,5,17)
atTheMoment=datetime.now()
if (atTheMoment.month!=lastUpdated.month):
	print ("Update Time!!!!!")
else:
	sleep(2)
