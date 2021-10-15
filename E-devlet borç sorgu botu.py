from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
sleep(2)
driver.get("https://giris.turkiye.gov.tr/Giris/gir")

sleep(1)
##kullanıcı giris işlemleri
driver.find_element_by_xpath("/html/body/div[1]/main/section[2]/form/fieldset/div[1]/div/input").send_keys("")

driver.find_element_by_xpath("/html/body/div[1]/main/section[2]/form/fieldset/div[2]/div/input[1]").send_keys("")

driver.find_element_by_name("submitButton").click()

sleep(2)

###                   ARAMA    sgk

any("self")
driver.get("https://www.turkiye.gov.tr/4a-hizmet-dokumu") 
sleep(5)

###                   ARAMA    hava

any("self")
driver.get("https://www.turkiye.gov.tr/5-gunluk-hava-tahmini") 
sleep(5)

###                   ARAMA    plaka cezaları

any("self")
driver.get("https://www.turkiye.gov.tr/emniyet-arac-plakasina-yazilan-ceza-sorgulama") 
sleep(5)

###                   ARAMA    vergi borcu

any("self")
driver.get("https://www.turkiye.gov.tr/gib-vergi-borcu-sorgu") 
sleep(5)


###                   ARAMA    Gelir İdaresi Baskanlıgı

any("self")
driver.get("https://www.turkiye.gov.tr/gib-ivd?redirect=Url")
sleep(1)
sleep(5)

###                   ARAMA    Dava Dosyası Sorgulama adalet

any("self")
driver.get("https://www.turkiye.gov.tr/davalarim") 
sleep(8)

###                   ARAMA    Dava Dosya Sorgulama yargıtay

any("self")
driver.get("https://www.turkiye.gov.tr/yargitay-dava-sureci-sorgulama") 
sleep(8)

###                   ARAMA    İcra Dosyası Sorgulama

any("self")
driver.get("https://www.turkiye.gov.tr/adalet-icra-dosyasi-sorgulama") 
sleep(8)

###                   ARAMA    Mobil/Sabit/İnternet/Kablo Tv/Uydu İşletmecilerinden Borç/Alacak Sorgulama ve Ödeme/iade İşlemleri

any("self")
driver.get("https://www.turkiye.gov.tr/btk-mobil-sabit-internet-kablo-tv-uydu-isletmecilerinden-borc-ve-alacak-sorgulama") 
sleep(10)


###                   ARAMA    Uyap/Hukuk Dava Açılış/TAMAMLANMAYAN DOSYALAR 

any("self")
driver.get("https://www.turkiye.gov.tr/uyap-portali-vatandas-girisi?redirect=Url") 
sleep(10)
driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/div[2]/ul/li[3]/a/span[1]").click() 
driver.get("https://vatandas.uyap.gov.tr/main/jsp/vatandas/index.jsp?menuId=14597")
sleep(20)

###                   ARAMA    Uyap/İdari Dava Açılış/ÖDEME BEKLEYEN DOSYALAR

any("self")
driver.get("https://www.turkiye.gov.tr/uyap-portali-vatandas-girisi?redirect=Url") 
sleep(10)
driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/div[2]/ul/li[3]/a/span[1]").click() 
driver.get("https://vatandas.uyap.gov.tr/main/jsp/vatandas/index.jsp?menuId=17665")
sleep(20)

driver.get("https://vatandas.uyap.gov.tr/main/jsp/vatandas/index.jsp?menuId=12577")
sleep(20)


driver.close()