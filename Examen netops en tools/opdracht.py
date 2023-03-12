"""
Opdracht:

Bepalingen:
 - Je moet gebruik maken van de aangeleverde variable(n)
 - Je mag deze variable(n) niet aanpassen
 - Het is de bedoeling dat je op het einde 1 programma hebt
 - Inlever datum is zondag avond 13 maart 2023 18:00CET
 - Als inlever formaat wordt een git url verwacht die gecloned kan worden

/ 5 ptn 1 - Maak een public repository aan op jouw gitlab/github account voor dit project
/10 ptn 2 - Gebruik python om de gegeven api url aan te spreken
/20 ptn 3 - Gebruik regex om de volgende data te extracten:
    - Jaar, maand en dag van de created date
    - De provider van de nameservers (bijv voor 'ns3.combell.net' is de provider 'combell')
/15 ptn 4 - Verzamel onderstaande data en output alles als yaml. Een voorbeeld vind je hieronder.
    - Het land van het domein
    - Het ip van het domain
    - De DNS provider van het domein
    - Aparte jaar, maand en dag van de created date


Totaal  /50ptn
"""

""" voorbeeld yaml output

created:
  dag: '18'
  jaar: '2022'
  maand: '02'
ip: 185.162.31.124
land: BE
provider: combell

"""
import re
import yaml
import requests
url = "https://api.domainsdb.info/v1/domains/search?domain=syntra.be"
response = requests.get(f"{url}/broadcast_messages")
print(response.text)

re_datum = r"(?P<jaar>\d{4})-(?P<maand>\d{2})-(?P<dag>\d{2})"
re_nameserver = r"ns3\.(\w+)\b"

datum = re.findall(re_datum, response.text)
nameserver = re.findall(re_nameserver, response.text)
print(datum)
print(nameserver)
with open("data.yml", "r") as f:
  result = yaml.safe_load(f)
print(result)