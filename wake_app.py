import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
APP_URL = "https://sbskkz5w96tlxlsmvkcha7.streamlit.app/"
def wake_streamlit():
    print(f"Visiting Streamlit App: {APP_URL}")
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(APP_URL)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        wake_button = None
        for button in buttons:
            if "Yes, get this app back up" in button.text or "Wake up" in button.text:
                wake_button = button
                break
        if wake_button:
            print("App is asleep! Clicking the wake-up button...")
            wake_button.click()
            time.sleep(10) 
            print("Wake up signal sent successfully.")
        else:
            print("App is already awake or button wasn't found.") 
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
if __name__ == "__main__":
    wake_streamlit()