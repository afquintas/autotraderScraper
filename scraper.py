from bs4 import BeautifulSoup as soup
from openpyxl import Workbook, load_workbook
from urllib.request import urlopen, Request
import time
import random

# this funcion extracting a single page data as all info need from a car
def extract_page(soup):
    price = soup.find(
        'div', class_='text-gray-base text-bold text-size-600 margin-right-auto').text
    Name = soup.find(
        'h1', class_='text-bold text-size-600 text-size-sm-700 margin-right-2').text
    seller = soup.find(
        'div', class_='colored-background bg-blue-lightest').div.div.div.div.text.replace('Call DealerChat with Dealer', '')
    N = Name.split()
    new_or_used = N[0]
    year = N[1]
    make = N[2]
    model = str(N[3:])
    car_info = [i.div.find(class_='col-xs-8').text for i in soup.find_all(
        'li', class_='list-bordered list-condensed')]
    milage = car_info[0].replace(',', '')
    drive_type = car_info[1]
    engine = car_info[2]
    transmission = car_info[3]
    fuel_type = car_info[4]
    mpg = car_info[5]
    interior = car_info[6]
    exterior = car_info[7]
    stock_number = car_info[8]
    vin = car_info[9]
    all_data = [new_or_used, year, make, model, price, milage, drive_type,
                engine, transmission, fuel_type, mpg, interior, exterior, vin, seller]

    print(all_data)
    save_data(all_data)


def save_data(data):
    # This funcion dynamically adding to excel file
    wb = load_workbook('ProductData.xlsx')
    ws = wb.active
    ws.append(data)
    wb.save('ProductData.xlsx')


def main():
    user_agents = [
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)']

    url = 'https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=527163493&zip=91402&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D91402%26startYear%3D2015%26numRecords%3D100%26sortBy%3DderivedpriceASC%26incremental%3Dall%26firstRecord%3D0%26seriesCodeList%3DG_CLASS%26marketExtension%3Don%26makeCodeList%3DMB%26searchRadius%3D100&startYear=2015&numRecords=100&firstRecord=0&makeCodeList=MB&searchRadius=100&clickType=alpha'
    headers = {"User-Agent": random.choice(user_agents)}
    
    page_html = urlopen(Request(url, headers=headers))
    bs = soup(page_html, "html.parser")

    extract_page(bs)


if __name__ == '__main__':
    main()
