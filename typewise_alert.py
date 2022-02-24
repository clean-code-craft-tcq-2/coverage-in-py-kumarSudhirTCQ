from notification import*
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = 0
  upperLimit = 0
  if coolingType == 'PASSIVE_COOLING':
    lowerLimit = 0
    upperLimit = 35
  elif coolingType == 'HI_ACTIVE_COOLING':
    lowerLimit = 0
    upperLimit = 45
  elif coolingType == 'MED_ACTIVE_COOLING':
    lowerLimit = 0
    upperLimit = 40
  return infer_breach(temperatureInC, lowerLimit, upperLimit)

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  return Notifier.send_notification(alertTarget, breachType)
