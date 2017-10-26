---
title: "Complete scrapy tutorial : scrape data from reddit"
categories:
  - scrapy
excerpt_separator: "<!--more-->"
---


*Step by step explain with real example how to scraping web data with Scrapy*

<!--more-->

## Part 1 : scrape titles, links, score in one page

![2017-10-20_21-31-44](/assets\images\2017-10-20_21-31-44.jpg)

One of my favorite on Reddit is funny image page, you could access at  [https://www.reddit.com/r/funny/](https://www.reddit.com/r/funny/) . First part of this tutorial will explain how to scrape the link, title and score from above link.



## Shell : understanding the page 

Scrapy framework include a very handy tool called `shell    `  . With `shell` you could try to fetch url, then try to extract data from `response` object. To access `shell` , from command prompt typing in `scrapy shell` , now the shell ready to accept your commands.

![2017-10-22_23-06-43](/assets\images\2017-10-22_23-06-43.jpg)

Typing following command then enter

```shell
fetch('https://www.reddit.com/r/funny/')
```

After execute above command, a object call `response` is created, `response` object represent result of command `fetch` , so it contain all data from above Reddit url. After have `response` object, we could show up some information as below:

- Typing in `view(response)` , a local HTML page is show up on browser, allow us visually know what contain in the page.
- Typing in `response.url` , this command will show up original url.
- Typing in `response.text` , this command show up whole HTML source code for this page.

The main thing we need to tell to Scrapy is how to extract data from `response` object. Have 2 way to extract data, using `css selector` or `xpath` . In this tutorial we will use `css selector`. 

From Chrome browser, open url  [https://www.reddit.com/r/funny/](https://www.reddit.com/r/funny/) , move your mouse above one of title , right click and select `inspect` 

![2017-10-22_23-55-13](/assets\images\2017-10-22_23-55-13.jpg)

From inspection tool, we see that we need to care about all `a` tag which has css class call `title` 

![2017-10-23_20-51-57](/assets\images\2017-10-23_20-51-57.jpg)

Type following command then enter :

```shell
response.css("a.title").extract()
```

This command using css selector to extract all `a` tags which has class `title` .

![2017-10-23_21-00-09](/assets\images\2017-10-23_21-00-09.jpg)

We want text title, so typing following command then enter

```sh     
response.css("a.title::text").extract()
```

This command will extract all wanted title text as show below

![2017-10-23_21-06-19](/assets\images\2017-10-23_21-06-19.jpg)

To extract the link title, from inspection tool, we need to get value of attribute name `href` 

```shell
response.css("a.title::attr(href)").extract()
```

All links will be extracted

![2017-10-23_21-10-14](/assets\images\2017-10-23_21-10-14.jpg)

Related to score, let's do another inspection by move mouse to above score, right click and then select `inspect` . We found that we need to find `div` tag with class `score unvoted` .

![2017-10-23_21-13-04](/assets\images\2017-10-23_21-13-04.jpg)

Let's try to extract all score by following command

```shell
response.css("div.score.unvoted::attr(title)").extract()
```

Following result return

![2017-10-23_21-16-33](/assets\images\2017-10-23_21-16-33.jpg)

This understanding of how to extract data will be completely applied when we create Scrapy project. Now let summary useful thing we can do with shell:

- ***fetch('url')***  will return `response` object which contain all information.


- ***view(response)*** view local web page on browser


- ***response.url*** will return original url which using on fetch command


- ***response.text*** will return entire HTML source code from page


- ***response.css('').extract()***  will filter HTML source code based on css selector then extract wanted information
  - *'css_selector::**text**'* will return text of extracted tags
  - *'css_selector::**attr**(attribute_name)'* will return value of attribute_name



## Spider : where to start and how to extract

Now, it time to create new Scrapy project. From command prompt, enter command and enter

```shell
scrapy startproject reddit
```

A new project folder name **reddit** will be automatically created with following structure

![2017-10-25_20-25-00](/assets\images\2017-10-25_20-25-00.jpg)



Now change current directory to **reddit** then create a new `spider` . You need to pass on spider name and the domain, in this case is reddit.com

```shell
cd reddit
scrapy genspider reddit_job reddit.com
```

A new file call **reddit_job.py** will be created inside spider folder with following content

```python
# -*- coding: utf-8 -*-
import scrapy

class RedditJobSpider(scrapy.Spider):
    name = 'reddit_job'
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/']

    def parse(self, response):
        pass
```

 

Let explain what inside this spider file

- `name` is the name of spider, this name will be used when we want to run this spider


- `allowed_domains` spider will only crawl file in this list of domain


- `start_urls` starting point so spider start crawling, let edit the `start_urls` to https://www.reddit.com/r/funny/

- `parse` function, this function will parse the response which return automatically from crawl result.

  We will use selector which already tried successfully with `shell` in this function to extract data.

Let try to change `parse` function as following code

```python
# -*- coding: utf-8 -*-
import scrapy


class RedditJobSpider(scrapy.Spider):
    
    name = 'reddit_job'
    allowed_domains = ['reddit.com']

    # we start from funny title
    start_urls = ['https://www.reddit.com/r/funny/']

    def parse(self, response):
        print response.css("a.title::text").extract()
        print response.css("a.title::attr(href)").extract()
        print response.css("div.score.unvoted::attr(title)").extract()
```

Now let back to command prompt and start the reddit_job spider with command

```shell
scrapy crawl reddit_job
```

You will see our data is extract and print out to console as 3 list. So, spider extraction working fine.



## Item : define what to extract

`items.py` will be place where you specify what data you want. Each data item will be a `Field` object.

Let change file `items.py` with following content

```python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RedditItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
```

Now let change spider `parse` function a little bit correspond to item we just created. The point is `parse` function will `yield` out items, each item will contain data we want to extract.

```python
# -*- coding: utf-8 -*-
import scrapy
# Import so parse could understand RedditItem define structure
from reddit.items import RedditItem

class RedditJobSpider(scrapy.Spider):
    
    name = 'reddit_job'
    allowed_domains = ['reddit.com']

    # we start from funny title
    start_urls = ['https://www.reddit.com/r/funny/']

    def parse(self, response):
        titles = response.css("a.title::text").extract()
        hrefs = response.css("a.title::attr(href)").extract()
        scores = response.css("div.score.unvoted::attr(title)").extract()

        for item in zip(titles, hrefs, scores):

        	new_item = RedditItem()
        	
        	new_item['title'] = item[0]
        	new_item['url'] = item[1]
        	new_item['score'] = item[2]
            
        	yield new_item
```



Now let's run the crawl command again

```shell
scrapy crawl reddit_job
```

Console will print out data items as expected. That it, we just create a fully functional Scrapy project.

![2017-10-25_22-30-58](/assets\images\2017-10-25_22-30-58.jpg)



## Crawl : store data to json, csv, xml file

For almost Scrapy project,  after be extracted data will be saved to database or file. To save data to csv file, let execute crawl command as below

```shell
scrapy crawl reddit_job -o out_data.csv -t csv
```

File with name `out_data.csv` is created and contain our data like magical.

![2017-10-25_22-43-38](/assets\images\2017-10-25_22-43-38.jpg)

It is very similar if you want export data to json or xml file

```shell
scrapy crawl reddit_job -o out_data.json -t json
```

```shell
scrapy crawl reddit_job -o out_data.xml -t xml
```



## Item Pipeline : filter with score value

Some time after extracting data (after  `yield` in `parse`  function) you want to do some extra processing before data go to data base or file. Some kind of extra processing : remove duplicate, add to database. In this session I will show you how to filter data base on score value. Mean if the score is below a value, I will drop data, so the data not go in to csv file.

To do this Scrapy provide object call `ITEM_PIPELINES` . Have 2 steps to enable and apply `ITEM_PIPELINES`. First, from reddit project folder , open the file `settings.py` then uncomment `ITEM_PIPELINES` part.

```python
ITEM_PIPELINES = {
   'reddit.pipelines.RedditPipeline': 300,
}
```

Second, from project folder, open the file `pipelines.py` , in this file you will modify function `process_item` to add your logic you want. In this function, I  will drop the data item if score value below 10000.

```python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class RedditPipeline(object):
    def process_item(self, item, spider):
    	if int(item['score']) > 10000:
        	return item
        else:
        	raise DropItem("too low score")

```

Now let try crawl command

```python
scrapy crawl reddit_job -o out_data_filter.csv -t csv
```

From the console you will see drop message for data which have score < = 10000

![2017-10-26_7-58-11](/assets\images\2017-10-26_7-58-11.jpg)

In in the csv file, you will only see the data item which score > 10000

![2017-10-26_8-06-25](/assets\images\2017-10-26_8-06-25.jpg)



## Part 2 : scrape all pages

Scrape title and link from all pages which start from https://www.reddit.com/r/funny/



## Spider : improve method to specify how to extract

This session explain how to use Rules and Link Extractor to specify way to follow links



## Part 3 : scrape thumbs images

Scrape title, link and image from all pages which start from https://www.reddit.com/r/funny/



## Image Pipeline : download image

This session explain how to configure image pipeline to download save image to local.



## Review it all with architecture

Let look back at Scrapy architecture and understand it all.



## Resources 

| Resource     | Link                                     |
| :----------- | :--------------------------------------- |
| CSS selector | https://www.w3schools.com/cssref/css_selectors.asp |
|              |                                          |
|              |                                          |
|              |                                          |
|              |                                          |
|              |                                          |



