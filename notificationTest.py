import unittest
from notification import*

class NotificationTest(unittest.TestCase):
    
    def test_notifier(self):
        
        # check for notification send by email
        alertTarget = 'TO_EMAIL'
        breachType = 'TOO_HIGH'
        result = Notifier.send_notification(alertTarget, breachType)
        self.assertTrue(result == 1)
        
        # check for notification send by email with message NORMAL
        alertTarget = 'TO_EMAIL'
        breachType = 'NORMAL'
        result = Notifier.send_notification(alertTarget, breachType)
        self.assertTrue(result == 1)
        
        # check for notification send to contoller
        alertTarget = 'TO_CONTROLLER'
        breachType = 'TOO_HIGH'
        result = Notifier.send_notification(alertTarget, breachType)
        self.assertTrue(result == 1)
