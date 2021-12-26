from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_selection_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    # Esta função retorna uma lista com todas as boxes correspondentes aos hotéis.
    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements_by_css_selector(
            'div[class="_fe1927d9e _0811a1b54 _a8a1be610 _022ee35ec b9c27d6646 fb3c4512b4 fc21746a73"]'
        )

    # Esta função retorna uma lista de listas constituída com os nomes dos hotéis e com os seus respetivos preços.
    def pull_deal_boxes_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element_by_css_selector(
                'div[class="fde444d7ef _c445487e2"]'
            ).get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element_by_css_selector(
                'span[class="fde444d7ef _e885fdc12"]'
            ).get_attribute('innerHTML').strip()

            collection.append(
                [hotel_name, hotel_price]
            )
        
        return collection