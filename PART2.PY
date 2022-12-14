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



# Driver yolu giris
browser = webdriver.Edge('msedgedriver.exe')
#Site giris
browser.get("https://giris.turkiye.gov.tr/Giris/gir")
time.sleep(2)

#Kullanıcı bilgileri button
username = browser.find_element_by_xpath("/html/body/div[1]/main/section[2]/form/fieldset/div[1]/div/input")
password = browser.find_element_by_xpath("/html/body/div[1]/main/section[2]/form/fieldset/div[2]/div/input[1]")
#Kulanıcı bilgileri çekme :)
username.send_keys(kadi)
password.send_keys(sifre)
tikla = browser.find_element_by_xpath("/html/body/div[1]/main/section[2]/form/div[2]/input[4]") 
tikla.click()
time.sleep(2)

###                   ARAMA    sgk

any("self")
browser.get("https://www.turkiye.gov.tr/4a-hizmet-dokumu") 
can = browser.find_element_by_xpath("/html/body/main/div/section/section[2]/div[1]/dl/dd[9]/strong").text
print(can)




time.sleep(10)


###                   ARAMA    davalarim
browser.get("https://www.turkiye.gov.tr/davalarim")
time.sleep(10)
###                   ARAMA    yargitay dava
browser.get("https://www.turkiye.gov.tr/yargitay-dava-sureci-sorgulama")
time.sleep(10)

###                   ARAMA    sgk
browser.get("https://www.turkiye.gov.tr/sgk-tescil-ve-hizmet-dokumu")
time.sleep(10)

###                   ARAMA    BTK
browser.get("https://www.turkiye.gov.tr/mobil-hat-sorgulama")
time.sleep(10)

###                   ARAMA    TVKGS
browser.get("https://www.turkiye.gov.tr/tapu-bilgileri-sorgulama")
time.sleep(10)

###                   ARAMA    gib
browser.get("    https://ivd.gib.gov.tr/index_edevlet.jsp?gn=")
browser.find_element_by_xpath("/html/body/main/div/section/section[2]/div[3]/a")
time.sleep(30)

browser.close()
