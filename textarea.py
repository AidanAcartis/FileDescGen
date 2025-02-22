import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialiser le navigateur
driver = webdriver.Chrome()

try:
    # Ouvrir la page cible
    driver.get("https://chat.openai.com/")
    time.sleep(5)  # Attendre que la page se charge

    try:
        # Sélectionner le champ <textarea>
        textarea = driver.find_element(By.CSS_SELECTOR, "textarea.block.h-10.w-full.resize-none.border-0.bg-transparent.px-0.py-2.text-token-text-primary.placeholder\\:text-token-text-tertiary")
        print("✅ Textarea trouvé !")
    except Exception as e:
        print("❌ Textarea non trouvé :", e)
        driver.quit()
        exit()

    # Vérifier si l'élément est caché et le rendre visible
    driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", textarea)

    # Attendre un peu pour voir si le changement prend effet
    time.sleep(1)

    # Tenter d'envoyer du texte
    textarea.send_keys("Mon texte ici")
    textarea.send_keys(Keys.ENTER)
    print("✅ Texte envoyé !")

except Exception as e:
    print("❌ Erreur générale :", e)

finally:
    driver.quit()  # Toujours fermer le navigateur
