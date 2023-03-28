from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

start = time.time()

# Function that 'clicks' the "Show More" button to dynamically load more data
def showmore_clicker():
    count=0
    while True:
        try:
            show_more = driver.find_element(By.XPATH, '//*[@id="show-more"]')
            show_more.click()
            count+=1
            print('Show More clicked. Left: ', 379-count) # 379 is the number of clicks it takes to load all the data. Found by trial
            time.sleep(1)
        except:
            print("No more buttons")
            break
    print("Times clicked:", count)

# URL of ICAHN website
url = 'https://icahn.mssm.edu/find-a-faculty?type=faculty'

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# make a Chrome webdriver instance
driver = webdriver.Chrome(options=options)

# open the webpage
driver.get(url)

# Click 'show more'
showmore_clicker()

# store html structure to be parsed
html = driver.page_source
doc = BeautifulSoup(html, 'html.parser') # parse using BeautifulSoup

# Find the master div tag containing the blocks of data
blocks = doc.find_all(['div'], class_='data')

details = []

print('Getting Data...')

# for each person
for block in blocks:
    blocklist = list(block)
    
    name = blocklist[3].text            # get name
    title = blocklist[5].text           # get title (speciality)
    tel = str(blocklist[7].text)[5:]    # get phone number (Sliced by 5 indices to omit non numberic characters)
    email = blocklist[9].text           # get email

    # store values in dictionary
    dic = {
        'Name': name,
        'Title': title,
        'Telephone': tel,
        'Email': email
    }

    # add entries to a list
    details.append(dic)
    
# convert list of entries into a DataFrame table
df = pd.DataFrame(details)

# Store table in Excel file
df.to_excel(r"C:\Users\ga201\Desktop\ICAHN_data.xlsx", index=False)

end = time.time()
total = end - start

print('Done')
print('Time taken: ', time.strftime("%H:%M:%S", time.gmtime(total)))