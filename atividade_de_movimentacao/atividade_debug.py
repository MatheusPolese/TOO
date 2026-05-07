class Pagamento:
    def processar():
        print("")

class CartaoCredito(Pagamento):
    def processar(self):
        print("Pagamento Cartão de Credito")

class CartaoDebito(Pagamento):
    def processar(self):
        print("Pagamento Cartão de Debito")

class Pix(Pagamento):
    def processar(self):
        print("Pagamento via PIX")

class Dinheiro(Pagamento):
    def processar(self):
        print("Pagamento em Dinheiro")



pagamentos = [CartaoCredito(),CartaoDebito(),Pix(),Dinheiro()]

for i in pagamentos:
  i.processar()