from safety.limits import applyLimits

wasCharging = False

voltage = 4.1 #for testing

while True:
    wasCharging = applyLimits(voltage, wasCharging, "li-ion")
    