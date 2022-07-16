from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

MAX_WAIT = 3


# class NewBlogTest(StaticLiveServerTestCase):
#     def setUp(self):
#         opts = Options()
#         # opts.add_argument("--headless")
#         self.browser = webdriver.Firefox(options=opts)
#         self.live_server_url += "/blogs/staff/"

#     def tearDown(self):
#         self.browser.quit()

#     def wait_for_row_in_list_table(self, row_text):
#         start_time = time.time()
#         while True:
#             try:
#                 table = self.browser.find_element(By.ID, "id_list_table")
#                 rows = table.find_elements(By.TAG_NAME, "tr")
#                 self.assertIn(row_text, [row.text for row in rows])
#                 return
#             except (AssertionError, WebDriverException) as e:
#                 if time.time() - start_time > MAX_WAIT:
#                     raise e
#                 time.sleep(0.5)

#     def test_can_add_blog(self):
#         # Aditya types the url of the new and hip website
#         self.browser.get(self.live_server_url)

#         # He sees that blogs is written in the titel
#         self.assertIn("Blogs", self.browser.title)
#         header_text = self.browser.find_element(By.ID, "head-text").text
#         self.assertIn("Blogs", header_text)

#         # He types a 'why to become doctor' in title for a blog
#         title = self.browser.find_element(By.ID, "id_new_title")
#         title.send_keys("why to become doctor")
#         # he proceds to type 'for the foreplay' in body for the blog
#         body = self.browser.find_element(By.ID, "id_new_body")
#         body.send_keys("for the foreplay")

#         # HE then presses enter
#         submit_button = self.browser.find_element(By.ID, "submit_blog")
#         submit_button.click()

#         # and the page updates and now the page has listed
#         # 1. why to become doctor : for the foreplay
#         self.wait_for_row_in_list_table("1. why to become doctor : for the foreplay")

#         # There is still a text box inviting to add another. he emters
#         # what is the meaning of life : 69
#         self.browser.get(self.live_server_url)
#         title = self.browser.find_element(By.ID, "id_new_title")
#         title.send_keys("what is the meaning of life")
#         body = self.browser.find_element(By.ID, "id_new_body")
#         body.send_keys("69")

#         # HE then presses enter
#         submit_button = self.browser.find_element(By.ID, "submit_blog")
#         submit_button.click()

#         # The page updates again and now shows both items on his list
#         self.wait_for_row_in_list_table("1. why to become doctor : for the foreplay")
#         self.wait_for_row_in_list_table("1. what is the meaning of life : 69")

        # he wonders whether the site will remember her list. Then she sees that
        # the site has generated a unique URL for her -- the is some explanatory text
        # to that effect
        # self.fail("Finish the test!")

