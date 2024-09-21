from PageObject.FormObjects import FormElements

class Test_FillForm:
    def test_form_tc001(self,setup):
        form_page = FormElements(setup)
        form_page.click_to_form_card()
        form_page.click_to_li_items_form()
        form_page.set_first_name("arjun")
        form_page.set_last_name("Bhardwaj")
        form_page.set_email_id("aarjunbhardwaj@email.com")
        form_page.set_phone_number("8780729753")
        form_page.click_male_radio()
        form_page.click_dob_field()
        form_page.set_date("22")
        form_page.set_month("October")
        form_page.set_year("1994")
        form_page.set_subjects("Python,Automation")
        form_page.set_hobby_checkboxes()
        form_page.upload_picture("C://Users/Arjun/Downloads/logo.png")
        form_page.set_address("12345 Oakwood Drive,Apt 304 Raleigh, NC 27607 USA")
        form_page.set_combox_state()
        form_page.set_city()
        form_page.form_submit_btn()
        
