# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import os
import time
from unidecode import unidecode

def start():
    print ("[+] PS5 Price Collector v1.0.0")
    print ("[-] Coded By RealSalehn ")
    print ("[-] https://salehn.ir")
    global headers
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def tilno():
    r = requests.get('https://tilno.ir/shop/buy-ps5-console', headers=headers)
    if r.status_code == 200:
        try:
            global tilno_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_value = soup.find_all('div', attrs={'class': 'summary-inner'})
            price_value = section_value
            price_value = soup.find_all('p', attrs={'class': 'price'})
            tilno_price = price_value[0].text.strip()
            if tilno_price == "تماس بگیرید":
                tilno_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar Tilno Mojod Nist!")
            else:
                tilno_price = re.sub(r'\D+', '', tilno_price)
                tilno_price = unidecode(tilno_price)
                print("Gheymat PS5 Dar Tilno:", tilno_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")
    
    r = requests.get('https://tilno.ir/shop/buy-ps5-digital-console', headers=headers)
    if r.status_code == 200:
        try:
            global tilno_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_digital_value = soup.find_all('div', attrs={'class': 'summary-inner'})
            price_digital_value = section_digital_value
            price_digital_value = soup.find_all('p', attrs={'class': 'price'})
            tilno_digital_price = price_digital_value[0].text.strip()
            if tilno_digital_price == "تماس بگیرید":
                tilno_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar Tilno Mojod Nist!")
            else:
                tilno_digital_price = re.sub(r'\D+', '', tilno_digital_price)
                tilno_digital_price = unidecode(tilno_digital_price)
                print("Gheymat PS5 Digital Dar Tilno:", tilno_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")



def dragonshop():
    r = requests.get('https://dragon-shop.ir/product/%d8%ae%d8%b1%db%8c%d8%af-playstation-5-%d9%be%d9%84%db%8c-%d8%a7%d8%b3%d8%aa%db%8c%d8%b4%d9%86-5', headers=headers)
    if r.status_code == 200:
        try:
            global dragonshop_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_value = soup.find_all('div', attrs={'class': 'row'})
            price_value = section_value
            price_value = soup.find_all('p', attrs={'class': 'price'})
            if soup.find_all('ins'):
                price_value = soup.find_all('ins')
                dragonshop_price = price_value[0].text.strip()
                dragonshop_price = re.sub(r'\D+', '', dragonshop_price)
                dragonshop_price = unidecode(dragonshop_price)
                print("Gheymat PS5 Dar Dragon-Shop:", dragonshop_price)
            else:
                dragonshop_price = price_value[0].text.strip()
                if dragonshop_price == "تماس بگیرید":
                    dragonshop_price = "قیمت ناموجود"
                    print("Gheymat PS5 Dar Dragon-Shop Mojod Nist!")
                else:
                    dragonshop_price = re.sub(r'\D+', '', dragonshop_price)
                    dragonshop_price = unidecode(dragonshop_price)
                    print("Gheymat PS5 Dar Dragon-Shop:", dragonshop_price)
        except:
            print("Gheymat PS5 Dar Dragon-Shop Mojod Nist!")
    else:
        print("Connection Error! Please Try Again.")
    
    r = requests.get('https://dragon-shop.ir/product/%D8%AE%D8%B1%DB%8C%D8%AF-playstation-5-%D9%BE%D9%84%DB%8C-%D8%A7%D8%B3%D8%AA%DB%8C%D8%B4%D9%86-5-%D8%AF%DB%8C%D8%AC%DB%8C%D8%AA%D8%A7%D9%84', headers=headers)
    if r.status_code == 200:
        try:
            global dragonshop_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_digital_value = soup.find_all('div', attrs={'class': 'summary entry-summary col-lg-24 col-md-24 col-sm-21 col-xs-36'})
            price_digital_value = section_digital_value
            price_digital_value = soup.find_all('p', attrs={'class': 'price'})
            if soup.find_all('ins'):
                dragonshop_digital_price = price_digital_value[0].text.strip()
                dragonshop_digital_price = re.sub(r'\D+', '', dragonshop_digital_price)
                dragonshop_digital_price = unidecode(dragonshop_digital_price)
                print("Gheymat PS5 Digital Dar Dragon-Shop:", dragonshop_digital_price)
            else:
                dragonshop_digital_price = price_digital_value[0].text.strip()
                if dragonshop_digital_price == "تماس بگیرید":
                    dragonshop_digital_price = "قیمت ناموجود"
                    print("Gheymat PS5 Digital Dar Dragon-Shop Mojod Nist!")
                else:
                    dragonshop_digital_price = re.sub(r'\D+', '', dragonshop_digital_price)
                    dragonshop_digital_price = unidecode(dragonshop_digital_price)
                    print("Gheymat PS5 Digital Dar Dragon-Shop:", dragonshop_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")


def pspro():
    r = requests.get('https://pspro.ir/playstation-5-standard-edition-white', headers=headers)
    if r.status_code == 200:
        try:
            global pspro_price
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find_all('a', {'class': 'btn btn-lg btn-block red-btn'}):
                pspro_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar PSPro Mojod Nist!")
            else:
                section_value = soup.find_all('div', attrs={'class': 'col-6 d-flex flex-column justify-content-between px-4'})
                price_value = section_value
                price_value = soup.find_all('button', attrs={'class': 'btn btn-lg btn-block green-btn'})
                pspro_price = price_value[0].text.strip()
                pspro_price = re.sub(r'(\D+)', '', pspro_price)
                pspro_price = unidecode(pspro_price)
                print("Gheymat PS5 Dar PSPro:", pspro_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")

    r = requests.get('https://pspro.ir/PlayStation-5-Digital-Edition-825GB-R2-CFI-1016B', headers=headers)
    if r.status_code == 200:
        try:
            global pspro_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find_all('a', {'class': 'btn btn-lg btn-block red-btn'}):
                pspro_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar PSPro Mojod Nist!")
            else:
                section_digital_value = soup.find_all('div', attrs={'class': 'col-6 d-flex flex-column justify-content-between px-4'})
                price_digital_value = section_digital_value
                price_digital_value = soup.find_all('button', attrs={'class': 'btn btn-lg btn-block green-btn'})
                pspro_digital_price = price_digital_value[0].text.strip()
                pspro_digital_price = re.sub(r'(\D+)', '', pspro_digital_price)
                pspro_digital_price = unidecode(pspro_digital_price)
                print("Gheymat PS5 Dar PSPro:", pspro_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")



def techsiro():
    r = requests.get('https://techsiro.com/product/ps5-standard-edition-825gb-white-cfi-1015a', headers=headers)
    if r.status_code == 200:
        try:
            global techsiro_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_value = soup.find_all('div', attrs={'class': 'summary entry-summary'})
            price_value = section_value
            if soup.find_all('p', attrs={'class': 'stock out-of-stock'}):
                techsiro_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar Techsiro Mojod Nist!")
            else:
                price_value = soup.find_all('p', attrs={'class': 'price'})
                techsiro_price = price_value[0].text.strip()
                if techsiro_price == "تماس بگیرید":
                    techsiro_price = "قیمت ناموجود"
                    print("Gheymat PS5 Dar Techsiro Mojod Nist!")
                else:
                    techsiro_price = re.sub(r'\D+', '', techsiro_price)
                    techsiro_price = unidecode(techsiro_price)
                    print("Gheymat PS5 Dar Techsiro:", techsiro_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")
    
    r = requests.get('https://techsiro.com/product/ps5-digital-edition-825gb-white-cfi-1016b', headers=headers)
    if r.status_code == 200:
        try:
            global techsiro_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_digital_value = soup.find_all('div', attrs={'class': 'summary-inner'})
            price_digital_value = section_digital_value
            if soup.find_all('p', attrs={'class': 'stock out-of-stock'}):
                techsiro_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar Techsiro Mojod Nist!")
            else:
                price_digital_value = soup.find_all('p', attrs={'class': 'price'})
                techsiro_digital_price = price_digital_value[0].text.strip()
                if techsiro_digital_price == "تماس بگیرید":
                    techsiro_digital_price = "قیمت ناموجود"
                    print("Gheymat PS5 Digital Dar Techsiro Mojod Nist!")
                else:
                    techsiro_digital_price = re.sub(r'\D+', '', techsiro_digital_price)
                    techsiro_digital_price = unidecode(techsiro_digital_price)
                    print("Gheymat PS5 Digital Dar Techsiro:", techsiro_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")


def gamiha():
    r = requests.get('https://gamiha.net/shop/playstation5/P335-ps5.html', headers=headers)
    if r.status_code == 200:
        try:
            global gamiha_price
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find_all('div', {'class': 'wz-shop-product-out-stock'}):
                gamiha_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar Gamiha Mojod Nist!")
            else:
                section_value = soup.find_all('div', attrs={'class': 'wz-shop-product-section'})
                price_value = section_value
                if soup.find_all('span', {'class': 'wz-shop-product-sale-price'}):
                    price_value = soup.find_all('span', attrs={'class': 'wz-shop-product-sale-price'})
                    gamiha_price = price_value[0].text.strip()
                    gamiha_price = re.sub(r'\D+', '', gamiha_price)
                    gamiha_price = unidecode(gamiha_price)
                    print("Gheymat PS5 Dar Gamiha:", gamiha_price)
                else:
                    price_value = soup.find_all('div', attrs={'class': 'wz-shop-product-price'})
                    gamiha_price = price_value[0].text.strip()
                    gamiha_price = re.sub(r'\D+', '', gamiha_price)
                    gamiha_price = unidecode(gamiha_price)
                    print("Gheymat PS5 Dar Gamiha:", gamiha_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")

    r = requests.get('https://gamiha.net/shop/playstation-5-digital/P605-%DA%A9%D9%86%D8%B3%D9%88%D9%84-%D8%A8%D8%A7%D8%B2%DB%8C-%D8%B3%D9%88%D9%86%DB%8C-%D9%85%D8%AF%D9%84-%D9%BE%D9%84%DB%8C-%D8%A7%D8%B3%D8%AA%DB%8C%D8%B4%D9%86-%DB%B5-%D8%AF%DB%8C%D8%AC%DB%8C%D8%AA%D8%A7%D9%84.html', headers=headers)
    if r.status_code == 200:
        try:
            global gamiha_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find_all('div', {'class': 'wz-shop-product-out-stock'}):
                gamiha_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar Gamiha Mojod Nist!")
            else:
                section_digital_value = soup.find_all('div', attrs={'class': 'wz-shop-product-section'})
                price_digital_value = section_digital_value
                if soup.find_all('span', {'class': 'wz-shop-product-sale-price'}):
                    price_digital_value = soup.find_all('span', attrs={'class': 'wz-shop-product-sale-price'})
                    gamiha_digital_price = price_digital_value[0].text.strip()
                    gamiha_digital_price = re.sub(r'\D+', '', gamiha_digital_price)
                    gamiha_digital_price = unidecode(gamiha_digital_price)
                    print("Gheymat PS5 Digital Dar Gamiha:", gamiha_digital_price)
                else:
                    price_digital_value = soup.find_all('div', attrs={'class': 'wz-shop-product-price'})
                    gamiha_digital_price = price_digital_value[0].text.strip()
                    gamiha_digital_price = re.sub(r'\D+', '', gamiha_digital_price)
                    gamiha_digital_price = unidecode(gamiha_digital_price)
                    print("Gheymat PS5 Digital Dar Gamiha:", gamiha_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")


def timcheh():
    r = requests.get('https://timcheh.com/product/tpi-8378', headers=headers)
    if r.status_code == 200:
        try:
            global timcheh_price
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find_all('h4', {'class': 'product_styles_unavailable_title__2XMnW product_styles_unavailable__GKiyV'}):
                timcheh_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar Timcheh Mojod Nist!")
            else:
                section_value = soup.find_all('div', attrs={'class': 'product_styles_product_info_holder__9IC6k'})
                price_value = section_value
                price_value = soup.find_all('span', attrs={'class': 'product_styles_price__3Ws3t'})
                timcheh_price = price_value[0].text.strip()
                timcheh_price = re.sub(r'\D+', '', timcheh_price)
                print("Gheymat PS5 Dar timcheh:", timcheh_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")

    r = requests.get('https://timcheh.com/product/tpi-8374', headers=headers)
    if r.status_code == 200:
        try:
            global timcheh_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find_all('h4', {'class': 'product_styles_unavailable_title__2XMnW product_styles_unavailable__GKiyV'}):
                timcheh_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar timcheh Mojod Nist!")
            else:
                section_digital_value = soup.find_all('div', attrs={'class': 'product_styles_product_info_holder__9IC6k'})
                price_digital_value = section_digital_value
                price_digital_value = soup.find_all('span', attrs={'class': 'product_styles_price__3Ws3t'})
                timcheh_digital_price = price_digital_value[0].text.strip()
                timcheh_digital_price = re.sub(r'\D+', '', timcheh_digital_price)
                print("Gheymat PS5 Digital Dar timcheh:", timcheh_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")


def lioncomputer():
    r = requests.get('https://www.lioncomputer.com/product/48766/Sony-PlayStation-5-With-Blu-Ray-Drive-Console-PS5', headers=headers)
    if r.status_code == 200:
        try:
            global lioncomputer_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_value = soup.find_all('div', attrs={'class': 'col-lg-6 col-sm-12'})
            price_value = section_value
            price_value = soup.find_all('strong', attrs={'class': 'text-success font-size-large font-weight-bold mt-2'})
            lioncomputer_price = price_value[0].text.strip()
            if lioncomputer_price == "ناموجود":
                lioncomputer_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar Lioncomputer Mojod Nist!")
            else:
                lioncomputer_price = re.sub(r'\D+', '', lioncomputer_price)
                lioncomputer_price = unidecode(lioncomputer_price)
                print("Gheymat PS5 Dar Lioncomputer:", lioncomputer_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")

    r = requests.get('https://www.lioncomputer.com/product/gqlm1/Sony-PlayStation-5-CFI-1015B-Digital-Edition-PS5-Console', headers=headers)
    if r.status_code == 200:
        try:
            global lioncomputer_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_digital_value = soup.find_all('div', attrs={'class': 'col-lg-6 col-sm-12'})
            price_digital_value = section_digital_value
            price_digital_value = soup.find_all('strong', attrs={'class': 'text-success font-size-large font-weight-bold mt-2'})
            lioncomputer_digital_price = price_digital_value[0].text.strip()
            if lioncomputer_digital_price == "ناموجود":
                lioncomputer_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar Lioncomputer Mojod Nist!")
            else:
                lioncomputer_digital_price = re.sub(r'\D+', '', lioncomputer_digital_price)
                lioncomputer_digital_price = unidecode(lioncomputer_digital_price)
                print("Gheymat PS5 Digital Dar Lioncomputer:", lioncomputer_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")


def nakhlmarket():
    r = requests.get('https://nakhlmarket.com/product/playstation-5', headers=headers)
    if r.status_code == 200:
        try:
            global nakhlmarket_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_value = soup.find_all('div', attrs={'class': 'summary-inner'})
            section_value = soup.find_all('div', attrs={'class': 'single_variation_wrap'})
            price_value = section_value
            price_value = soup.find_all('span', attrs={'class': 'price'})
            price_value = soup.find_all('bdi', attrs={'class': ''})
            nakhlmarket_price = price_value[2].text.strip()
            if nakhlmarket_price == "تماس بگیرید":
                nakhlmarket_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar Nakhlmarket Mojod Nist!")
            else:
                nakhlmarket_price = re.sub(r'\D+', '', nakhlmarket_price)
                print("Gheymat PS5 Dar Nakhlmarket:", nakhlmarket_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")

    r = requests.get('https://nakhlmarket.com/product/buy-ps5-digital-edition', headers=headers)
    if r.status_code == 200:
        try:
            global nakhlmarket_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_digital_value = soup.find_all('div', attrs={'class': 'summary-inner'})
            section_digital_value = soup.find_all('div', attrs={'class': 'single_variation_wrap'})
            price_digital_value = section_digital_value
            price_digital_value = soup.find_all('span', attrs={'class': 'price'})
            price_digital_value = soup.find_all('bdi', attrs={'class': ''})
            nakhlmarket_digital_price = price_digital_value[2].text.strip()
            if nakhlmarket_digital_price == "تماس بگیرید":
                nakhlmarket_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar Nakhlmarket Mojod Nist!")
            else:
                nakhlmarket_digital_price = re.sub(r'\D+', '', nakhlmarket_digital_price)
                print("Gheymat PS5 Digital Dar Nakhlmarket:", nakhlmarket_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")


def zirpele():
    r = requests.get('https://zirpele.ir/product/%D8%AE%D8%B1%DB%8C%D8%AF-ps5-%D9%BE%D9%84%DB%8C-%D8%A7%D8%B3%D8%AA%DB%8C%D8%B4%D9%86-playstation-5', headers=headers)
    if r.status_code == 200:
        try:
            global zirpele_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_value = soup.find_all('div', attrs={'class': 'col-lg-28 col-md-28 col-sm-36 col-xs-36'})
            price_value = section_value
            price_value = soup.find_all('p', attrs={'class': 'price'})
            zirpele_price = price_value[0].text.strip()
            if zirpele_price == "تماس بگیرید":
                zirpele_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar Zirpele Mojod Nist!")
            else:
                zirpele_price = re.sub(r'\D+', '', zirpele_price)
                print("Gheymat PS5 Dar Zirpele:", zirpele_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")
    
    r = requests.get('https://zirpele.ir/product/ps5-%d9%be%d9%84%db%8c-%d8%a7%d8%b3%d8%aa%db%8c%d8%b4%d9%86-playstation-5-digital', headers=headers)
    if r.status_code == 200:
        try:
            global zirpele_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            section_digital_value = soup.find_all('div', attrs={'class': 'col-lg-28 col-md-28 col-sm-36 col-xs-36'})
            price_digital_value = section_digital_value
            price_digital_value = soup.find_all('p', attrs={'class': 'price'})
            zirpele_digital_price = price_digital_value[0].text.strip()
            if zirpele_digital_price == "تماس بگیرید":
                zirpele_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar Zirpele Mojod Nist!")
            else:
                zirpele_digital_price = re.sub(r'\D+', '', zirpele_digital_price)
                print("Gheymat PS5 Digital Dar Zirpele:", zirpele_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")


def digikala():
    r = requests.get('https://www.digikala.com/product/dkp-3737956/%DA%A9%D9%86%D8%B3%D9%88%D9%84-%D8%A8%D8%A7%D8%B2%DB%8C-%D8%B3%D9%88%D9%86%DB%8C-%D9%85%D8%AF%D9%84-playstation-5-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-825-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA', headers=headers)
    if r.status_code == 200:
        try:
            global digikala_price
            soup = BeautifulSoup(r.text, 'html.parser')
            find_ava = soup.find_all('div', attrs={'class': 'c-product__summary js-product-summary'})
            if soup.find_all('i', attrs={'class': 'c-product-stock__action--alarm-icon'}):
                digikala_price = "قیمت ناموجود"
                print("Gheymat PS5 Dar Digikala Mojod Nist!")
            else:
                section_value = soup.find_all('div', attrs={'class': 'c-product__summary js-product-summary'})
                price_value = section_value
                price_value = soup.find_all('div', attrs={'class': 'c-product__seller-price-pure js-price-value'})
                digikala_price = price_value[0].text.strip()
                digikala_price = re.sub(r'\D+', '', digikala_price)
                digikala_price = unidecode(digikala_price)
                print("Gheymat PS5 Dar Digikala:", digikala_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")

    r = requests.get('https://www.digikala.com/product/dkp-3738470/%DA%A9%D9%86%D8%B3%D9%88%D9%84-%D8%A8%D8%A7%D8%B2%DB%8C-%D8%B3%D9%88%D9%86%DB%8C-%D9%85%D8%AF%D9%84-playstation-5-digital-edition-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-825-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA', headers=headers)
    if r.status_code == 200:
        try:
            global digikala_digital_price
            soup = BeautifulSoup(r.text, 'html.parser')
            find_ava = soup.find_all('div', attrs={'class': 'c-product__summary js-product-summary'})
            if soup.find_all('i', attrs={'class': 'c-product-stock__action--alarm-icon'}):
                digikala_digital_price = "قیمت ناموجود"
                print("Gheymat PS5 Digital Dar Digikala Mojod Nist!")
            else:
                section_digital_value = soup.find_all('div', attrs={'class': 'c-product__summary js-product-summary'})
                price_digital_value = section_digital_value
                price_digital_value = soup.find_all('div', attrs={'class': 'c-product__seller-price-pure js-price-value'})
                digikala_digital_price = price_digital_value[0].text.strip()
                digikala_digital_price = re.sub(r'\D+', '', digikala_digital_price)
                digikala_digital_price = unidecode(digikala_digital_price)
                print("Gheymat PS5 Digital Dar Digikala:", digikala_digital_price)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")

def save():
    f = open("PS5.txt", "a", encoding="utf-8")
    f.write("تاریخ قیمت ها:")
    f.write(date)
    f.write("\n")
    f.write("======== Tilno.ir ========\n")
    f.write("معمولی:\n")
    f.write(tilno_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(tilno_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== Dragon-shop.ir ========\n")
    f.write("معمولی:\n")
    f.write(dragonshop_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(dragonshop_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== PSPro.ir ========\n")
    f.write("معمولی:\n")
    f.write(pspro_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(pspro_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== Techsiro.com ========\n")
    f.write("معمولی:\n")
    f.write(techsiro_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(techsiro_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== Gamiha.net ========\n")
    f.write("معمولی:\n")
    f.write(gamiha_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(gamiha_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== Timcheh.com ========\n")
    f.write("معمولی:\n")
    f.write(timcheh_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(timcheh_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== Lioncomputer.com ========\n")
    f.write("معمولی:\n")
    f.write(lioncomputer_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(lioncomputer_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== Nakhlmarket.com ========\n")
    f.write("معمولی:\n")
    f.write(nakhlmarket_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(nakhlmarket_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== Zirpele.ir ========\n")
    f.write("معمولی:\n")
    f.write(zirpele_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(zirpele_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.write("======== Digikala.com ========\n")
    f.write("معمولی:\n")
    f.write(digikala_price)
    f.write("\n")
    f.write("دیجیتال:\n")
    f.write(digikala_digital_price)
    f.write("\n")
    f.write("=======================\n")
    f.close()

def get_date():
    r = requests.get('https://www.time.ir', headers=headers)
    if r.status_code == 200:
        try:
            global date
            soup = BeautifulSoup(r.text, 'html.parser')
            find_tag = soup.find_all('span', attrs={'id': 'ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsiNumeral'})
            date = find_tag
            date = date[0].text.strip()
            date = unidecode(date)
            print(date)
        except:
            print("Error! Something is wrong.")
    else:
        print("Connection Error! Please Try Again.")

if __name__ == '__main__':
    start()
    get_date()
    tilno()
    dragonshop()
    pspro()
    techsiro()
    gamiha()
    timcheh()
    lioncomputer()
    nakhlmarket()
    zirpele()
    digikala()
    save()

