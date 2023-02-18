#Logo Text-to-ASCII-Art-GEnerator(TAGG)
print(r"""

   /$ /$   /$$      /$$ /$$$$$$$$ /$$$$$$$        /$$   /$$ /$$$$$$ /$$     /$$ /$$$$$$  /$$   /$$
  |_/|_/  | $$$    /$$$| $$_____/| $$__  $$      | $$  /$$/|_  $$_/|  $$   /$$//$$__  $$| $$  /$$/
  /$$$$$$ | $$$$  /$$$$| $$      | $$  \ $$      | $$ /$$/   | $$   \  $$ /$$/| $$  \ $$| $$ /$$/ 
 /$$__  $$| $$ $$/$$ $$| $$$$$   | $$$$$$$/      | $$$$$/    | $$    \  $$$$/ | $$$$$$$$| $$$$$/  
| $$  \ $$| $$  $$$| $$| $$__/   | $$__  $$      | $$  $$    | $$     \  $$/  | $$__  $$| $$  $$  
| $$  | $$| $$\  $ | $$| $$      | $$  \ $$      | $$\  $$   | $$      | $$   | $$  | $$| $$\  $$ 
|  $$$$$$/| $$ \/  | $$| $$$$$$$$| $$  | $$      | $$ \  $$ /$$$$$$    | $$   | $$  | $$| $$ \  $$
 \______/ |__/     |__/|________/|__/  |__/      |__/  \__/|______/    |__/   |__/  |__/|__/  \__/
                                                                                                  
                                                                                                  
                                                                                                  

 """)
print("\n***************************************************************** *")
print("\n* Copyright of Ömer KIYAK, 2022                                 * *")
print("\n* https://www.instagram.com/omer_x_kiyak/                       * *")
print("\n*  https://github.com/omer-X-kiyak/                             * *")
print("\n***************************************************************** *\n \n")
# Kullanıcı bilgileri-1

kadi = input ("Lütfen T.C numaranızı girin: \t")
sifre = input("Lütfen şifrenizi giriniz: \t")
#Kütüphaneler
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Driver yolu giris
browser = webdriver.Edge('msedgedriver.exe')
#Site giris
browser.get("https://giris.turkiye.gov.tr/Giris/gir")
time.sleep(2)

#Kullanıcı bilgileri button
username = browser.find_element(By.ID, 'tridField')
password = browser.find_element(By.ID, 'egpField')
#Kulanıcı bilgileri çekme :)
username.send_keys(kadi)
password.send_keys(sifre)
tikla = browser.find_element(By.CLASS_NAME, 'submitButton')
tikla.click()
time.sleep(2)

###                   ARAMA    sgk

any("self")
sgk = browser.get("https://www.turkiye.gov.tr/4a-hizmet-dokumu") 
time.sleep(3)
try:

    sgk0 =browser.find_element(By.CLASS_NAME, 'compact').text
    time.sleep(10)
except:
    print("Bulamadık :(")

###                   ARAMA    davalarim
davalarim = browser.get("https://www.turkiye.gov.tr/davalarim")
time.sleep(3)
try:

    davalarim0 = browser.find_element(By.CLASS_NAME, 'resultContainer').text
    time.sleep(10)
except:
    print("Bulamadık :(")

###                   ARAMA    yargitay dava
browser.get("https://www.turkiye.gov.tr/yargitay-dava-sureci-sorgulama")
time.sleep(10)


###                   ARAMA    sgk
sgko = browser.get("https://www.turkiye.gov.tr/sgk-tescil-ve-hizmet-dokumu")
time.sleep(3)
try:
    sgko0 =browser.find_element(By.ID, 'table_001').text
    time.sleep(10)
except:
    print("Bulamadık :(")

###                   ARAMA    BTK
BTK = browser.get("https://www.turkiye.gov.tr/mobil-hat-sorgulama")
time.sleep(3)
try:
    BTK0 = browser.find_element(By.CLASS_NAME, 'ed-partial-wrapper').text
except:
    print("Bulamadık :(")

time.sleep(10)

###                   ARAMA    TVKGS
tvkgs = browser.get("https://www.turkiye.gov.tr/tapu-bilgileri-sorgulama")
time.sleep(3)
try:
    tvkgs0 = browser.find_element(By.CLASS_NAME, 'resultContainer').text
except:
    print("Bulamadık :(")

time.sleep(10)

###                   ARAMA    gib
gib = browser.get("    https://ivd.gib.gov.tr/index_edevlet.jsp?gn=")
time.sleep(20)
try:

    gib0 = browser.find_element(By.CLASS_NAME, 'csc-ver-container').text
except:
    print("Bulamadık :(")
time.sleep(10)
print(sgk0,'\n', davalarim0,'\n', sgko0,'\n', BTK0,'\n', tvkgs0,'\n', gib0 )

with open('sonuç.txt', 'a') as f:
    f.write(sgk0 + '\n')
    f.write(davalarim0 + '\n')
    f.write(sgko0 + '\n')
    f.write(BTK0 + '\n')
    f.write(tvkgs0 + '\n')
    f.write(gib0 + '\n') # Her sonuç bilgisinin yeni bir satıra yazılmasını sağlar

    
browser.close()

