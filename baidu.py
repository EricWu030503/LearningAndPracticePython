from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to perform a Baidu search
def perform_baidu_search(query, num_searches):
    # Configure the browser to run in headless mode (invisible)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # Initialize a Selenium WebDriver using 'options'
    driver = webdriver.Chrome(options=options)

    # URL of the Baidu homepage
    url = "https://www.baidu.com"

    # Open the Baidu homepage in the browser
    driver.get(url)

    for _ in range(num_searches):
        # Find the search input element and enter the search query
        search_box = driver.find_element(By.ID, "kw")  # "kw" is the ID of the search input element on Baidu
        search_box.clear()  # Clear any existing text in the search box
        search_box.send_keys(query)

        # Find and click the search button
        search_button = driver.find_element(By.ID, "su")  # "su" is the ID of the search button on Baidu
        search_button.click()

        # Wait for search results to load (you may need to adjust the wait time)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "content_left"))  # "content_left" is the ID of the search results container on Baidu
            )
            print(f"Search for '{query}' was successful. Search results loaded.")
        except Exception as e:
            print(f"Search for '{query}' may not have been successful: {str(e)}")

    # Close the browser window when done
    driver.quit()

# Perform the same search query multiple times
query = ""  # Replace with the actual search query
num_searches = 1000  # Specify the number of times you want to search
perform_baidu_search(query, num_searches)

