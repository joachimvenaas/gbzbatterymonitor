"""
" Edit below this line to fit your needs
"""
# Path to pngview (raspidmx) and icons
PNGVIEWPATH = "/home/pi/raspidmx/pngview"
ICONPATH = "/home/pi/gbzbattery/icons"

# Battery icon or LED? Or both?
LEDS = 1
ICON = 1
CLIPS = 1

# GPIO (BOARD numbering scheme) pin for good voltage LED
GOODVOLTPIN = 16
LOWVOLTPIN = 15

# Fully charged voltage (for a single battery); 
#   i.e. 1.4V for a NiMH battery, or 4.2V for a LiPo battery
VOLT100 = 4.1
VOLT75 = 3.76
VOLT50 = 3.63
VOLT25 = 3.5
VOLT0 = 3.2

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
SVOLT100 = (VOLT100)*(HIGHRESVAL)/(LOWRESVAL+HIGHRESVAL)
SVOLT75 = (VOLT75)*(HIGHRESVAL)/(LOWRESVAL+HIGHRESVAL)
SVOLT50 = (VOLT50)*(HIGHRESVAL)/(LOWRESVAL+HIGHRESVAL)
SVOLT25 = (VOLT25)*(HIGHRESVAL)/(LOWRESVAL+HIGHRESVAL)
SVOLT0 = (VOLT0)*(HIGHRESVAL)/(LOWRESVAL+HIGHRESVAL)

# ADC voltage reference (3.3V for Raspberry Pi)
ADCVREF = 3.3

# MCP3008 channel to use (from 0 to 7)
ADCCHANNEL = 0

# MCP3008 scaling
ADC100 = SVOLT100 / (ADCVREF / 1024.0)
ADC75 = SVOLT75 / (ADCVREF / 1024.0)
ADC50 = SVOLT50 / (ADCVREF / 1024.0)
ADC25 = SVOLT25 / (ADCVREF / 1024.0)
ADC0 = SVOLT0 / (ADCVREF / 1024.0)

# Refresh rate (s)
REFRESH_RATE = 2

# Display some debug values when set to 1, and nothing when set to 0
DEBUGMSG = 0
