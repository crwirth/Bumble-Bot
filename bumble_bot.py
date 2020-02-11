from selenium import webdriver
from secrets import username, password
from time import sleep

class BumbleBot():

    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://bumble.com') 

        sleep(2)

        sign_in = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a') 
        sign_in.click()

        sleep(2)

        fb_sign_in = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div')
        fb_sign_in.click()

        #switches to login popup for Facebook
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input.send_keys(username)

        password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')  
        password_input.send_keys(password)

        fb_login_button = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_login_button.click()

        self.driver.switch_to_window(base_window)
    
    def swipe_right(self):
        like_button = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
        like_button.click()

    def swipe_left(self):
        dislike_button = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div')
        dislike_button.click()
    
    def autoSwipe(self):
        while True:
            sleep(2)
            self.swipe_right()
    
    def close_match(self):
        continue_bumbling = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div/div[2]/div/span')
        continue_bumbling.click()
    
    def close_popup(self):
        close_popup_window = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div/div[2]/div/div[2]')
        close_popup_window.click()

        
bot = BumbleBot()
bot.login()
