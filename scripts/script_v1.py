#!/usr/bin/python3
from time import asctime, localtime
from datetime import datetime
from zoneinfo import ZoneInfo




if __name__ == "__main__":
    #print(2+40)
    #print("Hello, World!")
    print(asctime(localtime()))
    berlin_time = datetime.now(ZoneInfo("Europe/Berlin"))
    print(berlin_time.strftime("%Y-%m-%d %H:%M:%S"))
