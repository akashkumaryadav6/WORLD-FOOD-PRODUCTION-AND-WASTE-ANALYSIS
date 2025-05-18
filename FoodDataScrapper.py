from dash import *
import requests
from bs4 import BeautifulSoup
from Footer import footer
import time 
import dash_bootstrap_components as dbc
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get(url):
    try:
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session.get(url)
    except Exception as e:
        print("Scrapping Error", e)
        return None

url = "https://www.bbc.co.uk/search?q=food+waste&page={}"

no_of_pages=5
data = []
for pgno in range(1,no_of_pages+2):
    page = get(url.format(pgno))
    if not page:continue
    soup = BeautifulSoup(page.text,"html.parser")
    for div in soup.find_all('div',attrs={'class':"ssrcss-11rb3jo-Promo ett16tt0"}):
        news = {}
        news['image'] = src.attrs.get('src') if (src:=div.find('img')) else ""
        news['head'], news['subhead'] = [i.text for i in div.find_all('p')]
        news['link'] = div.find('a').attrs.get('href')
        data.append(news)
    time.sleep(1)


scrap = []

for i in data:
    div= dbc.Card([
         html.Div([
        html.A([html.H1(i['head']),], href=i['link'], style={'color': 'black'}),        
        html.H3(i['subhead']),
        dbc.CardImg(src=i['image'], top=True)
    ], className='row')
    ], className='text-center mx-auto', style={'margin': '3rem', 'width': '40rem'})       
    scrap.append(div)


scrapper = html.Div(scrap), footer