#task 1

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookSaver:
    def save(self, book):
        print(f"Saving book '{book.title}'...")

class BookPrinter:
    def display(self, book):
        print(f"{book.title} by {book.author}")

class BookUpdater:
    def update(self, book, title, author):
        book.title = title
        book.author = author

book = Book("1984", "George Orwell")
printer = BookPrinter()
printer.display(book)

updater = BookUpdater()
updater.update(book, "Animal Farm", "George Orwell")
printer.display(book)

#task 2

class Payment:
    def pay(self, amount):
        raise NotImplementedError

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} with Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} with PayPal")

class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} with Cryptocurrency")

def process_payment(payment_method, amount):
    payment_method.pay(amount)

process_payment(CreditCardPayment(), 100)
process_payment(PayPalPayment(), 200)
process_payment(CryptoPayment(), 300)

#task 3

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"Email sent: {message}")

class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"SMS sent: {message}")

class PushNotifier(Notifier):
    def notify(self, message):
        print(f"Push Notification sent: {message}")

class NotificationService:
    def __init__(self, notifiers):
        self.notifiers = notifiers

    def send_notifications(self, message):
        for notifier in self.notifiers:
            notifier.notify(message)

service = NotificationService([
    EmailNotifier(),
    SMSNotifier(),
    PushNotifier()
])
service.send_notifications("Подiя сталася!")
