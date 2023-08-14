from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys

# Specify the path to the ChromeDriver executable
chrome_driver_path = 'C:\Program Files\chromedriver-win64\chromedriver.exe'

# Create a ChromeDriver service instance
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Create a Chrome WebDriver instance using the service
driver = webdriver.Chrome(service=chrome_service)

# Open a website
desired_url = 'https://www.google.com'  # Replace with the URL you want to open
driver.get(desired_url)

# Get the actual URL and title
actual_url = driver.current_url
title = driver.title

# Check if the opened URL is the correct one
if actual_url == desired_url:
    print(f"Opened URL: {actual_url}")
    print(f"Title: {title}")
else:
    print(f"Expected URL: {desired_url}")
    print(f"Actual URL: {actual_url}")
    print(f"Title: {title}")

# Find the search input element by its name attribute
search_input = driver.find_element('name', 'q')

# Enter a search query
search_input.send_keys('Selenium automation')

# Simulate pressing Enter
search_input.send_keys(Keys.RETURN)

# Find the search results
search_results = driver.find_elements('css selector', 'div.g')

# Print the titles of the search results
for result in search_results:
    title = result.find_element('css selector', 'h3').text
    print(title)

# Close the browser tab and quit the WebDriver
driver.quit()
