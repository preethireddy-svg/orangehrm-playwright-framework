from pages.base_page import BasePage

class PIMPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators for adding emp
        self.pim_menu = "a:has-text('PIM')"
        self.add_employee_btn = "button:has-text('Add')"
        self.first_name = "input[name='firstName']"
        self.last_name = "input[name='lastName']"
        self.save_btn = "button:has-text('Save')"
        self.success_header = "h6:has-text('Personal Details')"
        # Locators for searching emp
        self.employee_name_search = "input[placeholder='Type for hints...']"
        self.search_button = "button:has-text('Search')"
        self.result_table = ".oxd-table-body"
        

    def go_to_pim(self):
        self.wait_for(self.pim_menu)
        self.click(self.pim_menu)

    def click_add_employee(self):
        self.click(self.add_employee_btn)

    def add_employee(self, fname, lname):
        self.page.wait_for_selector(self.first_name, timeout=10000)
        self.fill(self.first_name, fname)
        self.fill(self.last_name, lname)
        self.click(self.save_btn)
        
    def is_employee_added(self):
        self.page.wait_for_selector(self.success_header, timeout=10000)
        return True
    
    def search_employee(self, name):
        self.wait_for(self.employee_name_search)
        self.fill(self.employee_name_search, name)
        self.click(self.search_button)

    def is_employee_in_results(self, name):
        self.page.wait_for_selector(self.result_table)
        return self.page.locator(self.result_table).inner_text().__contains__ (name)

    

