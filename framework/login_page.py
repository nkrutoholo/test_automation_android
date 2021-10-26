from selenium.webdriver.common.by import By

from .page import Page


class LoginPage(Page):
    LOGIN = (By.ID, 'com.ajaxsystems:id/login')
    FRGT_PSSWD = (By.ID, 'com.ajaxsystems:id/forgot')
    FORGOT_WARNING = (By.ID, 'com.ajaxsystems:id/title')
    FORGOT_MESSAGE_FIELD = (By.ID, 'com.ajaxsystems:id/message')
    CHANGE_PASSWORD = (By.ID, 'com.ajaxsystems:id/nextButton')
    FORGOT_TITLE = (By.ID, 'com.ajaxsystems:id/forgotTitle')
    FORGOT_CANCLE = (By.ID, 'com.ajaxsystems:id/cancel')
    FORGOT_OK = (By.ID, 'com.ajaxsystems:id/ok')
    PASSWORD_FIELD = (By.ID, 'com.ajaxsystems:id/password')
    LOG_IN_BUTTON = (By.ID, 'com.ajaxsystems:id/next')
    SUCCESS_LOGIN_TEXT = (By.ID, 'com.ajaxsystems:id/addFirstHub')
    LOADING_WINDOW = (By.ID, 'com.ajaxsystems:id/loading')
    LOADING_TEXT = (By.ID, 'ajaxsystems:id/content_text')
    CHK_LATER_BUTTON = (By.ID, 'ajaxsystems:id/cancel_button')
    LOGIN_UNFILL_MSG = (By.ID, 'com.ajaxsystems:id/snackbar_text')

    LOADING_CONTEXT = 'Android OS can block push notifications.\n/' \
                      'Please check the settings to receive instant alerts.'
    FORGOT_MESSAGE_TEXT = 'You log out this account at all devices except for this one'
    FORGOT_TITLE_TEXT = 'Enter your phone number or email and press "Next".'

    def tap_log_in(self):
        self.click_element(*self.LOGIN)

    def tap_forgot_password(self):
        self.click_element(*self.FRGT_PSSWD)
        self.driver.implicitly_wait(5)
        text_wrng = self.find_element(*self.FORGOT_WARNING).text
        forgot_msg = self.find_element(*self.FORGOT_MESSAGE_FIELD).text

        assert text_wrng == 'Warning', f'Expected "{text_wrng}" text in Warning field'
        assert forgot_msg == self.FORGOT_MESSAGE_TEXT, f'Expected "{text_wrng}" text in {self.FORGOT_MESSAGE_TEXT}'

    def tap_change_password(self):
        self.click_element(*self.CHANGE_PASSWORD)
        text = self.find_element(*self.FORGOT_TITLE).text
        assert text == self.FORGOT_TITLE_TEXT, f'Expected "{text}" text in {self.FORGOT_TITLE_TEXT}'

    def tap_ok_in_forgot(self):
        self.click_element(*self.FORGOT_OK)
        text = self.find_element(*self.FORGOT_TITLE).text
        assert text == self.FORGOT_TITLE_TEXT, f'Expected "{text}" text in {self.FORGOT_TITLE_TEXT}'

    def tap_cancel_in_forgot(self):
        self.click_element(*self.FORGOT_CANCLE)

    def input_login(self, email=str, password=str):
        self.input(email, *self.LOGIN)
        self.input(password, *self.PASSWORD_FIELD)
        self.click_element(*self.LOG_IN_BUTTON)

    def invalid_login_result(self):
        self.input_login('', '')
        self.click_element(*self.LOGIN)

        assert self.find_element(*self.LOGIN_UNFILL_MSG).is_displayed()

    def success_login_result(self, text=str):
        self.driver.implicitly_wait(5)
        app_text = self.find_element(*self.SUCCESS_LOGIN_TEXT).text

        assert text in app_text, f'Expected "{text}" text in {app_text}'
