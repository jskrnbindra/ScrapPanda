from scrap_panda import ScrapPanda
import sys


def get_parameters():
    """
    Accepts URL, sample product name and sample category as command line arguments.
    Uses default if insufficient arguments provided.
    """
    url = 'https://www.snapdeal.com'
    sample_product_name = 'Lenovo Ideapad 110 (80T70015IH) Notebook (Intel Pentium- 4GB RAM- 1TB HDD- 39.62cm (15.6)- DOS) (Black)'
    sample_category_name = 'Loafers'

    if len(sys.argv) < 4:
        print('\nNo or insufficient command line arguments passed. Using default.\n')
        print('url:', url)
        print('sample_product_name:', sample_product_name)
        print('sample_category_name:', sample_category_name + '\n')
        return url, sample_product_name, sample_category_name

    cla_url = sys.argv[1]
    cla_sample_product_name = sys.argv[2]
    cla_sample_category_name = sys.argv[3]

    return cla_url or url, \
           cla_sample_product_name or sample_product_name, \
           cla_sample_category_name or sample_category_name


if __name__ == '__main__':

    inputs = get_parameters()
    scrapper = ScrapPanda()
    products, categories = scrapper.start(*inputs)

    print(products)
    print(categories)
