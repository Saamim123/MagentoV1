import os
from datetime import datetime
from selenium import webdriver
import allure
import pytest
from pageobjects.CustomerLoginPage import CustomerLoginPage
from pageobjects.Luma_Homepage import Luma_homepage
from pageobjects.Myaccountpage import Myaccountpage
from utilities.readproperties import Readconfig
from utilities.customlogger import CustomLogger
from pageobjects.UserHomepage import UserHomepage

# ---------------- FIXTURES ---------------- #
@pytest.fixture()
def setup(browser, request):
    if browser == "edge":
        driver = webdriver.Edge()
        driver.maximize_window()
        request.cls.driver = driver
        print("------launching Edge-------")

    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        print("------launching Firefox-------")

    else:
        # --- Chrome Options to disable "Change your password" popup ---
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--incognito")  # optional: clean session
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        print("------launching Chrome-------")
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ---------------- HOOKS ---------------- #
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to check if a test has failed and take a screenshot automatically.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")
        if driver:
            save_screenshot(driver, item.name)


# ---------------- UTIL FUNCTIONS ---------------- #
def save_screenshot(driver, test_name):
    """
    Save screenshot to Screenshots folder with timestamp.
    """
    screenshots_folder = os.path.join(os.getcwd(), "Screenshots")
    os.makedirs(screenshots_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(screenshots_folder, f"{test_name}_{timestamp}.png")

    driver.save_screenshot(file_path)
    print(f"\n[SCREENSHOT SAVED] {file_path}")


# ---------------- HTML REPORT CONFIG ---------------- #
def pytest_configure(config):
    # Create reports directory if it doesn't exist
    reports_dir = os.path.join(os.getcwd(), "Reports")
    os.makedirs(reports_dir, exist_ok=True)

    # Create a timestamped HTML report filename
    report_file = os.path.join(reports_dir, f"report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html")

    # Set HTML report path
    config.option.htmlpath = report_file
    config.option.self_contained_html = True


# Login fixture

@pytest.fixture()
def login_fixture(setup):
    driver = setup
    logger = CustomLogger().get_logger()
    user_login_url = Readconfig.get_user_login_url()
    email = Readconfig.get_user_login_email()
    password = Readconfig.get_user_login_password()
    expected_msg = Readconfig.get_user_login_cnf_msg()

    logger.info("-------Starting user Login Test----------")
    driver.get(user_login_url)
    driver.maximize_window()
    hp = UserHomepage(driver)
    hp.click_login()

    cxlp = CustomerLoginPage(driver)
    cxlp.set_useremail(email)
    cxlp.set_password(password)
    logger.info("------logging into user account-----")
    cxlp.click_login()
    lh = Luma_homepage(driver)

    myacp = Myaccountpage(driver)
    lh.is_logo_present()
    """act_msg = myacp.capture_myaccount_cnf()

    # ✅ Validation inside try block
    if not act_msg or act_msg != expected_msg:
        logger.error(f"Login failed! Expected '{expected_msg}' but got '{act_msg}'")
        pytest.fail(f"Stopping tests: Login fixture failed. Reason: Expected '{expected_msg}' but got '{act_msg}'")

except Exception as e:
    logger.error(f"Exception occurred during login: {str(e)}")
    pytest.fail(f"Stopping tests: Login fixture failed due to exception: {str(e)}")

# ✅ If login successful → continue tests"""


    yield driver













