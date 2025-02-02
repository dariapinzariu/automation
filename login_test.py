from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver (Change path to your driver)
driver = webdriver.Chrome()

# Test Data
url = "https://example.com/login"  # Replace with the actual login URL
valid_username = "testuser"
valid_password = "securepassword"

try:
    # Step 1: Open the login page
    driver.get(url)
    driver.maximize_window()
    
    # Step 2: Locate username field and enter valid username
    username_field = driver.find_element(By.ID, "username")  # Adjust selector as needed
    username_field.send_keys(valid_username)

    # Step 3: Locate password field and enter valid password
    password_field = driver.find_element(By.ID, "password")  # Adjust selector as needed
    password_field.send_keys(valid_password)

    # Step 4: Click the login button
    login_button = driver.find_element(By.ID, "login-button")  # Adjust selector as needed
    login_button.click()

    # Step 5: Validate successful login (Check for dashboard element or welcome message)
    time.sleep(3)  # Wait for page to load
    success_message = driver.find_element(By.ID, "welcome-message")  # Adjust selector as needed

    assert "Welcome" in success_message.text, "Login failed!"

    print("Test Passed: User successfully logged in.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser
    driver.quit()
