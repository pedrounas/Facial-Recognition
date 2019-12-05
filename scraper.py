from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request 
import os
import requests

def get_students_names():
	user_name = "up201606726"
	password = "Chitaveloz98"
	names=[]
	driver = webdriver.Firefox()
	driver.get("https://sigarra.up.pt/fcup/pt/WEB_PAGE.INICIAL")
	element = driver.find_element_by_id("user")
	element.send_keys(user_name)
	element = driver.find_element_by_id("pass")
	element.send_keys(password)
	element.send_keys(Keys.RETURN)
	time.sleep(1) #para só avançar quando tiver feito mesmo o login 
	
	#58 alunos (2-60)
	for i in range (2,60):
		if(i>=52): #mais de uma pagina de alunos
			driver.get("https://sigarra.up.pt/fcup/pt/fest_geral.estudantes_inscritos_list?pv_num_pag=2&pv_ocorrencia_id=445367")
			element=driver.find_element_by_xpath("//*[@id='conteudoinner']/table/tbody/tr["+str(i-50)+"]/td[1]/a")
		else:
			driver.get("https://sigarra.up.pt/fcup/pt/fest_geral.estudantes_inscritos_list?pv_ocorrencia_id=445367")
			element=driver.find_element_by_xpath("//*[@id='conteudoinner']/table/tbody/tr["+str(i)+"]/td[1]/a")
		element.click()
		time.sleep(3)
		name=driver.find_element_by_xpath("//*[@id='conteudoinner']/h1[2]")

		if(name is None):
			name=driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[3]/div/div[2]/div/div[2]/div[1]")
			if(name is None):
				#Feup
				name=driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[3]/div/h1[2]")
		print(name.text)
		names.append(name.text)
		#img_url = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[3]/div/div[2]/div/div[1]/div/img").get_attribute("src")
		#o link da imagem esta certo
		#print(img_url)
		#img_name = str(i)+"jpg"
		##Método1 - dá forbidden

		#urlretrieve(image, "student"+str(i)+".jpg")
		#Metodo4 - Wget 
	
		#wget --save-cookies cookies.txt --keep-session-cookies --auth-no-challenge --user=up201606726 --password=Chitaveloz98 https://sigarra.up.pt/fcup/pt/WEB_PAGE.INICIAL
		#wget --load-cookies cookies.txt https://sigarra.up.pt/fcup/pt/fotografias_service.foto?pct_cod=201200765
	return names


