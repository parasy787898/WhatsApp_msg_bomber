from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import path

class Whatsapp :
    def __init__(self):
        self.driver = webdriver.Chrome(path.join(path.dirname(__file__), "c.exe"))
        self.driver.get('https://web.whatsapp.com/')
        sleep(2)

    def search_and_send(self):
        count = int(input("No Of Messages : "))
        self.name = input("Enter the username : ")
        self.message ="These are automated messages "
        sleep(2)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').send_keys(self.name)
        sleep(1)
        
        self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(self.name)).click()
        sleep(1)

        self.no=1

        for i in range(count):
            msg_box = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            msg_box.send_keys(self.message,+self.no)

            button = self.driver.find_element_by_class_name('_2Ujuu')
            button.click()
            
            self.no+=1
    def close_browser(self):
        sleep(5)
        self.driver.close()

bot = Whatsapp()
bot.search_and_send()
#bot.close_browser()
