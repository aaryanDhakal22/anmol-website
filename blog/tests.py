from urllib import response
from django.test import TestCase

# Create your tests here.


class NewItemTest(TestCase):
    def test_can_save_a_POST_request(self):
        response = self.client.post(
            "/blogs/new",
            data={
                "title_text": "A new title for blog",
                "body_text": "A new body for blog",
            },
        )
        self.assertIn("A new title for blog", response.content.decode())
        self.assertIn("A new body for blog", response.content.decode())

    def test_can_redirect_after_POST(self):
        response = self.client.post(
            "/blogs/new",
            data={
                "title_text": "A new title for blog",
                "body_text": "A new body for blog",
            },
        )
        self.assertTemplateUsed(response, "blogs.html")


class BlogPageTest(TestCase):
    def test_blog_page_returns_correct_html(self):
        response = self.client.get("/blogs/")
        self.assertTemplateUsed(response, "blogs.html")
