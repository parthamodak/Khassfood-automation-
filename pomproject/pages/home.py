class AllNav():
    def __init__(self, driver):
       self.driver =driver
       #top nav
       self.click_gift_card_XPATH="//a[@href='https://www.khaasfood.com/gift-card/']"
       self.click_howto_order_XPATH = "//span[normalize-space()='How to order']"
       self.click_FAQS_XPATH = "//span[normalize-space()='FAQs']"
       #  #secound nav
       self.click_home_XPATH = "//*[@id='menu-item-405']/a/span"
       self.click_products_XPATH = "/html/body/div[1]/header/div/div[2]/div/div/div[2]/div/div/ul/li[1]/a/span"
       self.click_stores_XPATH = "/html/body/div[1]/header/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span"
       self.click_blog_XPATH = "//*[@id='menu-item-44665']/a/span"
       self.click_download_XPATH = "//*[@id='menu-item-48419']/a/span"
       #  #search
       self.enter_serch_dashbord ="/html/body/div[1]/header/div/div[3]/div/div/div[2]/div/form/input[1]"
       self.enter_serch_button = "/html/body/div[1]/header/div/div[3]/div/div/div[2]/div/form/button"
       #
       #  #suscribe
       self.enter_suscribe_email="//input[@placeholder='Enter your email']"
       self.enter_suscribe_button="//input[@id='es_subscription_form_submit_6320460624184']"


    def top_navbar_check(self):
        self.driver.find_element(self.click_gift_card_XPATH).click()
        self.driver.find_element(self.click_howto_order_XPATH).click()
        self.driver.find_element(self.click_FAQS_XPATH).click()

    def secound_navbar_check(self):
        self.driver.find_element(self.click_home_XPATH).click()
        self.driver.find_element(self.click_products_XPATH).click()
        self.driver.find_element(self.click_stores_XPATH).click()
        self.driver.find_element(self.click_blog_XPATH).click()
        self.driver.find_element(self.click_download_XPATH).click()

    def search_check(self,product):
        self.driver.find_element(self.enter_serch_dashbord).send_keys(product)
    def search_button(self):
        self.driver.find_element(self.enter_serch_button).click()


    def subcribe_check(self, sub):
        self.driver.find_element(self.enter_suscribe_email).send_keys(sub)
        self.driver.find_element(self.enter_suscribe_button).click()








