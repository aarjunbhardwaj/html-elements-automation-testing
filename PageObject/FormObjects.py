from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time



class FormElements:
    def __init__(self,Driver):
        self.driver = Driver
        self.formcard_xpath = '//h5[text()="Forms"]/ancestor::div[contains(@class,"top-card")]'
        self.form_list_item_xpath = '//span[text()="Practice Form"]//parent::li'
        self.fname_box_id = 'firstName'
        self.last_name_id = 'lastName'
        self.email_box_id = 'userEmail'
        self.phone_number_id = 'userNumber'
        self.male_rd_btn_css_selector = 'label[for="gender-radio-1"]'
        self.dob_input_id = 'dateOfBirthInput'
        self.date_css_selector = 'div.react-datepicker__day'
        self.month_classname = 'react-datepicker__month-select'
        self.year_section_classname ='react-datepicker__year-select'
        self.years_option_css_selector = 'select.react-datepicker__year-select option'
        self.previous_month_button_class_name = 'react-datepicker__month-container'
        self.subject_xpath = "//input[@id='subjectsInput']"
        self.sports_checkbox_css_selector = 'label[for="hobbies-checkbox-1"]'
        self.reading_checkbox_css_selector = 'label[for="hobbies-checkbox-2"]'
        self.music_checkbox_css_selector = 'label[for="hobbies-checkbox-3"]'
        self.upload_pic_id = 'uploadPicture'
        self.current_address_id = 'currentAddress'
        self.combbox_states_xpath = '//div[text()="Select State"]'
        self.city_div_xpath = '//div[text()="Select City"]'
        self.submit_btn_id = 'submit'

    def click_to_form_card(self):
        formcard = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.formcard_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();",formcard)
        ActionChains(self.driver).move_to_element(formcard).click().perform()

    def click_to_li_items_form(self):
        formcard_li = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.form_list_item_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();",formcard_li)
        ActionChains(self.driver).move_to_element(formcard_li).click().perform()
    
    def set_first_name(self,firstname):
        fname = self.driver.find_element(By.ID,self.fname_box_id)
        fname.click()
        fname.send_keys(firstname)

    def set_last_name(self,lastname):
        lname = self.driver.find_element(By.ID,self.last_name_id)
        lname.click()
        lname.send_keys(lastname)

    def set_email_id(self,email):
        email_id = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.ID,self.email_box_id))
        )
        email_id.send_keys(email)

    def set_phone_number(self,phonenumber):
        ph_number = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.ID,self.phone_number_id))

        )
        self.driver.execute_script("arguments[0].scrollIntoView()",ph_number)    
        ph_number.send_keys(phonenumber)

    def click_male_radio(self):
        male_rd_elem = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,self.male_rd_btn_css_selector))
        )
        male_rd_elem.click()
    def click_dob_field(self):
        dob_elem = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.ID,self.dob_input_id))
        )
        dob_elem.click()
    def set_date(self,Date):
        pick_date = self.driver.find_elements(By.CSS_SELECTOR,self.date_css_selector)
        for date in pick_date:
            if date.text == Date and print(f"date is enabled and displayed {date.is_enabled() and date.is_displayed()}"):
                actions = ActionChains(self.driver)
                actions.move_to_element(date).click().perform()
                break
        time.sleep(2)

    def set_month(self,month):
        month_option = self.driver.find_element(By.CLASS_NAME,self.month_classname)
        select_month = Select(month_option)
        select_month.select_by_visible_text(month)

    def click_year_field(self):
        year_option = self.driver.find_element(By.CLASS_NAME,self.year_section_classname)
        year_option.click()

    def set_year(self,Year):
        year_options = self.driver.find_elements(By.CSS_SELECTOR,self.years_option_css_selector)
        for year in year_options:
            if year.text == Year:
                self.driver.execute_script("arguments[0].scrollIntoView();",year)
                year.click()
                break
         # Click outside the dropdown to close it
        self.driver.find_element(By.TAG_NAME, 'body').click()
    
    def set_subjects(self,subjects):
        subject_box = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, self.subject_xpath))
    )
    
        actions = ActionChains(self.driver)
        actions.move_to_element(subject_box).click().perform()
        
        time.sleep(0.5)  # Wait 0.5 seconds
        
        subject_box.send_keys(subjects)

    def set_hobby_checkboxes(self):
        hobbies = [
        self.sports_checkbox_css_selector,
        self.reading_checkbox_css_selector,
        self.music_checkbox_css_selector
    ]
    
        for css_selector in hobbies:
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
            )
            checkbox.click()
        
    def upload_picture(self,path):
        upload_pic = self.driver.find_element(By.ID,self.upload_pic_id)
        upload_pic.send_keys(path)

    def set_address(self,c_address):
        address = self.driver.find_element(By.ID,self.current_address_id)
        address.click()
        address.send_keys(c_address)

    def set_combox_state(self):
        combo_box = self.driver.find_element(By.XPATH,self.combbox_states_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",combo_box)
        combo_box.click()
        for i in range(0,2):
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()

    def set_city(self):
        city_div = self.driver.find_element(By.XPATH,self.city_div_xpath)
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(city_div)
        )
        city_div.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def form_submit_btn(self):
        self.driver.find_element(By.ID,self.submit_btn_id).click()

