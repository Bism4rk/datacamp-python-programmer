class BankAccount:
  def __init__(self, email):
    self.email = email
    
  @property
  def email(self):
    return f"Email for this account is: {self._email}"
  
  @email.setter
  def email(self, new_email_address):
    if "@" in new_email_address:
      self._email = new_email_address
    else:
      print("Please make sure to enter a valid email.")
  
  # Define a method to be used when deleting the email attribute
  @email.deleter
  def email(self):
    del self._email
    print("Email deleted, make sure to add a new email!")

'''
O código acima demonstra como usar descritores em Python para gerenciar o acesso a um atributo de uma classe. A classe BankAccount possui um atributo privado _email, que é acessado e modificado através do descritor email. Ele inclui métodos para obter, definir e deletar o valor do email, garantindo que o email seja sempre válido (contendo um "@"). O uso do decorador @property permite que o atributo email seja acessado como se fosse um atributo normal, enquanto os decoradores @email.setter e @email.deleter fornecem controle adicional sobre a modificação e remoção do atributo.
'''