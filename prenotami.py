import datetime
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

# Bot Ejecutado Creado por guido halley 

def horario (hora, minuto, segundos, data_actual):
    if data_actual.hour == hora and data_actual.minute == minuto and data_actual.second== segundos:
        return True
    return False


def procesamiento_dias_de_semana(dias_de_semana):
    dias_de_semana_int = []
    
    for dia in dias_de_semana:
        if dia== "lun":
            dias_de_semana_int.append(0)
        if dia== "mar":
            dias_de_semana_int.append(1)
        if dia== "mier":
            dias_de_semana_int.append(2)
        if dia== "jue":
            dias_de_semana_int.append(3)
        if dia== "vier":
            dias_de_semana_int.append(4)
        if dia== "sab":
            dias_de_semana_int.append(5)
        if dia== "dom":
            dias_de_semana_int.append(6)
            
    return dias_de_semana_int

print("████████████████████████▀███████████████████████████")
print("█▄─▄─▀█─▄▄─█▄─▀█▄─▄█─▄▄▄▄█▄─▄█─▄▄─█▄─▄─▀█─▄▄─█─▄─▄─█")
print("██─▄─▀█─██─██─█▄▀─██─██▄─██─██─██─██─▄─▀█─██─███─███")
print("▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀")

def esta_enelDia(dias_de_semana,data_actual):
    if data_actual.weekday() in dias_de_semana:
        return True
    
    return False


hora_string = input("hh:mm:ss")
dia_semana_string = input("dia: lun mar mier jue vier sab dom")


email = input("email: ")
password = input("password: ")

path = "\prenotami\path"

hora = int(hora_string.split(':')[0])
minuto = int(hora_string.split(':')[1])
segundos = int(hora_string.split(':')[2])

dias_de_semana = dia_semana_string.split(' ')
dias_de_semana_int = procesamiento_dias_de_semana(dias_de_semana)

activo = True
chrome_options = webdriver.ChromeOptions()
pref = {"profile.magaed_default_content_settings.images" : 2}
chrome_options.add_experimental_option("prefs".prefs)

while activo:
    ahora = datetime.datetime.now()
    print (ahora)
    if  horario (hora, minuto, segundos, ahora) and  procesamiento_dias_de_semana ():
        activo = False
        navegador = webdriver.Chrome(chrome_options=chrome_options)
        navegador.get("https://prenotami.esteri.it")
        time.sleep(2)
        navegador.find_element(
             By.ID, "login-email").send_keys(email)
        navegador.find_element(
            By.ID, "login-password").send_keys(password)
        navegador.find_element(
            By.XPATH, '//*[@id="login-form"]/button').click()
        time.sleep(3)
        navegador.find_element(By.ID, "advanced").click()
        time.sleep(2)
        navegador.find_element(
            By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button').click()
        time.sleep(2)
        i = 1
        
        while navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button') == navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button'):
            print("Tentativa Nº - " + str(i))
            navegador.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button').click()
            delay = 10  # segundos
            try:
                elemento = WebDriverWait(navegador, delay).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button')))
                elemento.click()
            except TimeoutException:
                print("No se encontro el elemento")
            i = i + 1
            
            time.sleep(1)
            
            navegador.find_element(By.ID, 'File_0').send_keys(path)
            navegador.find_element(By.ID, 'PrivacyCheck').click()
            navegador.find_element(By.ID, 'btnAvanti').click()
            alert = Alert(navegador)
            alert.accept()
            ativo = True
        while ativo:
            if navegador.find_element(By.CLASS_NAME, 'day availableDay').is_enabled:
                navegador.find_element(By.CLASS_NAME, 'day availableDay').click()
                activo = False
                navegador.find_element(
                    By.CLASS_NAME, 'table-condensed > dtpicker-next').click()
                navegador.find_element(By.ID, 'btnPrenota').click()
            
