import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Setup WebDriver path and options
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the jQuery UI Droppable demo page
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)  # Wait for the page to load completely

# Switch to the iframe that contains the draggable and droppable elements
iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(iframe)

# Locate the draggable and droppable elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")
# Perform drag and drop operation
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Wait to observe the result
time.sleep(3)

# Print confirmation
print("Drag and drop operation performed successfully.")

# Close the browser
driver.quit()