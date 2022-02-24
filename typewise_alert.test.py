import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
  def test_check_and_alert(self):
    batteryChar = {'coolingType': 'PASSIVE_COOLING'}
    status = typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 36)
    self.assertTrue(status == 1)
    
    batteryChar = {'coolingType': 'PASSIVE_COOLING'}
    status = typewise_alert.check_and_alert('TO_EMAIL', batteryChar, -36)
    self.assertTrue(status == 1)
    
    batteryChar = {'coolingType': 'PASSIVE_COOLING'}
    status = typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 25)
    self.assertTrue(status == 1)

if __name__ == '__main__':
  unittest.main()
