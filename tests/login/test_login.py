import logging

from framework import LoginPage


def test_user_login(user_login_fixture):
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    logging.info("Start user login test")
    login_page = user_login_fixture.create_page(LoginPage)
    login_page.tap_log_in()
    logging.info("Input login and password invalid test")
    login_page.invalid_login_result()
    logging.info("Check forgot password test")
    login_page.tap_forgot_password()
    login_page.tap_change_password()
    login_page.tap_ok_in_forgot()
    login_page.tap_cancel_in_forgot()
    logging.info("Invalid login test")
    login_page.invalid_login_result()
    logging.info("Valid login test")
    login_page.input_login('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    login_page.success_login_result('Add ypur first hub to start managing the security system')
