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
        elif comp["category"] == 'Trading':
            trading["data"].append(comp)
        elif comp["category"] == 'Hospital & Healthcare Services':
            hospital["data"].append(comp)
        elif comp["category"] == 'Power Generation/Distribution':
            power["data"].append(comp)
        elif comp["category"] == 'Transport Infrastructure':
            transport["data"].append(comp)
    IST = pytz.timezone('Asia/Kolkata')
    timenow = datetime.datetime.now(IST).strftime('%d-%m-%Y %H:%M:%S')
    total_data = [timenow,minerals,nonMinerals,finance,tech,nonConsumer,telecom,industry,consumer,health,power,transport,trading,hospital]
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

    # {
    #     ADANIGREEN ATGL ADANITRANS SHREECEM  GAIL  GODREJCP INDIGO NYKAA TORNTPHARM  TATAMOTORS  MARICO  NTPC 
    #     MARUTI DABUR COLPAL HAVELLS BRITANNIA MOTHERSON BPCL  DRREDDY POWERGRID  PIIND  TITAN  SUNPHARMA 
    #     SIEMENS MCDOWELL-N IOC BAJAJ-AUTO PIDILITIND HINDUNILVR ITC  TECHM ADANIPORTS BHARTIARTL HCLTECH BIOCON 
    #     CIPLA UPL SBILIFE TATASTEEL MUTHOOTFIN JSWSTEEL HEROMOTOCO BERGEPAINT TCS DMART COALINDIA 
    #     HDFCLIFE ULTRACEMCO WIPRO NESTLEIND ONGC 155.80 156.70 154.20 -0.50 -0.32 Grasim Industries Ltd. GRASIM 1,595.90 1,606.75 1,583.15 -5.35 -0.33 SRF Ltd. SRF 2,292.55 2,300.00 2,273.05 -8.00 -0.35 Zomato Ltd. ZOMATO 53.85 54.50 53.30 -0.20 -0.37 Bosch Ltd. BOSCHLTD 18,389.30 18,481.70 18,052.20 -81.55 -0.44 Bajaj Finance Ltd. BAJFINANCE 5,874.15 5,887.40 5,781.00 -27.15 -0.46 Hindustan Aeronautics Ltd. HAL 2,849.30 2,913.40 2,814.45 -13.40 -0.47 Tata Power Company Ltd. TATAPOWER 208.75 209.20 206.00 -1.00 -0.48 Indian Railway Catering And Tourism Corporation Ltd. IRCTC 611.95 613.50 604.55 -3.10 -0.50 Procter & Gamble Hygiene and Health Care Ltd. PGHH 13,757.60 13,880.00 13,705.00 -69.80 -0.50 Life Insurance Corporation of India LICI 595.50 596.95 590.05 -3.05 -0.51 Bharat Electronics Ltd. BEL 94.90 95.50 93.55 -0.55 -0.58 Infosys Ltd. INFY 1,471.55 1,474.30 1,457.65 -8.85 -0.60 Tata Consumer Products Ltd. TATACONSUM 704.40 710.20 701.35 -4.85 -0.68 ACC Ltd. ACC 1,846.90 1,858.65 1,819.80 -13.20 -0.71 Hindalco Industries Ltd. HINDALCO 405.65 409.50 395.40 -3.20 -0.78 Divi's Laboratories Ltd. DIVISLAB 2,787.50 2,832.80 2,779.00 -22.70 -0.81 Asian Paints Ltd. ASIANPAINT 2,830.20 2,844.00 2,807.00 -23.35 -0.82 ICICI Lombard General Insurance Company Ltd. ICICIGI 1,075.15 1,085.00 1,072.10 -8.90 -0.82 Bandhan Bank Ltd. BANDHANBNK 224.85 225.70 220.30 -2.00 -0.88 ICICI Prudential Life Insurance Company Ltd. ICICIPRULI 394.00 396.20 390.15 -3.60 -0.91 Indus Towers Ltd. INDUSTOWER 155.30 157.15 154.30 -1.45 -0.93 Eicher Motors Ltd. EICHERMOT 3,116.10 3,147.20 3,095.15 -30.60 -0.97 Kotak Mahindra Bank Ltd. KOTAKBANK 1,699.30 1,713.50 1,692.00 -17.40 -1.01 HDFC Asset Management Company Ltd. HDFCAMC 1,757.35 1,778.85 1,750.50 -25.90 -1.45 Reliance Industries Ltd. RELIANCE 2,322.70 2,344.00 2,315.05 -36.55 -1.55 ICICI Bank Ltd. ICICIBANK 842.65 845.35 836.25 -13.30 -1.55 Info Edge (India) Ltd. NAUKRI 3,456.90 3,478.75 3,429.05 -54.80 -1.56 Larsen & Toubro Ltd. LT 2,157.85 2,182.00 2,133.00 -35.35 -1.61 Ambuja Cements Ltd. AMBUJACEM 378.35 382.35 373.40 -6.35 -1.65 Mahindra & Mahindra Ltd. M&M 1,226.70 1,256.70 1,225.35 -21.45 -1.72 SBI Cards And Payment Services Ltd. SBICARD 753.75 761.00 747.00 -13.35 -1.74 Bajaj Finserv Ltd. BAJAJFINSV 1,328.85 1,342.00 1,321.05 -23.70 -1.75 Cholamandalam Investment and Finance Company Ltd. CHOLAFIN 752.75 762.00 749.55 -13.90 -1.81 Axis Bank Ltd. AXISBANK 851.90 861.60 845.50 -15.90 -1.83 DLF Ltd. DLF 350.05 356.35 347.70 -7.05 -1.97 Vedanta Ltd. VEDL 279.85 284.95 272.55 -5.65 -1.98 LTIMindtree Ltd. LTIM 4,640.10 4,680.00 4,600.10 -97.90 -2.07 State Bank Of India SBIN 547.35 554.95 545.00 -11.55 -2.07 IndusInd Bank Ltd. INDUSINDBK 1,144.80 1,162.25 1,138.00 -25.00 -2.14 One97 Communications Ltd. PAYTM 593.05 605.40 589.10 -13.00 -2.15 Housing Development Finance Corporation Ltd. HDFC 2,608.90 2,649.95 2,588.10 -58.20 -2.18 Bank Of Baroda BANKBARODA 167.80 170.70 166.05 -3.75 -2.19 Apollo Hospitals Enterprise Ltd. APOLLOHOSP 4,317.25 4,399.70 4,291.65 -100.90 -2.28 HDFC Bank Ltd. HDFCBANK 1,588.65 1,613.75 1,585.00 -42.05 -2.58 Adani Enterprises Ltd. ADANIENT 1,896.20 1,940.00 1,820.60 -56.95 -2.92 Bajaj Holdings & Investment Ltd. BAJAJHLDNG MPHASIS  GLAND
    # }
