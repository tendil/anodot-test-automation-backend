import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Make sure the page loads successfully
def test_page_loads(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")
    assert "Convert Temeperature | Degrees Celsius to Fahrenheit | Online Converter" in browser.title

# Check if the temperature conversion function is working properly
def test_conversion(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    user_input = browser.find_element(By.NAME, "userInput")
    user_input.send_keys("100")

    convert_from = browser.find_element(By.NAME, "convertFrom")
    convert_from.send_keys("degree Celsius")

    convert_to = browser.find_element(By.NAME, "convertTo")
    convert_to.send_keys("degree Fahrenheit")

    convert_button = browser.find_element(By.ID, "convertBtn")
    convert_button.click()

    answer = browser.find_element(By.ID, "answer")
    assert answer.text == "100 degree Celsius = 212 degree Fahrenheit"

# Make sure that the temperature input field does not accept text values.
def test_conversion_error(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    user_input = browser.find_element(By.NAME, "userInput")
    user_input.send_keys("abcd")

    convert_from = browser.find_element(By.NAME, "convertFrom")
    convert_from.send_keys("degree Celsius")

    convert_to = browser.find_element(By.NAME, "convertTo")
    convert_to.send_keys("degree Fahrenheit")

    convert_button = browser.find_element(By.ID, "convertBtn")
    convert_button.click()

    answer = browser.find_element(By.ID, "answer")
    assert answer.text == "0 degree Celsius = 32 degree Fahrenheit"

# Make sure the temperature input field is present on the page
def test_temperature_field_present(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    temperature_field = browser.find_element(By.NAME, "userInput")
    assert temperature_field.is_displayed()


# Make sure the temperature input field only accepts numeric values
def test_temperature_entry_field_accepts_only_numeric_values(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    temp_entry_field = browser.find_element(By.NAME, "userInput")
    temp_entry_field.send_keys("25")

    assert temp_entry_field.get_attribute("value").isnumeric()
    temp_entry_field.clear()

    temp_entry_field.send_keys("not a number")
    assert not temp_entry_field.get_attribute("value").isnumeric()


# Make sure that the temperature input field can take negative values.
def test_negative_temperature_entry(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    user_input = browser.find_element(By.NAME, "userInput")
    user_input.send_keys("-10")

    convert_from = browser.find_element(By.NAME, "convertFrom")
    convert_from.send_keys("degree Celsius")

    convert_to = browser.find_element(By.NAME, "convertTo")
    convert_to.send_keys("degree Fahrenheit")

    convert_button = browser.find_element(By.ID, "convertBtn")
    convert_button.click()

    answer = browser.find_element(By.ID, "answer")
    assert answer.text == "-10 degree Celsius = 14 degree Fahrenheit"

# Make sure the temperature input field has a default value of blank.
def test_temperature_entry_field_default_value(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    temperature_input = browser.find_element(By.NAME, "userInput")
    assert temperature_input.get_attribute("value") == ""

# Make sure the page has a drop-down list of "from" units.
def test_temperature_unit_dropdown_present_convertfrom(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    dropdown = browser.find_element(By.NAME, "convertFrom")
    assert dropdown.is_displayed()

# Make sure the page has a drop-down list of units of measure "before"
def test_temperature_unit_dropdown_present_convertto(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    dropdown = browser.find_element(By.NAME, "convertTo")
    assert dropdown.is_displayed()

# Verify that pressing the "convert" button returns the converted temperature value.
def test_convert_button(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    temperature_input = browser.find_element(By.NAME, "userInput")
    temperature_input.send_keys("25")

    from_unit_dropdown = browser.find_element(By.NAME, "convertFrom")
    from_unit_dropdown.send_keys("degree Celsius")

    to_unit_dropdown = browser.find_element(By.NAME, "convertTo")
    to_unit_dropdown.send_keys("degree Fahrenheit")

    convert_button = browser.find_element(By.ID, "convertBtn")
    convert_button.click()

    converted_value = browser.find_element(By.ID, "answer")
    assert converted_value.text == "25 degree Celsius = 77 degree Fahrenheit"

# Verify that when converting a negative temperature value, the correct converted value is displayed.
def test_negative_temperature_conversion(browser):
    browser.get("https://www.theonlineconverter.co.uk/temperature-converter/")

    temperature_input = browser.find_element(By.NAME, "userInput")
    temperature_input.clear()
    temperature_input.send_keys("-10")

    from_unit_dropdown = browser.find_element(By.NAME, "convertFrom")
    from_unit_dropdown.click()
    from_unit_option = from_unit_dropdown.find_element(By.XPATH, "//option[@value='0']")
    from_unit_option.click()

    to_unit_dropdown = browser.find_element(By.NAME, "convertTo")
    to_unit_dropdown.click()
    to_unit_option = to_unit_dropdown.find_element(By.XPATH, "//option[@value='1']")
    to_unit_option.click()

    convert_button = browser.find_element(By.ID, "convertBtn")
    convert_button.click()

    converted_value = browser.find_element(By.ID, "answer")
    assert converted_value.text == "-10 degree Fahrenheit = -23.3333333 degree Celsius"
