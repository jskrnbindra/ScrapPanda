from lxml import etree
from io import StringIO


class Template:
    """
    A matchable template which yeilds matching items in a page.
    """

    name = 'no-template'

    matching_class_name = 'no-class'
    matching_tag = 'no-tag'
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
        tree = self.to_dom_tree(html)
        meta_extracted = self.extract_tag_meta(sample_text, tree)

        return meta_extracted and self

    def extract_tag_meta(self, sample_text, tree):
        """
        Extracts and populates node's meta, in the DOM tree, which contains the sample text.
        :param sample_text: string
        :param tree: etree
        :return:
        """
        xpath_expression = f'//*[. = "{sample_text}"]'
        elements = tree.xpath(xpath_expression)
        nodes = len(elements)
        if nodes == 0:
            print('Product not found. Maybe try again...')
        elif nodes == 1:
            self.matching_class_name = elements[0].get('class')
            self.matching_tag = elements[0].tag
            return True
        else:
            print('Unexpected number of elements with value as product name')

    def find_matches(self, html):
        """
        Finds matches from the etree which match this template.
        :param html:
        :return:
        """
        tree = self.to_dom_tree(html)
        xpath_exp = self.get_matching_xpath()
        matches = tree.xpath(xpath_exp)

        return matches

    def extract_matches_with_links(self, html):
        """
        Extracts template matches with urls.
        :param html:
        :return:
        """
        matches = self.find_matches(html)
        matches_with_links = [(x.text, self.extract_engulfing_link(x)) for x in matches]

        return matches_with_links

    def get_matching_xpath(self):
        """
        Template specific XPATH string generator.
        :return:
        """
        xpath_expression = f'//{self.matching_tag}[@class = "{self.matching_class_name}"]'

        return xpath_expression

    def extract_nearest_anchor_parent(self, ele):
        if ele.tag == 'a':
            return ele

        if ele.tag == 'html':
            print('No anchor tag found in any ancestors.')
            return False

        return self.extract_nearest_anchor_parent(ele.getparent())

    def extract_engulfing_link(self, ele):
        """
        Extracts youngest <a> tag in ancestors of the ele node
        and returns its href(link).
        :param ele:
        :return:
        """
        anchor_parent = self.extract_nearest_anchor_parent(ele)
        if anchor_parent is None:
            return False
        engulfing_link = anchor_parent.get('href')

        return engulfing_link

    @staticmethod
    def to_dom_tree(html):
        html_as_file = StringIO(html)
        html_parser = etree.HTMLParser()
        dom_tree = etree.parse(html_as_file, parser=html_parser)

        return dom_tree
