
from abstractfactories import PaymentFactory, PaymentProcessor, PaymentSerializer
# Produto concreto para processar cartão de crédito
class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, payment_data):
        # Implementar a lógica de processamento de pagamento aqui
        print("Processing credit card payment...")

class CreditCardPaymentSerializer(PaymentSerializer):
    def validate_payment(self, payment_data):
        # Implementar a lógica de validação de pagamento aqui
        print("Validating credit card payment data...")

# Fábrica concreta para o cartão de crédito
class CreditCardPaymentFactory(PaymentFactory):
    def create_payment_processor(self):
        return CreditCardPaymentProcessor()

    def create_payment_serializer(self):
        return CreditCardPaymentSerializer()

#Implementando outro produto

# Produtos

class PixPaymentProcessor(PaymentProcessor):
    def process_payment(self, payment_data):
        # Implement payment processing logic here
        print("Processing pix payment...")

class PixPaymentSerializer(PaymentSerializer):
    def validate_payment(self, payment_data):
        # Implement payment data validation logic here
        print("Validating pix payment data...")

# Fabrica
class PixPaymentFactory(PaymentFactory):
    def create_payment_processor(self):
        return PixPaymentProcessor()

    def create_payment_serializer(self):
        return PixPaymentSerializer()

#Boleto

class BoletoPaymentProcessor(PaymentProcessor):
    def process_payment(self, payment_data):
        # Implement payment processing logic here
        print("Processing boleto payment...")
class BoletoPaymentSerializer(PaymentSerializer):
    def validate_payment(self, payment_data):
        # Implement payment data validation logic here
        print("Validating boleto payment data...")

class BoletoPaymentFactory(PaymentFactory):
    def create_payment_processor(self):
        return BoletoPaymentProcessor()

    def create_payment_serializer(self):
        return BoletoPaymentSerializer()