# scrapy_fcc

## This repo contains:

- part-3 - basic setup for scrapy spider 
- part-4 - scrapy spider project 'woolscraper' for www.woolwarehouse.co.uk 
- part-4-books - scrapy spider follow along project, scraping books.toscrape.com
- part-5 - updated scraper spider project 'woolscraper_ii' for www.woolwarehouse.co.uk

## Step 1 - Install & activate your python virtual environment

To install the python virtual environment follow the following instructions below.

For Mac: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-macos

For Windows: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-windows

For Linux: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-linux

Then to activate it so that any new modules that are installed are installed into this virtual environment:

For Linux: `source venv/bin/activate`
For Windows: `venv\scripts\activate`

## Step 2 - Install the required python modules

To install the required modules for each project to run you need to install the required python modules using the following command:

`pip install -r requirements.txt`

## Step 3 - Run the project

Once the required python modules are installed, cd into scrapy project folder and you should be able to view the spider(s) with the following command: `scrapy list`

To run the desired spider, use `scrapy crawl <spider_name>` 

Spider names:
Part-3: There is none, as it was just a set up practice
Part-4: woolspider
Part-4-books: bookspider, bookspider_ii, bookspider_3
Part-5: woolspider_ii