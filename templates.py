from template import Template


class ProductTemplate(Template):

    name = 'ProductTemplate'

    def __init__(self):
        super().__init__()


class CategoryTemplate(Template):

    name = 'ProductTemplate'

    def __init__(self, class_name):
        super().__init__()
        self.class_name = class_name

