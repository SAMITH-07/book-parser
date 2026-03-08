# *********************** SELENIUM WEB SCRAPING – UPDATED VERSION *************************
#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ------------------- CONFIGURATION -------------------

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

print("Chrome browser started")

# ------------------- CONFIGURATION -------------------

pages = 2         # -1 = ALL pages | 2,3,4 = limited pages
output_file = "books_selenium.json"

# ------------------- OPEN WEBSITE -------------------

url = "https://books.toscrape.com/"
driver.get(url)
print("Website opened")

# ------------------- DATA STORAGE -------------------

all_books = []
current_page = 1

# ------------------- PAGINATION LOOP -------------------

while True:

    # Stop if page limit reached (except -1)
    if pages != -1 and current_page > pages:
        break

    print(f"\nScraping Page {current_page}")

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod"))
    )

    books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    print(f"Books found: {len(books)}")

    # ------------------- SCRAPE BOOK DETAILS -------------------

    for book in books:
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price = book.find_element(By.CSS_SELECTOR, "p.price_color").text

        # ⭐ Rating
        rating_class = book.find_element(
            By.CSS_SELECTOR, "p.star-rating"
        ).get_attribute("class")
        rating = rating_class.split()[-1]

        # 🖼 Image URL
        image_url = book.find_element(By.TAG_NAME, "img").get_attribute("src")

        # 📦 Availability
        availability = book.find_element(
            By.CSS_SELECTOR, "p.instock.availability"
        ).text.strip()

        all_books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "image_url": image_url,
            "availability": availability,
            "page": current_page
        })

        print(title, "|", price, "|", rating)

    # ------------------- CLICK NEXT -------------------

    try:
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.next a"))
        )
        next_button.click()
        current_page += 1
        time.sleep(2)  # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod"))
        )
    except:
        print("Last page reached")
        break

# ------------------- SAVE DATA TO JSON -------------------

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(all_books, file, indent=4, ensure_ascii=False)

print("\n✅ Scraping completed successfully")
print(f"📦 Total books scraped: {len(all_books)}")
print(f"📁 Data saved to: {output_file}")

# ------------------- CLOSE BROWSER -------------------

input("Press ENTER to close the browser...")
driver.quit()

# *********************** END OF SCRIPT *************************
