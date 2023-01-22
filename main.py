import requests
from bs4 import BeautifulSoup

#faz o web-scrapping da página da cotação
link = 'https://www.x-rates.com/calculator/?from=BRL&to=USD&amount='
d = requests.get(link)
sopa = BeautifulSoup(d.content, 'html.parser')
res = sopa.find("span", {"class": "ccOutputRslt"}).text

#deleta o USD para tornar possível transformar a string em float
delus = 'USD'
subus = ''
res = res.replace(delus, subus)

#processo principal
while True:
  req = int(input("Qual o valor que você deseja converter para dólar?\n"))
  if req < 0:
    print("Tente novamente")
  else:
    tot = float(req) * float(res)
    print(round(tot, 2))
    a = input("Deseja converter outro valor?\nPressione qualquer tecla caso sim ou digite sair caso não\n")
    if a == 'sair' or a == 'Sair':
      quit()
  
    