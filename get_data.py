# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import os

# Setup webdriver
service = Service(r"path/to/chromedriver.exe") # Add the local path to chromedrive.exe
browser = webdriver.Chrome(service=service)

# Connect to Google
browser.get("https://www.google.com/")

# Find the search box
search = browser.find_element(By.NAME, "q")

# Enter the search term and press ENTER
search.send_keys("vitiligo skin", Keys.ENTER)

# Wait for the "Images" link to be present and click it
wait = WebDriverWait(browser, 10)  # wait up to 10 seconds
elem = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Images")))
elem.click()

# Scroll and collect images
value = 0
for i in range(20):
   browser.execute_script("scrollBy("+ str(value) +",+1000);")
   value += 1000
   time.sleep(3)

# Find images
elem1 = browser.find_element_by_id("islmp")
sub = elem1.find_elements_by_tag_name("img")

# Create directory if it doesn't exist
try:
    os.mkdir("vitiligo_skin")
except FileExistsError:
    pass

# Download and save images
count = 0
for i in sub:
    src = i.get_attribute('src')
    try:
        if src != None:
            src  = str(src)
            print(src)
            count+=1
            urllib.request.urlretrieve(src, os.path.join('vitiligo_skin','image'+str(count)+'.jpg'))
        else:
            raise TypeError
    except TypeError:
        print('fail')