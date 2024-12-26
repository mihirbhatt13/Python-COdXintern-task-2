from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Initialize WebDriver
driver = webdriver.Chrome()  # Replace with your preferred browser

# Perform Google Search
driver.get("https://www.google.com/")
search_box = driver.find_element("name", "q")
search_box.send_keys("your_search_term")
search_box.send_keys(Keys.RETURN)

# Extract Search Results
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

results = soup.find_all("div", class_="tF2Cxc") 

for result in results:
    title = result.find("h3").text
    link = result.find("a")["href"]
    description = result.find("div", class_="s3v9rd").text
    print(f"Title: {title}\nLink: {link}\nDescription: {description}\n")

# Close WebDriver
driver.quit()
