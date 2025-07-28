import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def putValuesInExcel(name,fact,habitat,lifespan,diet) :
    activeWorkSheet.append([name,fact,habitat,lifespan,diet])
    
wb = Workbook()

# Send a GET request
url = "https://test-scrape-site.onrender.com/animals.html"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch the webpage.")
    exit()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

#find the list 
animals = soup.find_all(class_="animal-card")

activeWorkSheet = wb.active
for animal in animals :
    name = animal.find('h2').text
    fact = animal.find(class_="fact").text
    habitat = animal.find(class_="habitat").text
    lifespan = animal.find(class_="lifespan").text
    diet = animal.find(class_="diet").text
    putValuesInExcel(name,fact,habitat,lifespan,diet)

wb.save("animals.xlsx")


