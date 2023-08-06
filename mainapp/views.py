from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
import datetime
import pytz
def home(request):
    return render(request,'base.html')

def heatmap(request):
    minerals = {'name':'Energy Minerals',"data":[],"class":"minerals"}
    nonMinerals = {'name':'Non-Energy Minerals',"data":[],"class":"nonMinerals"}
    finance = {'name':'Finance',"data":[],"class":"finance"}
    tech = {'name':'Technology Services',"data":[],"class":"tech"}
    nonConsumer = {'name':'Consumer Non-Durables',"data":[],"class":"nonConsumer"}
    telecom = {'name':'Telecom',"data":[],"class":"telecom"}
    industry = {'name':'Industries',"data":[],"class":"industry"}
    consumer = {'name':'Consumer Durables',"data":[],"class":"consumer"}
    health = {'name':'Pharma',"data":[],"class":"health"}
    trading = {'name':'Trading',"data":[],"class":"trading"}
    hospital = {'name':'Hospital',"data":[],"class":"hospital"}
    power = {'name':'Utilities',"data":[],"class":"power"}
    transport = {'name':'Transport',"data":[],"class":"transport"}
    insurance = {'name':'Insurance',"data":[],"class":"insurance"}
    nifty_data = []
    nifty_total = 0
    response = requests.get(
        "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9")
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')
    trs = table[1].find_all('tr')[1:]
    for tr in trs:
        data_inside = tr.find_all('td')
        name = data_inside[0].find('a').find('b').string
        category = data_inside[1].find('a').find('b').string
        ltp = data_inside[2].string
        priceChange = data_inside[3].string
        percentChange = float(data_inside[4].string)
        mcap = float(data_inside[5].string.replace(',', ''))
        company = {'name': name, 'category': category, 'ltp': ltp,
                   'priceChange': priceChange, 'percentChange': percentChange, 'mcap': mcap}
        if percentChange<=-2.5:
            company["class"] = "negative-high"
        elif percentChange<=-1.5:
            company["class"] = "negative-mid"
        elif percentChange<=-0.5:
            company["class"] = "negative-small"
        elif percentChange>=-0.5 and percentChange<=0.5:
            company["class"] = "neutral"
        elif percentChange>=2.5:
            company["class"] = "positive-high"
        elif percentChange>=1.5:
            company["class"] = "positive-mid"
        elif percentChange>=0.5:
            company["class"] = "positive-small"
        nifty_data.append(company)
        nifty_total = nifty_total + mcap
    for comp in nifty_data:
        if comp["category"] == 'Paints' or comp["category"] == 'Engineering & Construction' or comp["category"] == 'Pesticides & Agrochemicals':
            industry["data"].append(comp)
        elif comp["category"] == 'Oil Exploration and Production' or comp["category"] == 'Coal' or comp["category"] == 'Refineries':
            minerals["data"].append(comp)
        elif comp["category"] == 'Iron & Steel' or comp["category"] == 'Cement' or (comp["name"] == 'Grasim'):
            nonMinerals["data"].append(comp)
        elif comp["category"] == 'Finance - Housing' or comp["category"] == 'Bank - Private' or comp["category"] == 'Bank - Public' or comp["category"] == 'Finance - NBFC' or comp["category"] == 'Finance - Investment':
            finance["data"].append(comp)
        elif comp["category"] == 'IT Services & Consulting':
            tech["data"].append(comp)
        elif comp["category"] == 'Household & Personal Products' or comp["category"] == 'Diversified' or comp["category"] == 'Consumer Food' or comp["category"] == 'Tea/Coffee':
            nonConsumer["data"].append(comp)
        elif comp["category"] == 'Telecommunication - Service Provider':
            telecom["data"].append(comp)
        elif comp["category"] == 'Automobile - Passenger Cars' or ('Diamond' in comp["category"]) or comp["category"] == 'Automobile - LCVS/ HVCS' or comp["category"] == 'Automobile - Auto & Truck Manufacturers' or comp["category"] == 'Automobile - 2 & 3 Wheelers':
            consumer["data"].append(comp)
        elif comp["category"] == 'Pharmaceuticals & Drugs':
            health["data"].append(comp)
        elif comp["category"] == 'Trading':
            trading["data"].append(comp)
        elif comp["category"] == 'Hospital & Healthcare Services':
            hospital["data"].append(comp)
        elif comp["category"] == 'Power Generation/Distribution':
            power["data"].append(comp)
        elif comp["category"] == 'Transport Infrastructure':
            transport["data"].append(comp)
        elif comp["category"] == 'Life & Health Insurance':
            insurance["data"].append(comp)
    IST = pytz.timezone('Asia/Kolkata')
    timenow = datetime.datetime.now(IST).strftime('%d-%m-%Y %H:%M:%S')
    total_data = [timenow,minerals,nonMinerals,finance,tech,nonConsumer,telecom,industry,consumer,health,power,transport,trading,hospital,insurance]
    context = {'total_data':total_data,'timenow':timenow}
    return render(request, 'heatmap.html', context)


