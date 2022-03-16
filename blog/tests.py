import imp
from urllib import response
from django.test import TestCase
from blog.models import Blog

# Create your tests here.


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Blog()
        first_item.title = "the first ever blog"
        first_item.body = "the first ever blog body"
        first_item.save()

        second_item = Blog()
        second_item.title = "the second blog"
        second_item.body = "the second blog body"
        second_item.save()

        saved_items = Blog.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.title, "the first ever blog")
        self.assertEqual(first_saved_item.body, "the first ever blog body")
        self.assertEqual(second_saved_item.title, "the second blog")
        self.assertEqual(second_saved_item.body, "the second blog body")


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
