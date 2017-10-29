---
title: "Complete Scrapy Tutorial Part 2: Scrape Data from Amazon"
categories:
  - scrapy
excerpt_separator: "<!--more-->"
---


*Step by step explain with real example how to scraping web data with Scrapy*

<!--more-->

# The Objective

In this tutorial we will scape data from Amazon. Open link on browser [https://www.amazon.com/best-sellers-books-Amazon/zgbs/books](https://www.amazon.com/best-sellers-books-Amazon/zgbs/books) the page contain 100 best seller book will show up.

![2017-10-29_20-14-21](/assets\images\2017-10-29_20-14-21.jpg)

The objective of this tutorial will be scrape following data item for each book and then save data to a csv file

* Sell order


* Book title
* Author
* Price
* Cover image (Note that we will rename image with book name)



# Understand starting page

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



# Get Book Links

Create a new project call **amazon**

```shell
scrapy startproject amazon
```





# Scrape Book Title, Author, Intro

# Scrape the Book Covers

# Scrape Review Part

