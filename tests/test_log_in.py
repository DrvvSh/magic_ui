# Invalid username and password
def test_invalid_log_in(log_in_page):
    log_in_page.open_page()
    log_in_page.fill_in_the_form('username', 'password')
    log_in_page.check_error_message_text_is('Invalid username or password')
