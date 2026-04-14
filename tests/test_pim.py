from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from utils.logger import get_logger
from utils.test_data import generate_employee_name

import random

def test_add_employee(page, config):
    login_page = LoginPage(page)
    pim_page = PIMPage(page)

    #login
    login_page.load(config.get("url"))
    login_page.login(config.get("username"), config.get("password"))

    #wait for dashboard
    page.wait_for_url("**/dashboard/**")

    # Navigate to PIM
    pim_page.go_to_pim()

    # Add employee
    pim_page.click_add_employee()

    # manually Generating dynamic data
    # fname = "John" + str(random.randint(1000, 9999))
    # lname = "Doe"
    # full_name = fname + " " + lname

    # Getting employee fname and lname from testdata file
    fname, lname = generate_employee_name ()
    
    # Add employee details
    pim_page.add_employee(fname, lname)

    

    # Validate employee adding
    assert pim_page.is_employee_added()

    # Go back to PIM list
    pim_page.go_to_pim()

    # Search employee
    pim_page.search_employee(fname)

    pim_page.take_screenshot("firstemployeeadded.png")

    # for logging errors if any
    logger = get_logger()
    logger.info("Launching application")
    logger.info("Logging in")
    logger.info("Adding employee")

    # validate employee in table
    assert pim_page.is_employee_in_results(fname)



