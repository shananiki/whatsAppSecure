import os
import time
import signal

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class WhatsAppSecure:
    def __init__(self):
        self.class_name = "WhatsAppSecure"
        self.local_appdata_path = os.getenv('LOCALAPPDATA')
        # Specify the path to the ChromeDriver executable
        self.chrome_driver_path = os.getcwd() + '/chromedriver/chromedriver.exe'
        # Create a Service object using the ChromeDriver executable path
        self.service = Service(self.chrome_driver_path)
        # Set cookies
        self.options = webdriver.ChromeOptions()
        self.loadProfile()
        # Create the WebDriver instance by passing the Service object and options
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

        # Receiver of message
        self.target = None
        # Message to send
        self.message = None
        # Number of messages
        self.messageCounter = 1

        self.wait = None

    # This will return "C:\Users\§USER\AppData\Local\"
    def getLocalAppDataPath(self) -> str:
        return self.local_appdata_path

    # This will append your users profile to the driver so you will have all your cookies etc.
    def loadProfile(self) -> None:
        self.options.add_argument("user-data-dir=" + self.getLocalAppDataPath() + "/Google/Chrome/User Data")

    # This will return the name given in "C:\Users\$USER" of current logged in user. $USER will be replaced by your profile folder name!
    def getProfileFolder(self) -> str:
        return os.path.split(os.path.expanduser("~"))[-1]

    # This will open WhatsApp
    def openWhatsApp(self) -> None:
        self.driver.get("https://web.whatsapp.com/")
        self.wait = WebDriverWait(self.driver, 100)

    def setTarget(self, name: str) -> None:
        self.target = name

    def setMessage(self, message: str) -> None:
        self.message = message

    def setMessageCounter(self, messageCounter: int) -> None:
        self.messageCounter = messageCounter

    def getTarget(self) -> str:
        return self.target

    def getMessage(self) -> str:
        return self.message

    def getMessageCounter(self) -> int:
        return self.messageCounter

    def sendMessage(self) -> None:
        contact_path = '//span[contains(@title,' + self.target + ')]'
        contact = self.wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
        contact.click()
        message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        message_box = self.wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
        for x in range(self.messageCounter):
            message_box.send_keys(self.message + Keys.ENTER)
            time.sleep(0.2)


if __name__ == '__main__':
    was = WhatsAppSecure()
    # Target has to be in double quotes!
    was.setTarget('"Phil Gassen Neu"')
    was.setMessage("Omg es hat funktioniert hehe!!")
    was.setMessageCounter(2)
    was.openWhatsApp()
    was.sendMessage()

    # Wait for script to be closed
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.pause()
