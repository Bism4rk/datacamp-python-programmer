from abc import ABC, abstractmethod

class LLM(ABC):
  @abstractmethod
  def complete_sentence(self, prompt):
    pass

class OpenAI(LLM):
  def complete_sentence(self, prompt):
    return prompt + " ... OpenAI end of sentence."
  
class Anthropic(LLM):
  def complete_sentence(self, prompt):
    return prompt + " ... Anthropic end of sentence."

class ChatBot:
  def _get_llm(self, provider):
    if provider == "OpenAI":
      return OpenAI()
    elif provider == "Anthropic":
      return Anthropic()
      
  def chat(self, prompt, provider):
    # Return an llm object, then call complete_sentence()
    llm = self._get_llm(provider)
    return llm.complete_sentence(prompt) # type: ignore

'''
O código acima demonstra como implementar métodos de fábrica em Python usando classes abstratas e herança. Ele define uma interface comum para diferentes tipos de clientes (membros de recompensas e novos clientes) e utiliza um método de fábrica para instanciar o tipo correto de cliente com base na entrada fornecida. A classe Checkout gerencia o processo de pagamento, delegando a responsabilidade ao objeto cliente apropriado.
'''