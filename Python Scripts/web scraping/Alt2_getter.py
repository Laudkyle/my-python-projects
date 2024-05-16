import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the Excel file
file_path = 'publications.csv'  # Update with your file path
df = pd.read_csv(file_path)
df = df.head()

# Function to scrape href links
def scrape_href(link):
    response = requests.get(link)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        div_tag = soup.find('div', {'id': 'gsc_oci_title'})
        if div_tag:
            a_tag = div_tag.find('a', {'class': 'gsc_oci_title_link'})
            if a_tag:
                return a_tag['href']
    return None

# Loop through the URLs and scrape the href links
hrefs = []
for url in df['link']:
    print(url)
    href = scrape_href(url)
    hrefs.append(href)
print(hrefs)
# Add the scraped hrefs to the dataframe
df['Scraped_Links'] = hrefs

# Save the updated dataframe to a new Excel file
output_file_path = 'abstract_links.xlsx'  # Update with your desired output file path
df.to_excel(output_file_path, index=False)

print("Scraping completed and saved to the new Excel file.")