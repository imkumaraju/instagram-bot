def __init__(self,username,password):
    self.username=username
    self.password=password
    self.driver=webdriver.Firefox()

def closrBrowser(self):
    self.driver.close()

def login(self):
    driver=self.driver
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(10)
    user_name_element=driver.find_element_by_xpath("//input[@name='username']")
    user_name_element.clear()
    user_name_element.send_keys(self.username)

    password_element = driver.find_element_by_xpath("//input[@name='password']")
    password_element.clear()
    password_element.send_keys(self.password)
    password_element.send_keys(Keys.RETURN)
    time.sleep(25)
    cancel_notification_button = driver.find_element_by_class_name('HoLwm')
    cancel_notification_button.send_keys(Keys.RETURN)
    time.sleep(2)

def like_photo(self,hashtag):
    driver = self.driver
    driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
    time.sleep(10)
    for i in range(1,3):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)
    #searshing for picture link
    hrefs = driver.find_elements_by_tag_name('a')
    images_links = []
    for item in hrefs:
        href = item.get_attribute('href')
        if "/p/" not in href:
            continue
        #print(href)
        images_links.append(href)

    for images_link in images_links:
        driver.get(images_link)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        try:
            driver.find_element_by_class_name("coreSpriteHeartOpen").click()
            time.sleep(10)
        except Exception as e:
            time.sleep(2)
bot=InstagramBot("username","password")
bot.login()
bot.like_photo('india')
`
