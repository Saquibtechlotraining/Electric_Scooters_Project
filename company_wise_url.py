# Company_Wise URLS

import requests
from bs4 import BeautifulSoup

# The URL of the webpage containing scooter links
base_url = "https://www.91wheels.com/electric-scooters"  # Replace with the actual URL

# Send an HTTP GET request to the main page
response = requests.get(base_url)

# Define URL suffixes to exclude
exclude_suffixes = ['/256524', '/190930', '/172777', '/256542', '/256610', '/images']

if response.status_code == 200:
    # Parse the HTML content of the main page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor (a) tags with 'href' attribute
    scooter_links = soup.find_all('a', href=True)

    # Create a list to store the individual electric scooter URLs
    individual_scooter_urls = []

    # Iterate through the links on the main page
    for link in scooter_links:
        scooter_url = link['href']
        if '/scooters/' in scooter_url and 'scooters/' in scooter_url:
            individual_scooter_urls.append(scooter_url)

        # Additional condition to capture URLs ending with "scooters"
        if scooter_url.endswith("scooters"):
            individual_scooter_urls.append(scooter_url)

    # Remove duplicates and filter for URLs starting with 'https://www.91wheels.com' and not ending with excluded suffixes
    all_urls = list(set(individual_scooter_urls))
    for url in all_urls:
        if url.startswith('https://www.91wheels.com') and not url.endswith(tuple(exclude_suffixes)):
            print(url)

else:
    print(f"Failed to fetch the main page. Status code: {response.status_code}")


