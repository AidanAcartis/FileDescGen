import time
import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

input_file = "Files_list.jsonl"
output_file = "response.jsonl"

prompt_template = """Describe the following file. Include:
- what it is according to the extension ({ext})
- what he does according to his name ({fname})
- where it is located ({directory})
- which application opens it ({app})

File : {fname}
Extension : {ext}
Directory : {directory}
Application : {app}
Description :
"""

#Init the browser
driver = uc.Chrome()

try:
    driver.get("https://chat.openai.com/")
    wait = WebDriverWait(driver, 30)

    # Input zone 
    text_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ProseMirror")))
    print("Print the output")

    with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
        for line in f_in:
            entry = json.loads(line.strip())
            fname = entry["filename"]
            ext = entry["extension"]
            directory = entry["directory"]
            app = entry["application"]

        # Build the prompt
        prompt = prompt_template.format(ext=ext, fname=fname, directory=directory, app=app)

        #Send to chatGPT
        text_input.send_keys(prompt, Keys.ENTER)
        print(f"Prompt sended to {fname}")

        #Wait for the response
        time.sleep(25)

        messages = driver.find_elements(By.CSS_SELECTOR, "div.markdown")
        if messages:
            response = messages[-1].text.strip()
            entry["description"] = response
            f_out.write(json.dumps(entry, ensure_ascii=False) + "\n")
            print(f"response received for {fname}")
        else:
            print(f"No response for {fname}")

        # Little pause before the next sending
        time.sleep(5)

except Exception as e:
    print("Error :", e)

finally:
    driver.quit()
    print("Browser closed!!")