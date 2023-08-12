from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time, json

driver = webdriver.Chrome()

with open("./datos-de-pruebas/pruebas.json") as json_file:
        data = json.load(json_file)

        driver.get("file:///c:/Users/ehdel/Documents/Asesoria%20legal%20web/index.html")
        time.sleep(3)
        
        nextPageLink = driver.find_element(By.ID, "navCitas")
        nextPageLink.click()
        time.sleep(3)
        for p in data["datos"]:
                
                name = driver.find_element(By.ID, "inputName")
                name.send_keys(p["name"])
                
                subject = driver.find_element(By.ID, "inputAsunto")
                subject.send_keys(p["asunto"])
                
                email = driver.find_element(By.ID, "inputEmail")
                email.send_keys(p["email"])
                
                address = driver.find_element(By.ID, "inputAddress")
                address.send_keys(p["address"])
                
                state = driver.find_element(By.ID, "inputState")
                state.click()
                state.send_keys("Asesoria Empresarial")
                
                textArea  = driver.find_element(By.ID, "inputTextarea")
                textArea.send_keys(p["cita"])
                
                btnSubmit  = driver.find_element(By.ID, "enviar")
                submit_button = driver.find_element("xpath", '//button[@id="enviar"]')

                actions = ActionChains(driver)
                actions.move_to_element(submit_button).perform()

                # Espera unos segundos para que el botón sea visible después de desplazarte
                btnSubmit.click()

time.sleep(12)
with open("./datos-de-pruebas/pruebas.json") as json_file:
        data = json.load(json_file)
        
        nextPageLink = driver.find_element(By.ID, "navSugerencias")
        nextPageLink.click()
        time.sleep(3)
        for p in data["datos"]:
                
                name = driver.find_element(By.ID, "inputName")
                name.send_keys(p["name"])
                
                subject = driver.find_element(By.ID, "inputAsunto")
                subject.send_keys(p["asunto"])
                
                email = driver.find_element(By.ID, "inputEmail")
                email.send_keys(p["email"])
                
                address = driver.find_element(By.ID, "inputAddress")
                address.send_keys(p["address"])
                
                state = driver.find_element(By.ID, "inputState")
                state.click()
                state.send_keys("Asesoria Empresarial")
                
                textArea  = driver.find_element(By.ID, "inputTextarea")
                textArea.send_keys(p["cita"])
                
                btnSubmit  = driver.find_element(By.ID, "enviar")
                submit_button = driver.find_element("xpath", '//button[@id="enviar"]')

                actions = ActionChains(driver)
                actions.move_to_element(submit_button).perform()

                # Espera unos segundos para que el botón sea visible después de desplazarte
                btnSubmit.click()


time.sleep(12)        
driver.close()