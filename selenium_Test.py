from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Navigate to Google
driver.get('https://www.google.com')

# Find the search input element by name and type a query
search_input = driver.find_element("name", "q")

# Type a query and press Enter
search_input.send_keys("Selenium WebDriver")
search_input.send_keys(Keys.RETURN)

# Find search result elements using CSS selector
search_results = driver.find_elements("css selector", "div.g")

# Wait for search results to load
wait = WebDriverWait(driver, 10)
search_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.g')))

# Print the titles of the search results
for result in search_results:
    title = result.find_element("css selector", "h3").text
    print(title)

# Close the browser
driver.quit()