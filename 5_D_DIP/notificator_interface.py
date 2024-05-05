from abc import ABC, abstractmethod

class NotificatorInterface():

    @abstractmethod
    def send_notification(self, message: str):
        pass