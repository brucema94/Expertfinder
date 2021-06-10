#https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Roel+Verstappen+university+of+Groningen&btnG=

import requests
import time
from bs4 import BeautifulSoup

ProfessorName = "Roel Verstappen"   
CollegeName = "University of Groningen"
ProfessorName = ProfessorName.replace(" ", "+")
CollegeName = CollegeName.replace(" ", "+")
query = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="+ProfessorName+"+"+CollegeName
response = requests.get(query)
soup = BeautifulSoup(response.text,'html.parser')
print(soup)
