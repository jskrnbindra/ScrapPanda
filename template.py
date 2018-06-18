from lxml import etree
from io import StringIO


class Template:

    name = 'no-template'
    class_name = 'no-class'
    class_pattern = r''

    def __init__(self):
        pass

    def create(self, sample_text, html):
        """
        Creates and returns a matching template.
        :param sample_text:
        :param html:
        :return:
        """
        tree = self.get_dom_tree(html)
        classname = self.getclassname(sample_text, tree)
        print(classname)

    def getclassname(self, sample_text, tree):
        xpath_expression = f'//*[. = "{sample_text}"]'
        elements = tree.xpath(xpath_expression)
        nodes = len(elements)
        if nodes == 0:
            print('Product not found. Maybe try again...')
        elif nodes == 1:
            classname = elements[0].get('class')
            return classname
        else:
            print('Unexpected number of elements with value as product name')

    @staticmethod
    def get_dom_tree(html):
        html_as_file = StringIO(html)
        html_parser = etree.HTMLParser()
        dom_tree = etree.parse(html_as_file, parser=html_parser)

        return dom_tree
