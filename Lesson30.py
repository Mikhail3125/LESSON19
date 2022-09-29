# WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', self.xpath_serial)))
# self.menu_serial_button = self.driver.find_element('xpath', self.xpath_serial)
# self.menu_serial_button.click()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://bank.gov.ua/ua/markets/exchangerates')
# driver.set_window_position(1900,300)
driver.maximize_window()