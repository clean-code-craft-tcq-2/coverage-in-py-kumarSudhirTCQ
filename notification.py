from abc import ABC, abstractmethod

class Notification_Sender(ABC):
    
    @abstractmethod
    def notify():
        pass
    
class Send_to_controller(Notification_Sender):
    def notify(breachType):
        header = 0xfeed
        print(f'{header}, {breachType}')
        return 1

class Send_to_email(Notification_Sender):
    def notify(breachType):
        recepient = "sudhirkr7870@live.com"
        if(breachType != 'NORMAL'):
            print(f'To: {recepient}')
            print(f'Hi, the temperature is {breachType.lower()}')
        return 1
  
alertTargetMapper = {'TO_EMAIL': Send_to_email, 'TO_CONTROLLER': Send_to_controller}
class Notifier:
    
    @abstractmethod
    def send_notification(alertTarget, breachType):
        return alertTargetMapper[alertTarget].notify(breachType)