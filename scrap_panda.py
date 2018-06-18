from templates import ProductTemplate
from urllib import request
import ssl


class ScrapPanda(object):

    def __init__(self):
        pass

    def start(self, url, sample_product_name, sample_category_name):
        html = self.gethtmlfromurl(url)
        product_template = ProductTemplate().create(sample_product_name, html=html)
        self.get_products()
        self.get_categories()

    def get_products(self):
        print('get products')

    def get_categories(self):
        print('get categories')

    def gethtmlfromurl(self, url):
        print('getting html')
        temp_ssl_context = ssl._create_unverified_context()
        response = request.urlopen(url, context=temp_ssl_context)
        html = response.read().decode('utf-8')
        print('received html')

        return html
