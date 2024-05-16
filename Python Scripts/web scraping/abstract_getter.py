import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to scrape href links with a specified IP address
def scrape_href_with_ip(link, ip_address):
    try:
        response = requests.get(link, timeout=10,headers={"X-Forwarded-For": ip_address})
        print(response.status_code)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            div_tag = soup.find('div', {'id': 'gsc_oci_title'})
            if div_tag:
                a_tag = div_tag.find('a', {'class': 'gsc_oci_title_link'})
                if a_tag and 'href' in a_tag.attrs:
                    return a_tag['href']
    except requests.RequestException as e:
        print(f"Request failed for URL {link}: {e}")
    return None

# Function to handle scraping with progress bar and specified IP addresses
def scrape_links_with_ips(links, ip_addresses):
    hrefs = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(scrape_href_with_ip, url, ip_address): url for url, ip_address in zip(links, ip_addresses)}
        for future in tqdm(as_completed(future_to_url), total=len(links), desc="Scraping URLs"):
            url = future_to_url[future]
            try:
                href = future.result()
                hrefs.append(href)
            except Exception as e:
                print(f"Exception occurred for URL {url}: {e}")
                hrefs.append(None)
    return hrefs

# Load the CSV file
file_path = 'publications.csv'
df = pd.read_csv(file_path)

# Define the number of rows per chunk
chunk_size = 100

# Split the dataframe into chunks
chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

# Generate a list of virtual IP addresses from 10.0.2.101 to 10.0.3.255
ip_addresses = ['10.0.2.' + str(i) for i in range(101, 256)] + ['10.0.3.' + str(i) for i in range(0, 256)]

# Initialize an empty list to store scraped links
scraped_hrefs = []

# Iterate over chunks and scrape links with corresponding IP addresses
for chunk, ip_address in zip(chunks, ip_addresses):
    # List of URLs to scrape for the current chunk
    urls = chunk['link']
    # Scrape the links with multithreading and progress bar
    chunk_hrefs = scrape_links_with_ips(urls, [ip_address] * len(urls))
    # Add the scraped hrefs to the list
    scraped_hrefs.extend(chunk_hrefs)

# Add the scraped hrefs to the dataframe
df['Scraped_Links'] = scraped_hrefs

# Save the updated dataframe to a new Excel file
output_file_path = 'abstract_links.xlsx'
df.to_excel(output_file_path, index=False)

print("Scraping completed and saved to the new Excel file.")
