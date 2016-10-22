from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # call up the homepage
        self.browser.get('http://localhost:8000')
        # page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # invitation to enter a to-do list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        # "Buy peacock feathers" into box
        inputbox.send_keys('Buy peacock feathers')
        # hit Enter
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table")
        # add "Use peacock feathers to make a fly" (ie, for fishing)
        self.fail('Finish the test!')
        # site creates unique URL for list

        # visit URL, site is there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
