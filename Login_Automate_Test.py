# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # Create a Chrome WebDriver instance
# driver = webdriver.Chrome()

# # Navigate to the login page
# driver.get('C:\\Users\\skb21\\Selethon_Practice\\Python_Practice\\Login_Form.html')

# # Find the username and password input fields
# username_input = driver.find_element_by_name('username')
# password_input = driver.find_element_by_name('password')

# # Enter your username and password
# username_input.send_keys('your_username')
# password_input.send_keys('your_password')

# # Submit the form (assuming the login button has a type of "submit")
# login_button = driver.find_element_by_css_selector('button[type="submit"]')
# login_button.click()

# # Wait for a moment to see the result (you can replace this with proper waits)
# driver.implicitly_wait(5)

# # Close the browser
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # Create a Chrome WebDriver instance
# driver = webdriver.Chrome()

# # Navigate to the login page
# driver.get(r'file:///C:/Users/skb21/Selethon_Practice/Python_Practice/Login_Form.html')  # Update the path as needed

# # Find the username and password input fields
# username_input = driver.find_element('name', 'username')  # Update to use find_element method

# # Enter your username and password
# username_input.send_keys('your_username')

# # Find the password input field and enter your password
# password_input = driver.find_element('name', 'password')
# password_input.send_keys('your_password')

# # Submit the form (assuming the login button has a type of "submit")
# login_button = driver.find_element('css selector', 'button[type="submit"]')
# login_button.click()

# # Wait for a moment to see the result (you can replace this with proper waits)
# driver.implicitly_wait(5)

# # Close the browser
# driver.quit()

#version 3
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # Create a Chrome WebDriver instance
# driver = webdriver.Chrome()

# # Navigate to the login page
# driver.get(r'file:///C:/Users/skb21/Selethon_Practice/Python_Practice/Login_Form.html')  # Update the path as needed

# # Find the username and password input fields
# username_input = driver.find_element('name', 'username')
# password_input = driver.find_element('name', 'password')

# # Display the process on screen
# print("Step 1: Navigated to the login page")

# # Enter valid username and password
# username = 'myuser'
# password = 'MyP@ssw0rd'
# username_input.send_keys(username)
# password_input.send_keys(password)

# print("Step 2: Entered username and password")

# # Submit the form (assuming the login button has a type of "submit")
# login_button = driver.find_element('css selector', 'button[type="submit"]')
# login_button.click()

# print("Step 3: Clicked the login button")

# # Wait for the success message to be displayed
# success_message = driver.find_element('id', 'successMessage')
# # Wait for the success message to be visible (you can replace this with proper waits)
# driver.implicitly_wait(5)

# # Display success message on screen
# print("Step 4: Login successful!")

# # Print login credentials used during testing
# print(f"Test Credentials: Username: {username}, Password: {password}")

# # Close the browser
# driver.quit()

#version 4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Navigate to the login page
driver.get(r'C:\Users\Sharddha K B\Desktop\DXC\Selenium_Test_Project-main\Login_Form.html')  # Update the path as needed

# Find the username and password input fields
username_input = driver.find_element('name', 'username')
password_input = driver.find_element('name', 'password')
login_button = driver.find_element('css selector', 'button[type="submit"]')

# Create an ActionChains instance
actions = ActionChains(driver)

# Display the process on screen
print("Step 1: Navigated to the login page")

# Simulate entering username and password
print("Step 2: Entering username and password...")
actions.send_keys_to_element(username_input, 'myuser').perform()
time.sleep(1)  # Pause for visualization
actions.send_keys_to_element(password_input, 'MyP@ssw0rd').perform()
time.sleep(1)  # Pause for visualization

# Simulate clicking the login button
print("Step 3: Clicking the login button...")
actions.move_to_element(login_button).click().perform()
time.sleep(1)  # Pause for visualization

# Wait for the success message to be displayed
success_message = driver.find_element('id', 'successMessage')
# Wait for the success message to be visible (you can replace this with proper waits)
driver.implicitly_wait(5)

# Display success message on screen
print("Step 4: Login successful!")

# Print login credentials used during testing
print("Test Credentials: Username: myuser, Password: MyP@ssw0rd")
print("Test completed successfully!!!")

# Pause to see the final result
time.sleep(3)

# Close the browser
driver.quit()
