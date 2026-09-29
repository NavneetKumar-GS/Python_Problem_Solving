# Abstract Base Classes (Contracts)

# 1.Import ABC and abstractmethod from the abc module.

# 2.Create an abstract class NotificationProvider with an abstract method send(message).

# 3. Create two child classes: WhatsAppNotifier and EmailNotifier. If you do not implement the send method in these child classes, Python should throw an error when you try to instantiate them.

# 4. Create a SystemAlert class that takes a NotificationProvider object in its constructor (Dependency Injection). Its trigger_alert() method should call the .send() method of whatever provider it was given.


