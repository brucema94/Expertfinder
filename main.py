import os
# os.environ["CHROMEDRIVER"] = r"C:\Users\bruce\Downloads\chromedriver_win32"
import sys
sys.path.append(r"C:\Users\bruce\PycharmProjects\ExpertFinder\chromedriver.exe")

from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\bruce\PycharmProjects\ExpertFinder\chromedriver.exe')

from linkedin_scraper import Person, actions
from selenium import webdriver
#driver = webdriver.Chrome()

email = "brucema1994@gmail.com"
password = "mgqst59M"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)




#from linkedin_scraper import Person, actions
#from selenium import webdriver
#driver = webdriver.Chrome()

#email = "some-email@email.address"
#password = "password123"
#actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
#person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)