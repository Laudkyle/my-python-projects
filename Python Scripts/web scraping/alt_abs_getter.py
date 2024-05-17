import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load the CSV file
file_path = 'publications.csv'  # Update with your file path
df = pd.read_csv(file_path)
df =df.head(200)
# Function to scrape href links
def scrape_href(link):
    try:
        response = requests.get(link, timeout=10,headers = {'User-agent': 'bot 0.1'})  # Added timeout for better handling
        print(response.status_code)
        if response.status_code == 429:
            print(response.headers["Retry-After"])
            time.sleep(int(response.headers["Retry-After"]))
        elif response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the specific div tag with id 'gsc_oci_title'
            div_tag = soup.find('div', {'id': 'gsc_oci_title'})
            if div_tag:
                # Find the a tag within this div
                a_tag = div_tag.find('a', {'class': 'gsc_oci_title_link'})
                if a_tag and 'href' in a_tag.attrs:
                    return a_tag['href']
    except requests.RequestException as e:
        print(f"Request failed for URL {link}: {e}")
    return None

# Function to handle scraping with progress bar
def scrape_links_with_progress(links):
    hrefs = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(scrape_href, url): url for url in links}
        for future in tqdm(as_completed(future_to_url), total=len(links), desc="Scraping URLs"):
            url = future_to_url[future]
            try:
                href = future.result()
                hrefs.append(href)
            except Exception as e:
                print(f"Exception occurred for URL {url}: {e}")
                hrefs.append(None)
    return hrefs

# List of URLs to scrape
urls = df['link']

# Scrape the links with multithreading and progress bar
scraped_hrefs = scrape_links_with_progress(urls)

# Add the scraped hrefs to the dataframe
df['Scraped_Links'] = scraped_hrefs

# Save the updated dataframe to a new Excel file
output_file_path = 'abstract_links.xlsx'  # Update with your desired output file path
df.to_excel(output_file_path, index=False)

print("Scraping completed and saved to the new Excel file.")
