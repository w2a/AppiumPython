from Pages.BasePage import BasePage
from Pages.HotelScreen import HotelScreen
from Pages.VillasScreen import VillasScreen


class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoHotels(self):
        self.click("hotels_ID")
        return HotelScreen(self.driver)

    def gotoVillas(self):
        self.click("villas_XPATH")
        return VillasScreen(self.driver)

    def gotoFlights(self):
        pass

    def gotoTrains(self):
        pass
