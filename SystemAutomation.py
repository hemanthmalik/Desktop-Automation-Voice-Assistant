from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import smtplib


class AutomateBrowser:
    def __init__(self, to=None, content=None):
        self.to = to
        self.content = content


    def facebookLogin(self):
        options = Options()
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        driver = webdriver.Chrome(r"C:\Users\HemantMalik\Downloads\chromedriver_win32/chromedriver")
        driver.get("https://facebook.com/")

        emailButton = driver.find_element_by_name("email")
        passBox = driver.find_element_by_name("pass")

        emailButton.send_keys("youremail@gmail.com")
        passBox.send_keys("1234")
        # sendButton = driver.find_element_by_id('_35EW6').send_keys(Keys.RETURN)
        passBox.send_keys(Keys.RETURN)
        # else:
        #     speak("Sir, Please try again with valid authentication code.")

    def sendEmail(self):
        emails = {"rinku": "Rs06798@gmail.com", "anshu": "anskmr831@gmail.com", "rohitash": "rksharma8aa@gmail.com",
                  "hemant": "hemantmalik121@gmail.com", "hemanth": "hemantmalik121@gmail.com"}
        print(self.to, self.content)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'yourpassword')
        server.sendmail('youremail@gmail.com', emails[self.to], self.content)
        server.close()

    def whatsappMess(self):
        # options = Options()
        # options.add_argument('start-maximized')
        # options.add_argument('disable-infobars')
        driver = webdriver.Chrome(r"C:\Users\HemantMalik\Downloads\chromedriver_win32/chromedriver")
        driver.get("https://web.whatsapp.com/")

        wait = WebDriverWait(driver, 6000)

        name = self.to

        message = self.content

        print(name, message)

        x_args = '//span[@title="'+name+'"]'

        try:
            target = wait.until(EC.presence_of_element_located((By.XPATH, x_args)))

            target.click()

            inputBox = driver.find_element_by_class_name('_1Plpp')
            inputBox.send_keys(message)
            driver.find_element_by_class_name('_35EW6').send_keys(Keys.RETURN)

        except:
            print("there is a problem")


    def googlesearch(self):
        driver = webdriver.Chrome(r"C:\Users\HemantMalik\Downloads\chromedriver_win32/chromedriver")

        driver.get("https://www.google.com/")

        x_args = "//input[@title='Search']"

        elem = driver.find_element_by_xpath(x_args)

        elem.send_keys(self.content)

        elem.send_keys(Keys.RETURN)

    def youtubesearch(self):
        driver = webdriver.Chrome(r"C:\Users\HemantMalik\Downloads\chromedriver_win32/chromedriver")

        driver.get("https://www.youtube.com/")

        elem = driver.find_element_by_id("search")

        elem.send_keys(self.content)

        elem.send_keys(Keys.RETURN)


