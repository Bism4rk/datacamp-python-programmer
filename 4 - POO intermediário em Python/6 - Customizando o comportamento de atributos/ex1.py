class BankAccount:
  def __init__(self, account_number):
    self.account_number = account_number
  
  # Define a magic method to handle references to attribute
  # not in an object's namespace
  def __getattr__(self, name):
    # Output a message to instruct further action
    print(f"""{name} is not defined in BankAccount object.
    	Please define this attribute if needed.""")
    
# Create a BankAccount object, reference routing_number
checking_account = BankAccount("123456")
checking_account.routing_number

'''
O código acima demonstra como usar o método mágico __getattr__ para personalizar o comportamento de atributos em uma classe Python. Quando um atributo que não existe é acessado, o método __getattr__ é chamado, permitindo que você defina uma ação personalizada, como exibir uma mensagem informativa. Neste exemplo, ao tentar acessar o atributo routing_number, que não foi definido na classe BankAccount, a mensagem personalizada é exibida, orientando o usuário a definir o atributo se necessário.
'''