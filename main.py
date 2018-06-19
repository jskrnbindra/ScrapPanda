from scrap_panda import ScrapPanda


if __name__ == '__main__':
    url = 'https://www.snapdeal.com'
    sample_product_name = 'Lenovo Ideapad 110 (80T70015IH) Notebook (Intel Pentium- 4GB RAM- 1TB HDD- 39.62cm (15.6)- DOS) (Black)'
    sample_category_name = 'Loafers'

    scrapper = ScrapPanda()
    products, categories = scrapper.start(url, sample_product_name, sample_category_name)

    print(products)
    print(categories)
