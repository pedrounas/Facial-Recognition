from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

user_name = "up201606726"
password = ""
driver = webdriver.Firefox()
driver.get("https://sigarra.up.pt/fcup/pt/WEB_PAGE.INICIAL")
element = driver.find_element_by_id("user")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(5) #para só avançar quando tiver feito mesmo o login 


#50 alunos, posteriormente pedir como argumento ou usar o scraper para buscar numero de alunos
for i in range (2,52):
	driver.get("https://sigarra.up.pt/fcup/pt/fest_geral.estudantes_inscritos_list?pv_ocorrencia_id=445367")
	element=driver.find_element_by_xpath("//*[@id='conteudoinner']/table/tbody/tr["+str(i)+"]/td[1]/a")
	element.click()
	time.sleep(5)
	#print(driver.page_source)
	url = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[3]/div/div[2]/div/div[1]/div/img").get_attribute("src")
	#falta fazer download da imagem
	urllib.request.urlretrieve(url, "local-filename.jpg")
	break



