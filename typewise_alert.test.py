import unittest
import typewise_alert
import notification.test.py

class TypewiseTest(unittest.TestCase):
  def test_check_and_alert(self):
    batteryChar = {'coolingType': 'PASSIVE_COOLING'}
    status = typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 36)
    self.assertTrue(status == 1)
    
    batteryChar = {'coolingType': 'HI_ACTIVE_COOLING'}
    status = typewise_alert.check_and_alert('TO_EMAIL', batteryChar, -1)
    self.assertTrue(status == 1)
    
    batteryChar = {'coolingType': 'MED_ACTIVE_COOLING'}
    status = typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, 0)
    self.assertTrue(status == 1)

if __name__ == '__main__':
  unittest.main()
