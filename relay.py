#relay
from gpiozero import OutputDevice
from time import sleep
from datetime import datetime
import sys

RELAY_1_PIN = 18

relay = OutputDevice(RELAY_1_PIN, active_high=False, initial_value=False)

def setLight():
	currentTime = datetime.now()
	startTime = datetime.now().replace(hour=10, minute=0, second=0)
	endTime = datetime.now().replace(hour=22, minute=0, second=0)
	if startTime <= currentTime and currentTime <= endTime:
		if relay.value == 0:
			relay.on()
	else:
		if relay.value == 1:
			relay.off()
	#print(relay.value)
	sleep(1)


def mainLoop():
	while True:
		setLight()

if __name__ == "__main__":
	try:
		mainLoop()
	except KeyboardInterrupt:
		print("Konec")
		sys.exit(0)
