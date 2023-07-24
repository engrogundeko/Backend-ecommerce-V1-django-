import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# def test_create_admin_user(create_admin_user):
#     assert create_admin_user.__str__ == "user"

@pytest.mark.selenium
def test_admin_login(live_server, django_db_setup, chrome_browser_instance):
    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url, "/admin/login")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    user_name.send_keys("admin")
    user_password.send_keys("password")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
