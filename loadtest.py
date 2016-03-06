from funkload_friendly.test import TestCase, description
from funkload_friendly.datatypes import JSONData


class MainTest(TestCase):
    @description("Load top_page")
    def test_top_page(self):
        self.get(self.site_url + "/")


class LoginTest(TestCase):
    def setUp(self):
        # login
        self.get(self.site_url + "/login/")
        self.post(self.site_url + "/login/",
            params=[
                ['username', 'spam'],
                ['password', 'P@ssw0rd'],
                ['csrfmiddlewaretoken', self.cookie['csrftoken']],
            ]
        )

    @description("Load secret_page with login")
    def test_secret_page(self):
        response = self.get(self.site_url + "/secret_page")
        self.assertEqual(response.code, 200)


class APITest(TestCase):
    @description("Load REST API")
    def test_calculate_add(self):
        response = self.post(self.site_url + "/calculate/add/",
            params=JSONData({
                'value1': 100,
                'value2': 50,
            })
        )
        self.assertEqual(response.code, 200)
        self.assertEqual(response.data['result'], 150)
