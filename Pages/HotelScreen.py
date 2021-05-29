from Pages.BasePage import BasePage


class HotelScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def searchHotel(self,city):
        self.click("destination_ACCESSIBILITYID")
        self.type("searchtext_ID",city)
        self.clickIndex("selectlocation_ID",0)
        self.click("searchbtn_XPATH")