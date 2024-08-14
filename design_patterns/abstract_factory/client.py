from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from concretefactories import CreditCardPaymentFactory, PixPaymentFactory, BoletoPaymentFactory

# Dictionary to map payment type to the corresponding factory
PAYMENT_FACTORIES = {
    'credit_card': CreditCardPaymentFactory(),
    'pix': PixPaymentFactory(),
    'boleto':BoletoPaymentFactory(),
    # 'paypal': PayPalPaymentFactory(),
    # 'crypto': CryptocurrencyPaymentFactory(),
    # Add other factories as needed
}

class PaymentView(views.APIView):
    def post(self, request):
        payment_type = request.data.get('payment_type')
        factory = PAYMENT_FACTORIES.get(payment_type)

        if not factory:
            return Response({'error': 'Invalid payment type'}, status=status.HTTP_400_BAD_REQUEST)

        # Use the factory to create the serializer and processor
        serializer = factory.create_payment_serializer()
        processor = factory.create_payment_processor()

        # Validate and process payment
        serializer.validate_payment(request.data)
        processor.process_payment(request.data)

        return Response({'message': 'Payment processed successfully'}, status=status.HTTP_200_OK)