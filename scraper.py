from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request 
import os
import requests

user_name = "up201606726"
password = "Chitaveloz98"
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
	img_url = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[3]/div/div[2]/div/div[1]/div/img").get_attribute("src")
	#o link da imagem esta certo
	print(img_url)
	img_name = str(i)+"jpg"
	##Método1 - dá forbidden

	#urlretrieve(image, "student"+str(i)+".jpg")
	##Método2 - dá uma imagem sem cara
		
	#r = requests.get(img_url,
                 #stream=True, headers={'User-agent': 'Mozilla/5.0'})
	#if r.status_code == 200:
		#with open(img_name, 'wb') as f:
			#r.raw.decode_content = True
			#shutil.copyfileobj(r.raw, f)
	##Método3 - dá forbidden
	
	#opener=urllib.request.build_opener()
	#opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
	#urllib.request.install_opener(opener)
	#urllib.request.urlretrieve(img_url,img_name)
	break



