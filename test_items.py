from selenium.common.exceptions import NoSuchElementException


def check_element_presence(browser, elem):
    try:
        return bool(browser.find_element_by_css_selector(elem))
    except NoSuchElementException:
        return False


def test_add_cart(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert check_element_presence(browser, ".btn-add-to-baske5t"), "Кнопка не найдена"
