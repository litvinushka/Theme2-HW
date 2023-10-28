from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_commands(self):
        pass

    @abstractmethod
    def display_message(self, message):
        pass