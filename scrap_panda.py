from templates import ProductTemplate, CategoryTemplate
from urllib import request
import ssl


class ScrapPanda(object):

    def __init__(self):
        pass

    def start(self, url, sample_product_name, sample_category_name):
        html = self.gethtmlfromurl(url)

        products = self.extract_products(sample_product_name, html)
        categories = self.extract_categories(sample_category_name, html)

        return products, categories

    @staticmethod
    def extract_products(sample_product_name, html):
        print('Extracting products...')
        product_template = ProductTemplate().create(sample_product_name, html=html)
        if product_template:
            return product_template.extract_matches_with_links(html)
        print('Unable to create Product Template. Aborting...')

    @staticmethod
    def extract_categories(sample_category_name, html):
        print('Extracting categories...')
        category_template = CategoryTemplate().create(sample_category_name, html=html)
        if category_template:
            return category_template.extract_matches_with_links(html)
        print('Unable to create Category Template. Aborting...')

    @staticmethod
    def gethtmlfromurl(url):
        print('Fetching resource...')
        temp_ssl_context = ssl._create_unverified_context()
        response = request.urlopen(url, context=temp_ssl_context)
        html = response.read().decode('utf-8')

        return html
