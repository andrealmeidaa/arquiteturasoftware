from abc import ABC, abstractmethod

# Abstract factory interface
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment_processor(self):
        pass

    @abstractmethod
    def create_payment_serializer(self):
        pass

# Abstract product interfaces
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, payment_data):
        pass

class PaymentSerializer(ABC):
    @abstractmethod
    def validate_payment(self, payment_data):
        pass
