from selenium import webdriver
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
        self.fail('Finish the test!')
        # invitation to enter a to-do list item

        # "Buy peacock feathers" into box

        # hit Enter 

        # add "Use peacock feathers to make a fly" (ie, for fishing)

        # site creates unique URL for list

        # visit URL, site is there

if __name__ == '__main__':
    unittest.main(warnings='ignore')

