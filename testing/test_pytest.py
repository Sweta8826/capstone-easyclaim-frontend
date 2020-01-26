from selenium import webdriver
#driver.implicitly_wait(10)   

def test_login():
    global driver
    driver=webdriver.Chrome("C:/Users/VigneshSmile/capstone-easyclaim-frontend/testing/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get('http://35.223.71.21/')
    driver.maximize_window()
    driver.find_element_by_id("username").send_keys('vishnu')
    driver.find_element_by_id('pwd').send_keys('vishnu@123')
    driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/form/button').click()
    print(driver.title)
def test_title_check():
    assert (driver.title == 'Easy Claim'), 'title not matched'
    driver.close()
    
