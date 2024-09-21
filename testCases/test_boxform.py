from PageObject.TextBoxObject import Text_Elements

class Test_TextBox:

    def test_textbox_tc001(self,setup):
        textbox_page = Text_Elements(setup)
        textbox_page.click_to_elements()
        textbox_page.click_to_textbox()
        textbox_page.set_username("Jai Shree Shyam Ji")
        textbox_page.set_emailid("jaishreeramji@bajrangbali.com")
        textbox_page.set_current_address("12345 Oakwood Drive,Apt 101,Riverview, FL 3357,United States")
        textbox_page.set_permanent_address("47A Kensington Road, London, NW4 2JD,United Kingdom")
        textbox_page.submit_btn_click()
        # Assertions
        assert textbox_page.get_username() == "Jai Shree Shyam Ji"
        assert textbox_page.get_emailid() == "jaishreeramji@bajrangbali.com"
        assert textbox_page.get_current_address() == "12345 Oakwood Drive,Apt 101,Riverview, FL 3357,United States"
        assert textbox_page.get_permanent_address() == "47A Kensington Road, London, NW4 2JD,United Kingdom"