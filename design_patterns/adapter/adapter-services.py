class PaymentProcessor:
    def process_payment(self, amount):
        # Process the payment through the current system
        print(f"Processing payment of {amount} through the current system.")

class NewPaymentService:
    def execute_payment(self, payment_details):
        # New payment service logic
        print(f"Executing payment of {payment_details['amount']} with {payment_details['method']}.")

class PaymentServiceAdapter(PaymentProcessor):
    def __init__(self, new_payment_service):
        self.new_payment_service = new_payment_service

    def process_payment(self, amount):
        payment_details = {
            'amount': amount,
            'method': 'New Method'
        }
        self.new_payment_service.execute_payment(payment_details)

class PaymentView(views.APIView):
    def post(self, request, *args, **kwargs):
        amount = request.data.get("amount")
      #  payment_processor = PaymentServiceAdapter(NewPaymentService())
        payment_processor=PaymentProcessor()
        payment_processor.process_payment(amount)
        return Response({"status": "Payment processed successfully"})
