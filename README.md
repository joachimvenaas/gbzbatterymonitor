# gbzbatterymonitor

# Installation

## Hardware part
1. Buy a MCP3008 and some resistors suitable for this project, you can calculate resistor value here http://www.raltron.com/cust/tools/voltage_divider.asp, Vin = 4.2V and Vout needs to be maximum 3.3V

## Software part
1. Install https://github.com/AndrewFromMelbourne/raspidmx/ and compile it by using `make`
2. Install this script by running the following command from terminal or ssh: `git clone https://github.com/joachimvenaas/gbzbatterymonitor`
3. Navigate into the gbzbatterymonitor folder: `cd gbzbatterymonitor`
4. Edit the config by typing `nano config.py` Here you must edit the battery voltages to suit your needs and add the resistor values.
5. Test the script by running command: `python main.py`
6. If the script runs as desired you can close it by pressing Ctrl+C
7.
#### Optional


##### Sources and inspiration:
https://github.com/aboudou/picheckvoltage
https://github.com/Camble/GBZ-Power-Monitor_PB
https://github.com/AndrewFromMelbourne/raspidmx/
