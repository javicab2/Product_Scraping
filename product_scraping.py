from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://siccba.com.ar/categoria-producto/alarmas-y-accesorios/barreras-infrarrojas/"
page= requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")

#productos
prod= soup.find_all("h2",class_="woocommerce-loop-product__title")
productos = list()

#precios
pre=soup.find_all("span",class_="woocommerce-Price-amount amount")
precios=list()

for i in prod:
    productos.append(i.text)
for i in pre:
    precios.append(i.text)

df=pd.DataFrame({"Productos":productos,"Precio":precios})

df.to_csv("products.csv", index = False)
print(df)