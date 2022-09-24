import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_product_view_sku():

	# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
	# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service = service, options = chrome_options)
    
    url = "https://test.qa.studio"
    
    driver.get(url)
    
    hot_items = driver.find_element(by = By.CSS_SELECTOR, value = "#main > div.catalog-toolbar.layout-v3 > div.catalog-toolbar-tabs__content > a.tab-featured")
    hot_items.click()
    
    sofa = driver.find_element(by = By.XPATH, value = "//a[text() = 'ДИВВИНА Журнальный столик']")
    sofa.click()
    
    sku = driver.find_element(by = By.CLASS_NAME, value = "sku")
    assert sku.text == "C0MSSDSUM7"
    
test_product_view_sku()
    