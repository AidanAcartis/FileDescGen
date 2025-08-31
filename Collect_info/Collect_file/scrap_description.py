import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Initialize the browser
driver = uc.Chrome()

try:
    driver.get("https://chat.openai.com/")

    #Wait for the input zone
    wait = WebDriverWait(driver, 15)
    text_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ProseMirror")))

    print("Found the input zone!!")

    #Send the input and ENter
    text_input.send_keys("", Keys.ENTER)
    print("Input sended!!")

    #Wait for the response
    time.sleep(60)

    # Verify if the response is found
    messages = driver.find_elements(By.CSS_SELECTOR, "div.markdown")
    if messages:
        print("Response :", messages[-1].text)
    else:
        print("No response found.")


except Exception as e:
    print("Error :", e)

finally:
    driver.quit()
    print("Quit!!")