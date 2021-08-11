from django.db.models.fields import TextField
from django.test import TestCase
from django.urls import reverse
from .models import News
# Create your tests here.

class NewsModelTest(TestCase):
    def setUp(self):
        News.objects.create(title="Fuck!", author="nico", text="HHHHHeLLLLOOO")
    
    def test_text_content(self):
        news = News.objects.get(id=1)
        ex_title = f'{news.title}'
        ex_author = f'{news.author}'
        ex_text = f'{news.text}'

        self.assertEqual(ex_title, "Fuck!")
        self.assertEqual(ex_text, "HHHHHeLLLLOOO")
        self.assertEqual(ex_author, "nico")

class NewsViewTest(TestCase):
    def setUp(self):
        News.objects.create(title="Fuck YOU!", author="nico2", text="HHHHHeLLLLOOO, BBBYYEEE")
    
    def test_views_url_exists_at_proper_location(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
    
    def test_view_url_by_name(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code, 200)

    def test_view_uses_corrent_template(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "home.html")