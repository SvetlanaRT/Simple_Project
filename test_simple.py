from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_simple():
    options=Options()
    options.set_capability("acceptInsecureSerts",True)
    driver = webdriver.Chrome(executable_path="/home/svetlana.kalchenko/PycharmProjects/BEautomat/chromedriver",chrome_options=options)
    driver.get("https://www.google.com/")
    assert "google" in driver.current_url