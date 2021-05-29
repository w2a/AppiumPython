import pytest

from Pages.HomeScreen import HomeScreen
from Pages.HotelScreen import HotelScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_SearchHotel(BaseTest):

    @pytest.mark.parametrize("city", dataProvider.get_data("SearchTest"))
    def test_searchHotel(self,city):
        home = HomeScreen(self.driver)
        home.gotoHotels().searchHotel(city)
