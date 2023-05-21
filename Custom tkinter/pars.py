import requests
from bs4 import BeautifulSoup as BS

# Ссылки, что парсим
path=requests.get("https://ru.investing.com/equities/russia") # Акции
path_cripto=requests.get("https://ru.investing.com/crypto/currencies") # Крипта
path_exchange=requests.get("https://finance.rambler.ru/currencies/") # Валюта
path_weather=requests.get("https://pogoda.turtella.ru/weathermap") # Погода
print(path.status_code)
print(path_cripto.status_code)
print(path_exchange.status_code)
print(path_weather.status_code)

html_company=BS(path.content,'html.parser')
html_cripto=BS(path_cripto.content,'html.parser')
html_exchange=BS(path_exchange.content,'html.parser')
html_weather=BS(path_weather.content,'html.parser')

# Списки с результатом парсинга
#Акции
company_name=[]
info=[]
company_info=[]
#Крипта
cripto_name=[]
cripto_price=[]
#Крипта
exchange_name=[]
exchange_price=[]
#Погода
weather_city=[]
weather_tmp=[]

# Где ищем
name_parse=html_company.findAll('span', class_='pt-2 font-normal dynamic-table_cell-symbol__wp4Vw') # Имя
price_parse=html_company.findAll('td', class_='datatable_cell__0y0eu datatable_cell--align-end__fwomz dynamic-table_col-other__tKGpI') # цена,объем,дата

name_cripto=html_cripto.findAll('td', class_='left bold elp name cryptoName first js-currency-name') # Имя
price_cripto=html_cripto.findAll('td', class_='price js-currency-price') # цена

name_exchange=html_exchange.findAll('div', class_='finance-currency-table__cell finance-currency-table__cell--currency') # Имя
price_exchange=html_exchange.findAll('div', class_='finance-currency-table__cell finance-currency-table__cell--value') # цена

# <div class="finance-currency-table__cell finance-currency-table__cell--currency">
# Армянских драмов
# </div>

# <div class="finance-currency-table__cell finance-currency-table__cell--value">
# 20.6794
# </div>

city=html_weather.findAll('div', class_='resortListName') # Город
weather=html_weather.findAll('div', class_='resortListTemp') # Погода


# Заполняю списки данными
#Акции
for i in name_parse:
    company_name.append(i.text)

for i in price_parse:
    info.append(i.text)
    stop = len(info)
    start = stop - 5
    if stop%5==0:
        company_info.append(info[start:stop])

#Крипта
cnt_cripto=len(name_cripto)
for i in range(cnt_cripto):
    cripto_name.append(name_cripto[i].text[1:-1])
    cripto_price.append(price_cripto[i].text)

#Валюта
cnt_exchange=len(name_exchange)
for i in range(cnt_exchange):
    exchange_name.append(name_exchange[i].text[1:-1])
    exchange_price.append(price_exchange[i].text[1:-1])


#Прогноз погоды
cnt_city=len(city)
for i in range(cnt_city):
    weather_city.append(city[i].text)
    weather_tmp.append(weather[i].text)

