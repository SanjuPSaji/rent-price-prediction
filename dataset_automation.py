from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome('/Users/MyUsername/Downloads/chromedriver')

title_list = []
price_list = []
area_list = []
location_list = []

no_pages = 2

for i in range(1, no_pages + 1):
    driver.get("https://www.makaan.com/pune-residential-property/rent-property-in-pune-city?page=" + str(i))

    titles = driver.find_elements(By.CLASS_NAME, "title-line")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    areas = driver.find_elements(By.CLASS_NAME, "size")
    locations = driver.find_elements(By.CLASS_NAME, "locName")

    for title, price, area, location in zip(titles, prices, areas, locations):
        title_list.append(title.text)
        price_list.append(price.text)
        area_list.append(area.text)
        location_list.append(location.text)

driver.quit()

data = {
    "Title": title_list,
    "Price": price_list,
    "Area": area_list,
    "Location": location_list
}
df = pd.DataFrame(data)

df.to_csv('scraped_data.csv', index=False)
