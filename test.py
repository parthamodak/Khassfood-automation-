

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.khaasfood.com/")
driver.maximize_window()
#-----secound navbar-----#
# driver.find_element(By.XPATH,"//*[@id='menu-item-405']/a/span").click()
# driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[2]/div/div/div[2]/div/div/ul/li[1]/a/span").click()
# driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span").click()
# driver.find_element(By.XPATH,"//*[@id='menu-item-44665']/a/span").click()
# driver.find_element(By.XPATH,"//*[@id='menu-item-48419']/a/span").click()
# driver.get("https://www.khaasfood.com/")
#------------secound navbar-----------#


#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[3]/div[2]/a").click()
#driver.find_element(By.XPATH,"//input[@placeholder='Email Address']").send_keys("mmodak642@gmail.com")
#driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("53pMM80@")
#driver.find_element(By.XPATH,"//button[@class='btn btn-color-primary btn-shape-semi-round btn-size-default btn-full-width'][normalize-space()='Login']").click()

#---chat box---#
# driver.find_element(By.XPATH,".//*[@id='webchat']/div[2]/div").click()
# iframe=driver.find_element(By.XPATH,"//*[@id='webchat']/div[2]/iframe")
# driver.switch_to.frame(iframe)
# driver.find_element(By.XPATH,"//input[@placeholder='Name*']").send_keys("ParhaModak")
# driver.find_element(By.XPATH,"//input[@placeholder='Phone Number*']").send_keys("01521314162")
# driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/input[3]").send_keys("mm.partho@gmail.com")
# driver.find_element(By.XPATH,"//input[@placeholder='Location']").send_keys("sherpur")
# driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/textarea").send_keys("this is a test case")
# driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/button/span").click()


#------chat box end-------#


#-------add to card------#
#card button
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[3]/div[3]/a").click()







#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[2]/div/form/input[1]").send_keys("product")
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[2]/div/form/button").click()
#driver.find_element(By.LINK_TEXT,"Products").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,Stores).click()



#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[2]/div/form/input[1]").send_keys("product")
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[2]/div/form/button").click()
#driver.find_element(By.LINK_TEXT,"Products").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,Stores).click()


#=-----------login-----------#
# driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[3]/div[2]/a").click()
# driver.find_element(By.XPATH,"//*[@id='username']").send_keys("mmodak642@gmail.com")
# driver.find_element(By.XPATH,"//*[@id='password']").send_keys("53pMM80@")
# driver.find_element(By.XPATH,"/html/body/div[9]/form/p[4]/button").click()

#-----------login end______________#


#______________top nav-----------#
# driver.find_element(By.XPATH,"//a[@href='https://www.khaasfood.com/gift-card/']").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='How to order']").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='FAQs']").click()
#end______top nav_____________#


# for----------------------- subcribe------------------- dr
driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']").send_keys("mm.partho@gmail.com")
driver.find_element(By.XPATH,"//input[@id='es_subscription_form_submit_6320460624184']").click()