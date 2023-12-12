# Using Company's URL we can extract all the EV vehicles related to the particular company.

import requests
from bs4 import BeautifulSoup

def collect_evs_links():
    list_of_ev_links = []
    url = 'https://www.91wheels.com/scooters/okinawa'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    box = soup.find('div', class_='vehicle_card_style__CResultList-sc-1mqhyos-6 hbrKZU')
    scooter_details = box.find_all('div', class_='vehicle_card_style__CardHolder-sc-1mqhyos-3 bpCyOy')

    for scooter_detail in scooter_details:
        scooter_links = scooter_detail.find_all('a', href=True)
        for ev in scooter_links:
            href = ev['href']
            if not href.endswith("price-in-new-delhi"):
                list_of_ev_links.append(href)

    return list_of_ev_links

evs_links = collect_evs_links()
for url in evs_links:
    print(url)
