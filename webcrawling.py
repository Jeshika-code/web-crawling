#installing selenium package and then import webdriver
from selenium import webdriver
# chromedriver path
driver = webdriver.Chrome(r'C:\Users\HP\Desktop\chromedriver.exe')
#website url
driver.get('https://www.weather-forecast.com/countries/Nepal')
# xpath of the data to crawl
places = driver.find_elements_by_xpath('//span[@class="b-list-table_item-name"]')
temp = driver.find_elements_by_xpath('//span[@class="temp"]')
number1 = len(places)
number2 = len(temp)
with open("weather.txt","w") as f:
    for i in range(number1):
      f.write(places[i].text + "temperature is" + temp[i].text + "\n")

driver.close()
