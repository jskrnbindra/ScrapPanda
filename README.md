# ScrapPanda
A quick scrapper to enumerate all products and categories on an e-commerce website's page.

### Prerequisites
Python3.6 or above

## Installation
1. Clone this repo
2. cd into ScrapPanda, create a virtualenv and activate it
3. install dependencies
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py <URL> <sample_product_name> <sample_category_name>
```

#### Where
1. ```bash <URL>``` is URL of the ecommerce website
2. ```bash <sample_product_name>``` is any product's name from the ```bash <URL>``` above.
3. ```bash <sample_category_name>``` is any category's name from the ```bash <URL>``` above.

### Example
```bash
python main.py 'https://www.snapdeal.com'  'Lenovo Ideapad 110 (80T70015IH) Notebook (Intel Pentium- 4GB RAM- 1TB HDD- 39.62cm (15.6)- DOS) (Black)' 'Loafers'
```
