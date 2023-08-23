#incript korlam na vatija 😊 ja free tei nia ja.. Vobissote tools making course dile amr theke sikhe nis ❤️‍🩹
import requests,os,json
os.system("clear")
os.system("xdg-open https://www.facebook.com/profile.php?id=100077855090738/")
import requests,re

logo3=("""
\033[1;32m .d8888b.   .d8888b.       88888888888 888     888 
\033[1;32m88P  Y88b d88P  Y88b           888     888     888 
\033[1;32m888    888 888    888          888     888     888 
\033[1;32m888        888                 888     Y88b   d88P 
\033[1;32m888        888                 888      Y88b d88P  
\033[1;32m888    888 888    888 888888   888       Y88o88P   
\033[1;32m88b  d88P Y88b  d88P           888        Y888P    
\033[1;32m "Y8888P"   "Y8888P"           888         Y8P     
																	
""")
headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36', 'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1'}
url = 'http://www.insecam.org/en/jsoncountries/'

response = requests.get(url,headers = headers)
data = response.json()
countries = data ['countries']
print(logo3)
print(47*'\033[1;32m═\033[1;32m')
for key,value in countries.items():
	
	print(f'code : ({key}) - {value["country"]} / {value["count"]})	 ')
	
	
	
	
print(47*'\033[1;32m═\033[1;32m')
country_code = input("\033[1;93mENTER Country_Code : \033[1;91m")
print(47*'\033[1;32m═\033[1;32m')
url = f"http://www.insecam.org/en/bycountry/{country_code}/"
res = requests.get(url, headers = headers)
last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
for page in last_page:
	res2 = requests.get(f'http://www.insecam.org/en/byrating/?page={page}',headers = headers)
find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
for ip in find_ip:
 print(ip)
