class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  @property
  def balance(self):
    return f"${round(self._balance, 2)}"

  @balance.setter
  def balance(self, new_balance):
    if new_balance > 0:
      self._balance = new_balance

  @balance.deleter
  def balance(self):
    print("Deleting the 'balance' attribute")
    del self._balance

checking_account = BankAccount(100)

# Output the balance of the checking_account object
print(checking_account.balance)

# Set the balance to 150, output the new balance
checking_account.balance = 150
print(checking_account.balance)

# Delete the balance attribute, attempt to print the balance
del checking_account.balance

'''
O códugo acima demonstra como usar descritores em Python para gerenciar o acesso a um atributo de uma classe. A classe BankAccount possui um atributo privado _balance, que é acessado e modificado através do descritor balance. Ele inclui métodos para obter, definir e deletar o valor do saldo, garantindo que o saldo seja sempre positivo. O uso do decorador @property permite que o atributo balance seja acessado como se fosse um atributo normal, enquanto os decoradores @balance.setter e @balance.deleter fornecem controle adicional sobre a modificação e remoção do atributo.
'''