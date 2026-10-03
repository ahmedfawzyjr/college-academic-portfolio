# 01_solid_principles.py - Demonstrating Single Responsibility & Open/Closed Principle

class NotificationService:
    def send(self, message: str, recipient: str):
        raise NotImplementedError

class EmailNotification(NotificationService):
    def send(self, message: str, recipient: str):
        print(f"Sending Email to {recipient}: {message}")

class SMSNotification(NotificationService):
    def send(self, message: str, recipient: str):
        print(f"Sending SMS to {recipient}: {message}")

if __name__ == "__main__":
    notifier: NotificationService = EmailNotification()
    notifier.send("Your assignment has been submitted successfully.", "student@university.edu")
