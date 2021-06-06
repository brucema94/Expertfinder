import requests
import time
from bs4 import BeautifulSoup

def ProfessorLunkedInScrapper(
  ProfessorName,CollegeName 
):
  #ProfessorName = "Steven Pinker"   
  #CollegeName = "Harvard"
  query = 'https://google.com/search?q=site:linkedin.com/in AND "'+ProfessorName+'" AND "'+CollegeName+'"'
  
  response = requests.get(query)
  soup = BeautifulSoup(response.text,'html.parser')
  print(soup)
  for anchor in soup.find_all('a'):
    url = anchor["href"]
    if 'https://www.linkedin.com/' in url:
      url = url[7:url.find('&')]
      print(url)
      time.sleep(1)
      return url