import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://scholar.ucc.edu.gh/publications"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all table rows
rows = soup.find_all('datatable-body-row')

# Open a file for writing
with open('output.txt', 'w') as f:
    # Loop through each row and extract title and link
    for row in rows:
        link_element = row.find('a', class_='show-ellipsis small')
        title = link_element['title']
        link = link_element['href']
        f.write("Title: {}\n".format(title))
        f.write("Link: {}\n".format(link))
        f.write("\n")  # Add a newline between entries

print("Data has been written to output.txt file.")
