import os

class WhatsAppSecure:


    def __init__(self):
        self.class_name = "WhatsAppSecure"
        self.local_appdata_path = os.getenv('LOCALAPPDATA')

    def getLocalAppDataPath(self):
        return self.local_appdata_path

    def load

if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time

    was = WhatsAppSecure()

    # Get cookies of your Google Chrome Profile
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=" + was.getLocalAppDataPath() + "/Google/Chrome/User Data")
    driver = webdriver.Chrome('/chromedriver/chromedriver.exe', chrome_options=options)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 100)

    target = '"Your Target"'
    message = "Your Message"
    number_of_times = 10  # No. of times to send a message

    contact_path = '//span[contains(@title,' + target + ')]'
    contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
    contact.click()
    message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
    for x in range(number_of_times):
        message_box.send_keys(message + Keys.ENTER)
        time.sleep(0.2)