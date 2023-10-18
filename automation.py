from re import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.google.com/")
driver.maximize_window()

search_input = driver.find_element("name", "q")
search_input.send_keys("Why you should hire veterans")

time.sleep(2)

search_input.submit()

time.sleep(3)

# Click the first link in the search results (updated method)
search_results = driver.find_elements("xpath", "//h3")
if search_results:
    first_result = search_results[0] 
    first_result.click()
    
scroll_pause_time = 1
scroll_step = 200
scrolls = 10

for _ in range(scrolls):
    driver.execute_script("window.scrollBy(0, " + str(scroll_step) + ");")
    time.sleep(scroll_pause_time)
    
time.sleep(4)
    
driver.get("https://www.google.com")

time.sleep(2)

search_input = driver.find_element("name", "q")
search_input.send_keys("automation")

search_input.submit()
    
time.sleep(3)

image_links = driver.find_elements("xpath", "//a[@href]")
for link in image_links:
    if "Images" in link.get_attribute("innerHTML"):
        link.click()
        break
    
time.sleep(3)

book_links = driver.find_elements("xpath", "//a")
for link in book_links:
    if "Books" in link.text:
        link.click()
        break
    
time.sleep(3)

# Click the first link in the search results (updated method)
search_results = driver.find_elements("xpath", "//h3")
if search_results:
    first_result = search_results[0]
    first_result.click()
    
time.sleep(3)
    

driver.quit()


