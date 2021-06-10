import sys
sys.path.append(r"C:\Users\bruce\PycharmProjects\ExpertFinder\chromedriver.exe")

from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\bruce\PycharmProjects\ExpertFinder\chromedriver.exe')

from linkedin_scraper import Person, actions
#from linkedin_scraper import Company

#PWD
from yaml import load as load_yaml
def config_loader(path):
    with open(path) as f:
        raw_dict = load_yaml(f)
    return  {key:raw_dict[key]['value'] for key in raw_dict.keys()}
config = config_loader("PassWD.yaml")


# personal login
email = "brucema1994@gmail.com"
password = config["PWD"]
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal

#https://
#Person(linkedin_url="https://www.linkedin.com/in/armandofox", name=None, about=[], experiences=[], educations=[], interests=[], accomplishments=[], company=None, job_title=None, driver=driver, scrape=True)
person = Person("https://www.linkedin.com/in/laura-hall-1484034", driver = driver, scrape=True,close_on_complete=False)
#company = Company("https://www.linkedin.com/company/chocolate-company-caf%C3%A9-groningen/", driver = driver)
print(person)

