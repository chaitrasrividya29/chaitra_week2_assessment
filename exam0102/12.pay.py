class payment_process:
    def payment(self):
        print("payment process is initiated")
        
class CreditCardPayment(payment_process):
    def payment(self):
        super().payment()
        print("payment is done through CREDIT CARD")
        
class PayPayPayment(payment_process):
    def payment(self):
        super().payment()
        print("payment is done through PAYPAL")
        
class BitCoinPayment(payment_process):
    def payment(self):
        super().payment()
        print("payment is done through BITCOIN")
        
cred=CreditCardPayment()
paypal=PayPayPayment()
Bitcoin=BitCoinPayment()
cred.payment()
paypal.payment()
Bitcoin.payment()