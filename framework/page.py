class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        el = self.find_element(*locator)
        el.click()

    def input(self, text, *locator):
        el = self.find_element(*locator)
        el.clear()
        el.send_keys(text)
