---
title: "Scrapy Tutorial Part 2: Scrape Data from Amazon"
categories:
  - scrapy
excerpt_separator: "<!--more-->"
---


*Step by step explained `inspection tool` `multiple levels parsing` `image pipeline`*

<!--more-->

# The Objective

In this tutorial we will scape data from Amazon. Open link on browser [https://www.amazon.com/best-sellers-books-Amazon/zgbs/books](https://www.amazon.com/best-sellers-books-Amazon/zgbs/books) the page contain 100 best seller book will show up.

![2017-10-29_20-14-21](/assets\images\2017-10-29_20-14-21.jpg)

The objective of this tutorial will be scrape following data item for each book and then save data to a csv file

* Sell order
* Book title
* Author
* Book summary
* Cover image (Note that we will rename image with book name)



# Understand starting page

As every other scraping data project, first step should be about understand the page, how to extract it.

Open the `shell` with command

```shell
scrapy shell
```

From the `shell` , fetch the starting page with command

```shell
fetch('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books')
```

After `fetch` command, a `response` object is created. Let try to view the html source from `response` with command

```shell
response.text
```

Now let's inspect the page with developer tool from Chrome browser. Move mouse over one of the title, then right click, chose `inspect`.

![2017-10-29_20-42-39](/assets\images\2017-10-29_20-42-39.jpg) 



From inspection, We could see strategy to extract information:

* Each book block is inside a `div` with class name `zg_itemImmersion` 

* Inside father block the rank could be get by `span` tag with class name `zg_rankNumber` 

* Inside father block the link to detail book information could be get by `a` tag with class name `a-link-normal` 

  ![2017-10-29_23-19-02](/assets\images\2017-10-29_23-19-02.jpg)

Now try to extract the rank with css selector and `response` object

```shell
response.css("div.zg_itemImmersion").css("span.zg_rankNumber::text").extract()
```

Rank show up

![2017-10-29_23-39-16](/assets\images\2017-10-29_23-39-16.jpg)

Let try to extract the detail book link

```shell
response.css("div.zg_itemImmersion").css("a.a-link-normal::attr(href)").extract()
```

Return not just have detail link but also has product link, so we need to do filter when coding the `spider`

![2017-10-29_23-44-18](/assets\images\2017-10-29_23-44-18.jpg)

That quite enough of start page understanding, let do project and spider.

# Get Detail Book Links

Create a new project call **amazon**

```shell
scrapy startproject amazon
```

Change current directory to amazon folder and create `spider` call **book**

```shell
scrapy genspider book www.amazon.com
```

Let change `start_urls`  and `parse` function and you have some thing like this

```python
# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    
    name = 'book'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/best-sellers-books-Amazon/zgbs/books']

    def parse(self, response):
        
        # extract data from response
        ranks = response.css("div.zg_itemImmersion").css("span.zg_rankNumber::text").extract()
        links = response.css("div.zg_itemImmersion").css("a.a-link-normal::attr(href)").extract()
        
        detail_links = []
        
        # filter product reviews link
        for link in links:
        	if 'product-reviews' not in link:
        		detail_links.append(link)

        for item in zip(ranks, detail_links):
	        print item[0]
	        print item[1]
```

Now try to run this `spider` with `crawl` command and you will get rank and detail link print out

```shell
scrapy crawl book
```

![2017-10-30_0-22-13](/assets\images\2017-10-30_0-22-13.jpg)

# Define Scrape Data with Item

It is time to define data structure which we want to archive inside file `items.py` . Change file `items.py` as follow:

```python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
	order = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	summary = scrapy.Field() 
```

# Multiple Levels Parsing

Back to spider file, from Amazon page structure. We see that, to get data we should have 2 levels of extraction.

* First extraction happen at starting url, and we could extract `order` and `detail link`
* From `detail link` , we continue to do another `request` , get the `response` and parse remain information : title, author, price, summary and cover image by another function call `parse_detail_info` 

Now let change the `parse` function follow changing in file `items.py`

```python
# -*- coding: utf-8 -*-
import scrapy
# import the item
from amazon.items import AmazonItem


class BookSpider(scrapy.Spider):
	
	name = 'book'
	allowed_domains = ['www.amazon.com']
	start_urls = ['https://www.amazon.com/best-sellers-books-Amazon/zgbs/books']

	def parse(self, response):
		
		# extract data from response
		orders = response.css("div.zg_itemImmersion").css("span.zg_rankNumber::text").extract()
		links = response.css("div.zg_itemImmersion").css("a.a-link-normal::attr(href)").extract()
		
		detail_links = []
		
		# filter product reviews out
		for link in links:
			if 'product-reviews' not in link:
				detail_links.append('https://www.amazon.com/'+link)

		# create data item
		for item in zip(orders, detail_links):
			# create a new item
			new_item = AmazonItem()
			new_item['order'] = item[0]

			# # create a new request and get detail infor on parse detail
			request = scrapy.Request(url=item[1], callback=self.parse_detail_info)

			# transfer item to parse detail function
			request.meta['item'] = new_item

			yield request


	def parse_detail_info(self, response):
		item = response.meta['item']
		print item['order']
		print response.url
```

Note that with Amazon you need to specify the user agent inside `settings.py` file

```python
# Need to have when want to crawl from Amazon
USER_AGENT = 'amazon (+https://tanpham.org)'
```

Now start the crawl and you will see function `parse_detail_info` work as expected.

# Scrape Book Title, Author, Intro

Let's go back to `shell` to see how to scrape data from detail book page. Try with one detail book page.

```
scrapy shell
```

```
fetch('https://www.amazon.com/Leonardo-Vinci-Walter-Isaacson/dp/1501139150/ref=zg_bs_books_1?_encoding=UTF8&psc=1&refRID=7TPBA5D9KY75PJ6S8YHT')
```

Now do some inspection with Chrome developer tool. First item is book title

![2017-10-31_7-54-55](/assets\images\2017-10-31_7-54-55.jpg)

For book title, we could extract by finding `span` tag with `id=productTitle`

```
response.css('span#productTitle::text').extract()
```

For author name

```
response.css('a.contributorNameID::text').extract()
```

 



# Scrape the Book Covers



