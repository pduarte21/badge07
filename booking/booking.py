import booking.constants as const
from selenium import webdriver
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    # Esta função serve para abrir a página Web pretendida e para aceitar os cookies.
    def land_first_page(self):
        self.get(const.BASE_URL)
        accept_cookies = self.find_element_by_id("onetrust-accept-btn-handler")
        accept_cookies.click()

    # Esta função serve para automatizarmos o processo de escolha da linguagem do website.
    def change_language(self, language=None):
        language_element = self.find_element_by_css_selector(
            'button[data-modal-id="language-selection"]'
        )
        language_element.click()

        selected_language_element = self.find_element_by_css_selector(
            f'a[data-lang="{language}"]'
        )
        selected_language_element.click

    # Esta função serve para automatizarmos o processo de escolha da moeda utilizada no website.
    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Escolha a sua moeda"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    # Esta função serve para automatizarmos o processo de escolha do nosso destino.
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

    # Esta função serve para automatizarmos o processo de escolha da data.
    def select_date(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    # Esta função serve para automatizarmos o processo de escolha do número de adultos e de quartos.
    def select_passengers(self, adults, rooms):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        decrease_adults_button = self.find_element_by_css_selector(
            'button[aria-label="Diminuir o número de Adultos"]'
        )
        increase_adults_button = self.find_element_by_css_selector(
            'button[aria-label="Aumentar o número de Adultos"]'
        )
        adults_value_element = self.find_element_by_id('group_adults')

        while True:
            if int(adults_value_element.get_attribute('value')) == adults:
                break
            else:
                if int(adults_value_element.get_attribute('value')) < adults:
                    increase_adults_button.click()
                else:
                    decrease_adults_button.click()

        decrease_rooms_button = self.find_element_by_css_selector(
            'button[aria-label="Diminuir o número de Quartos"]'
        )
        increase_rooms_button = self.find_element_by_css_selector(
            'button[aria-label="Aumentar o número de Quartos"]'
        )
        rooms_value_element = self.find_element_by_id('no_rooms')

        while True:
            if int(rooms_value_element.get_attribute('value')) == rooms:
                break
            else:
                if int(rooms_value_element.get_attribute('value')) < rooms:
                    increase_rooms_button.click()
                else:
                    decrease_rooms_button.click()
    
    # Esta função serve para automatizarmos o clicar do botão Pesquisar.
    def search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    # Esta função serve para automatizarmos a visualização dos hotéis com o preço mais baixo em primeiro lugar.
    def lowest_price_first(self):
        lowest_price_filter = self.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        lowest_price_filter.click()

    # Esta função serve para automatizarmos a filtragem da classificação dos hotéis.
    def apply_star_rating(self, rating):
        star_filtration_box = self.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')

        for star_element in star_child_elements:
            if str(star_element.get_attribute('innerHTML')).strip() == f'{rating} estrelas':
                star_element.click()

    # Esta função serve para visualizarmos os resultados.
    def report_results(self):
        hotel_boxes = self.find_element_by_id(
            'search_results_table'
        )
        
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=['Hotel Name', 'Hotel Price']
        )
        table.add_rows(report.pull_deal_boxes_attributes())
        print(table)