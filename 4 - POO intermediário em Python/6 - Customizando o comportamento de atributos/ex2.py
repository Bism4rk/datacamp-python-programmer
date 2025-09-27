class BankAccount:
  def __init__(self, account_number):
    self.account_number = account_number
  
  def __setattr__(self, name, value):
    if name in ["account_number", "balance"]:
      print(f"{name} is an allowed attribute.")
      self.__dict__[name] = value
    else:
      print(f"Invalid Attribute: {name}")

# Use savings_account and attempt to set attributes
savings_account = BankAccount("12345678")
savings_account.balance = 100
savings_account.beneficiary = "Anna Wu"

'''
O código acima demonstra como usar o método mágico __setattr__ para personalizar o comportamento de atribuição de atributos em uma classe Python. Neste exemplo, a classe BankAccount permite apenas a definição dos atributos account_number e balance. Ao tentar definir qualquer outro atributo, como beneficiary, uma mensagem de erro é exibida, indicando que o atributo é inválido. Isso ajuda a controlar quais atributos podem ser adicionados a instâncias da classe, garantindo maior integridade dos dados.
'''