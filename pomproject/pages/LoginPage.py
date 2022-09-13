class LoginPage():
    def __init__(self, driver):
       self.driver =driver
       self.click_login_XPATH="/html/body/div[1]/header/div/div[3]/div/div/div[3]/div[2]/a"
       self.username_email_XPATH="//input[@placeholder='Email Address']"
       self.password_password_XPATH="//input[@placeholder='Password']"
       self.login_button_XPATH="//button[@class='btn btn-color-primary btn-shape-semi-round btn-size-default btn-full-width'][normalize-space()='Login']"

    def login_regerter(self):
       self.driver.find_element(self.click_login_XPATH).click()


    def enter_usename(self,username):    #create function and pass arguments

        self.driver.find_element(self.username_email_XPATH).clear()
        self.driver.find_element(self.username_email_XPATH).send_key(username)

    def enter_password(self, password):

        self.driver.find_element(self.password_password_XPATH).clear()
        self.driver.find_element(self.password_password_XPATH).send_keys(password)

    def login_enter(self):

        self.driver.find_element(self.login_button_XPATH).click()


