import requests
from bs4 import BeautifulSoup
#./books/Scripts/Activate.ps1
# Step 1: Website URL to scrape
url = "https://books.toscrape.com/"

# Step 2: Send GET request
response = requests.get(url)

if response.status_code == 200:
    print("Website accessed successfully")
else:
    print("Failed to access website")
    exit()

# Step 3: Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all book containers
books = soup.find_all("article", class_="product_pod")

# Step 5: Loop through each book and extract details
for book in books:
    # Title
    title = book.h3.a["title"]

    # Price
    price = book.find("p", class_="price_color").text

    # Star rating
    # The rating is in the class name of <p class="star-rating ...">
    rating = book.find("p",class_="star-rating")["class"]
    rat = rating[-1]
    # Availability (in stock or not)
    availability = book.find("p", class_="instock availability").text.strip() # trim in java/javscript
    stocks = book.find("p",class_ ="instock availability").text.strip()
    img_url =book.find("img")
    url =  "https://books.toscrape.com/" + img_url["src"].replace("../","")


    # Print details
    print("Book Title:", title)
    print("Price:", price)
    print("Star Rating:", rat)
    print("Image URL:", url)
    print("Availability:", availability)
    print("-" * 50)
# Find the <li> with class 'current' inside <ul class="pager"> 
pages = soup.find("ul", class_="pager")
if pages :
    pages  = soup.find("li",class_="current").text.strip()
    print("Pages :",pages)
else: 
    print("No pagination")




