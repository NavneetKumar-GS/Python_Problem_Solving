# Abstract Base Classes (Contracts)

# 1.Import ABC and abstractmethod from the abc module.

# 2.Create an abstract class NotificationProvider with an abstract method send(message).

# 3. Create two child classes: WhatsAppNotifier and EmailNotifier. If you do not implement the send method in these child classes, Python should throw an error when you try to instantiate them.

# 4. Create a SystemAlert class that takes a NotificationProvider object in its constructor (Dependency Injection). Its trigger_alert() method should call the .send() method of whatever provider it was given.


from abc import ABC, abstractmethod


class NotificationProvider(ABC):

    @abstractmethod
    def send(self,message):
        pass


class WhatsAppNotifier(NotificationProvider):

    def send(self,message):
        print(print(f"Sending WhatsApp message: {message}"))

class EmailNotifier(NotificationProvider):

    def send(self, message):
        print(f"[SMTP Server] Sending: {message}")

class SystemAlert:

    def __init__(self, provider: NotificationProvider):

        self.provider = provider

    def trigger_alert(self, issue):

        self.provider.send(f"SYSTEM ALERT: {issue}")



wa_provider = WhatsAppNotifier()
alert_system = SystemAlert(wa_provider)
alert_system.trigger_alert("Server CPU at 99%") 


email_provider = EmailNotifier()
alert_system2 = SystemAlert(email_provider)
alert_system2.trigger_alert("Database connection lost")