"""
" Edit below this line to fit your needs
"""
# Path to pngview (raspidmx) and icons
PNGVIEWPATH = "/home/pi/raspidmx/pngview"
ICONPATH = "/home/pi/gbzbattery/icons"

# Battery icon or LED? Or both?
LEDS = 1
ICON = 1

# GPIO (BOARD numbering scheme) pin for good voltage LED
GOODVOLTPIN = 16
LOWVOLTPIN = 15

# Fully charged voltage (for a single battery); 
#   i.e. 1.4V for a NiMH battery, or 4.2V for a LiPo battery
FULLBATVOLT = 4.1

# Discharged voltage (for a single battery); 
#   i.e. 1.05V for a NiMH battery, or 3.4V for a LiPo battery#   You should use a conservative value in order to avoid destructive
#   discharging
LOWBATVOLT = 3.4

# Dangerous voltage (for a single battery);
#   i.e. 1.0V for a NiMH battery, or 3.2V for a LiPo battery
#   You should really not go below this voltage.
DNGBATVOLT = 3.2

# Value (in ohms) of the lower resistor from the voltage divider, connected to
#   the ground line (1 if no voltage divider). Default value (3900) is for a 
#   battery pack of 8 NiMH batteries, providing 11.2V max, stepped down to about
#   3.2V max.
LOWRESVAL = 2000

# Value (in ohms) of the higher resistor from the voltage divider, connected to 
#   the positive line (0 if no voltage divider). Default value (10000) is for a
#   battery pack of 8 NiMH batteries, providing 11.2V max, stepped down to about
#   3.2V max.
HIGHRESVAL = 5600

# Voltage value measured by the MCP3008 when batteries are fully charged
# It should be near 3.3V due to Raspberry Pi GPIO compatibility)
VHIGHBAT = (FULLBATVOLT)*(HIGHRESVAL)/(LOWRESVAL+HIGHRESVAL)

# Voltage value measured by the MCP3008 when batteries are discharged
VLOWBAT = (LOWBATVOLT)*(HIGHRESVAL)/(LOWRESVAL+HIGHRESVAL)

# Voltage value measured by the MCP3008 when batteries voltage is dangerously
#   low
VDNGBAT = (DNGBATVOLT)*(HIGHRESVAL)/(LOWRESVAL+HIGHRESVAL)

# ADC voltage reference (3.3V for Raspberry Pi)
ADCVREF = 3.3

## Define expected ADC values
# MCP23008 channel to use (from 0 to 7)
ADCCHANNEL = 0

# MCP23008 should return this value when batteries are fully charged
#  * 3.3 is the reference voltage (got from Raspberry Pi's +3.3V power line)
#  * 1024.0 is the number of possible values (MCP23008 is a 10 bit ADC)
ADCHIGH = VHIGHBAT / (ADCVREF / 1024.0)
ADCLOW = VLOWBAT / (ADCVREF / 1024.0)
ADCDNG = VDNGBAT / (ADCVREF / 1024.0)

# Refresh rate (s)
REFRESH_RATE = 2

# Display some debug values when set to 1, and nothing when set to 0
DEBUGMSG = 0