def sensexHeatmap(request):
    minerals = {'name':'Energy Minerals',"data":[],"class":"minerals"}
    nonMinerals = {'name':'Non-Energy Minerals',"data":[],"class":"nonMinerals"}
    finance = {'name':'Finance',"data":[],"class":"finance"}
    tech = {'name':'Technology Services',"data":[],"class":"tech"}
    nonConsumer = {'name':'Consumer Non-Durables',"data":[],"class":"nonConsumer"}
    telecom = {'name':'Telecom',"data":[],"class":"telecom"}
    industry = {'name':'Industries',"data":[],"class":"industry"}
    consumer = {'name':'Consumer Durables',"data":[],"class":"consumer"}
    health = {'name':'Pharma',"data":[],"class":"health"}
    power = {'name':'Utilities',"data":[],"class":"power"}
    sensex_data=[]
    sensex_total = 0
    response = requests.get(
        "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=BSE&opttopic=indexcomp&index=4")
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')
    trs = table[1].find_all('tr')[1:]
    for tr in trs:
        data_inside = tr.find_all('td')
        name = data_inside[0].find('a').find('b').string
        category = data_inside[1].find('a').find('b').string
        ltp = data_inside[2].string
        priceChange = data_inside[3].string
        percentChange = float(data_inside[4].string)
        mcap = float(data_inside[5].string.replace(',', ''))
        company = {'name': name, 'category': category, 'ltp': ltp,
                   'priceChange': priceChange, 'percentChange': percentChange, 'mcap': mcap}
        if percentChange<=-2.5:
            company["class"] = "negative-high"
        elif percentChange<=-1.5:
            company["class"] = "negative-mid"
        elif percentChange<=-0.5:
            company["class"] = "negative-small"
        elif percentChange>=-0.5 and percentChange<=0.5:
            company["class"] = "neutral"
        elif percentChange>=2.5:
            company["class"] = "positive-high"
        elif percentChange>=1.5:
            company["class"] = "positive-mid"
        elif percentChange>=0.5:
            company["class"] = "positive-small"
        sensex_data.append(company)
        sensex_total = sensex_total + mcap
    for comp in sensex_data:
        if comp["category"] == 'Paints' or comp["category"] == 'Engineering & Construction' or comp["category"] == 'Pesticides & Agrochemicals':
            industry["data"].append(comp)
        elif comp["category"] == 'Oil Exploration and Production' or comp["category"] == 'Coal' or comp["category"] == 'Refineries':
            minerals["data"].append(comp)
        elif comp["category"] == 'Iron & Steel' or comp["category"] == 'Cement' or (comp["name"] == 'Grasim'):
            nonMinerals["data"].append(comp)
        elif comp["category"] == 'Finance - Housing' or comp["category"] == 'Bank - Private' or comp["category"] == 'Bank - Public' or comp["category"] == 'Finance - NBFC' or comp["category"] == 'Finance - Investment' or comp["category"] == 'Life & Health Insurance':
            finance["data"].append(comp)
        elif comp["category"] == 'IT Services & Consulting':
            tech["data"].append(comp)
        elif comp["category"] == 'Household & Personal Products' or comp["category"] == 'Diversified' or comp["category"] == 'Consumer Food' or comp["category"] == 'Tea/Coffee':
            nonConsumer["data"].append(comp)
        elif comp["category"] == 'Telecommunication - Service Provider':
            telecom["data"].append(comp)
        elif comp["category"] == 'Automobile - Passenger Cars' or ('Diamond' in comp["category"]) or comp["category"] == 'Automobile - LCVS/ HVCS' or comp["category"] == 'Automobile - Auto & Truck Manufacturers' or comp["category"] == 'Automobile - 2 & 3 Wheelers':
            consumer["data"].append(comp)
        elif comp["category"] == 'Pharmaceuticals & Drugs':
            health["data"].append(comp)
        elif comp["category"] == 'Power Generation/Distribution':
            power["data"].append(comp)
    IST = pytz.timezone('Asia/Kolkata')
    timenow = datetime.datetime.now(IST).strftime('%d-%m-%Y %H:%M:%S')
    total_data = [minerals,nonMinerals,finance,tech,nonConsumer,telecom,industry,consumer,health,power]
    context = {'total_data':total_data,'timenow':timenow}
    return render(request, 'sensexHeatmap.html', context)
