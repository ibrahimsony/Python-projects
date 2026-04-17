import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Initialize driver outside the loop, to avoid unexpected crashes or errors
driver = webdriver.Chrome()

def get_price():
    # Use the current price from the page: 1249 kr, this is a dumy page example
    driver.get("https://www.maxgaming.se/sv/verktyg/electric-screwdriver-12v-max-brushless-cordless-drill-tradlos-skruvdragare")
    price = driver.find_element(By.CLASS_NAME, "PrisBOLD")
    print("Item price is: " + price.text)

# 2. Wrap the entire loop in the try/except block
try:
    print("Starting scan... Press the red STOP button in PyCharm to exit.")
    while True:
        get_price()#if interruption happens, don’t enter the function at all, unlke 
                              the old version  
        time.sleep(5)
except KeyboardInterrupt:#pycharm termination button error
    # 3. This catches the PyCharm interruption from keyboard
    print("\n[INFO] Scan terminated by user.")
except Exception as e:#catches an unexpected interruptions
    print(f"\n[ERROR] An unexpected error occurred: {e}")
finally:
    # 4. Ensures the browser closes regardless of how the program ends
    print("Closing browser...")
    driver.quit()#no matter how program terminate will ends with finally error handling block, for proper close. This update in program for fluency in execution issue. 
