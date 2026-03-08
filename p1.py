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
    rating_class = book.find("p", class_="star-rating")["class"]
    # The second class is the rating (One, Two, Three, Four, Five)
    rating = rating_class[1]

    # Image URL
    img_tag = book.find("img")
    img_url = "https://books.toscrape.com/" + img_tag["src"].replace("../", "")

    # Availability (in stock or not)
    availability = book.find("p", class_="instock availability").text.strip() # trim in java/javscript
    stocks = book.find("p",class_ ="instock availability").text.strip()


    # Print details
    print("Book Title:", title)
    print("Price:", price)
    print("Star Rating:", rating)
    print("Image URL:", img_url)
    print("Availability:", availability)
    print("-" * 50)
# Find the <li> with class 'current' inside <ul class="pager">
page_info = soup.find("ul", class_="pager")
if page_info:
    current = page_info.find("li", class_="current").text.strip()
    print("Page Info:", current)
else:
    print("Pagination not found")


