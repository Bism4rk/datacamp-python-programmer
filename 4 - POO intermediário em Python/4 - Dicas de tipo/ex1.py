# Import Dict and List from typing
from typing import Dict, List

# Type hint the roster of codenames and number of missions
roster: Dict[str, int] = {
  "Chuck": 37,
  "Devin": 2,
  "Steven": 4
}

# Unpack the values and add type hints for the new list
agents: List[str] = [
  f"Agent {agent}, {missions} missions" for agent, missions in roster.items()
]

'''
O código acima demonstra como usar dicas de tipo (type hints) em Python para melhorar a legibilidade e manutenção do código. Ele importa os tipos `Dict` e `List` do módulo `typing`, define um dicionário `roster` com codenomes de agentes e o número de missões realizadas, e cria uma lista `agents` formatada com essas informações. As dicas de tipo ajudam a esclarecer que `roster` é um dicionário com chaves do tipo `str` e valores do tipo `int`, enquanto `agents` é uma lista de strings.
'''