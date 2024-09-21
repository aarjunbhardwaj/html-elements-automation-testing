from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Text_Elements:

    def __init__(self,Driver):
        self.driver = Driver
        self.elements_xpath = "(//div[@class='avatar mx-auto white'])[1]"
        self.text_box_xpath = "//div[@class='element-list collapse show']//li[@id='item-0']"
        self.username_id = 'userName'
        self.email_id = 'userEmail'
        self.cAddress_id = 'currentAddress'
        self.pAddress_id = 'permanentAddress'
        self.submit_btn_class = 'btn btn-primary'

    def click_to_elements(self):
        e = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,self.elements_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", e)
        ActionChains(self.driver).move_to_element(e).click().perform()
    
    def click_to_textbox(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.text_box_xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            ActionChains(self.driver).move_to_element(element).click().perform()
        except TimeoutException:
            print("Element not clickable after waiting")
        except NoSuchElementException:
            print("Element not found") 

    def set_username(self,username):
        self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def set_emailid(self,email):
        self.driver.find_element(By.ID,self.email_id).send_keys(email)

    def set_current_address(self,currentAddress):
        self.driver.find_element(By.ID,self.cAddress_id).send_keys(currentAddress)

    def set_permanent_address(self,permanetAddress):
        self.driver.find_element(By.ID,self.pAddress_id).send_keys(permanetAddress)

    def submit_btn_click(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, self.submit_btn_class))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            ActionChains(self.driver).move_to_element(button).click().perform()
        except TimeoutException:
            print("Submit button not clickable after waiting")
        except NoSuchElementException:
            print("Submit button not found")

    def get_username(self):
        return self.driver.find_element(By.ID, self.username_id).get_attribute("value")

    def get_emailid(self):
        return self.driver.find_element(By.ID, self.email_id).get_attribute("value")

    def get_current_address(self):
        return self.driver.find_element(By.ID, self.cAddress_id).get_attribute("value")

    def get_permanent_address(self):
        return self.driver.find_element(By.ID, self.pAddress_id).get_attribute("value")
