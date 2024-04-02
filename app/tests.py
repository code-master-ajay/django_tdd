from django.test import TestCase
from .models import MyModel



class Test_model(TestCase):
    
    def test_model_exists(self):
        objs = MyModel.objects.count()

        self.assertEqual(objs, 0)

    def test_model_str(self):
        obj = MyModel(title='test')
        obj.save()

        self.assertEqual(str(obj), 'test')


class TestIndexPage(TestCase):
    def test_index_page(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_page_has_list(self):
        obj = MyModel.objects.create(title='test')
        response = self.client.get('/')

        self.assertContains(response, obj.title)



class DetailPageTest(TestCase):

    def setup(self):
        self.obj1 = MyModel.objects.create(title='test')
        self.obj2 = MyModel.objects.create(title='test')

    
    def test_detail_page (self):
        response = self.client.get(f'/detail/{self.obj1.id}')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')

    def test_detail_page_has_list(self):
        response = self.client.get(f'/detail/{self.obj1.id}')

        self.assertContains(response, self.obj1.title)