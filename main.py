import requests
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
   html_page = requests.get('https://www.isa.gov.il/%D7%92%D7%95%D7%A4%D7%99%D7%9D%20%D7%9E%D7%A4%D7%95%D7%A7%D7%97%D7%99%D7%9D/Corporations/-10/Pages/default.aspx#ResultsArea',verify=False).text
   soup = BeautifulSoup(html_page, 'lxml')
   componies=soup.find_all('td', class_='titlehead')
   for company in componies:
      company_name=company.find('h2').text.strip()
      company_name=company_name[0:(len(company_name)-4)]
      #company_name='אורה סמארט אייר'
      webpage = "https://il.investing.com/"
      searchterm = company_name
      driver = webdriver.Firefox()
      driver.get(webpage)
      time.sleep(3)
      inputElement =driver.find_element(By.XPATH, "/html/body/div[5]/header/div[1]/div/div[3]/div[1]/input")
      inputElement.send_keys(searchterm)
      inputElement.send_keys(Keys.ENTER)

      time.sleep(3)
      link_company = driver.find_element(By.XPATH, '/html/body/div[5]/section/div/div[2]/div[2]/div[1]/a[1]/span[1]')
      link_company.click()
      element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span').text
      print(element)













      




   """HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X)' }
   payload = {'lang': '0', 'qType': '1'}
   json_url = 'https://api.tase.co.il/api/company/tasecompaniesfilter'
   cooky=html_page.cookies['incap_ses_7213_1712163']
   res = requests.get(json_url,headers=HEADERS,params=payload,cookies=cooky)
   res.raise_for_status()
   data = res.json()"""

