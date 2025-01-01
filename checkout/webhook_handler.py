from django import Httpresponse

class StripeWH_Handler:
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        return Httpresponse(
            content=f'Webhook received: {event["type"]}', status=200)
    
    def handle_payment_intent_succeeded(self, event):
        return Httpresponse(
            content=f'Payment Intent Succeeded: {event["type"]}', status=200
        )
        
    def handle_payment_intent_payment_failed(self, event):
        return Httpresponse(
            content=f'Payment Intent Failed: {event["type"]}', status=200
        )