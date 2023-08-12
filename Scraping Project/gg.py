import requests
from bs4 import BeautifulSoup

url = "https://www.nmc.org.in/information-desk/indian-medical-register/"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table element containing the data
# table = soup.find("table", class_="table-striped")
print(soup.prettify())