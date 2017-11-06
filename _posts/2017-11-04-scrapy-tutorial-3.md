---
title: "Scrapy Tutorial Part 3: Nature Image from Pexels"
categories:
  - scrapy
excerpt_separator: "<!--more-->"
---


Explain **CrawlSpider**, **LinkExtractor**, **Rule**, **ImagePipeline**

<!--more-->

# The Objective

This tutorial explain step by step how to scrape nature image from [https://www.pexels.com](https://www.pexels.com) 

![2017-11-04_8-01-21](/assets\images\2017-11-04_8-01-21.jpg)



# Understand the Page with Shell

Start from this url which listed all nature picture [https://www.pexels.com/search/natural/](https://www.pexels.com/search/natural/) , let go to a specific image, our target is url to download image [https://www.pexels.com/photo/adult-and-cub-tiger-on-snowfield-near-bare-trees-39629/](https://www.pexels.com/photo/adult-and-cub-tiger-on-snowfield-near-bare-trees-39629/) . From inspection tool what we need to extract is `href` attribute of `a` tag which have classes are `btn__primary js-download`

![2017-11-04_9-55-18](/assets\images\2017-11-04_9-55-18.jpg)



Start `shell` with command

```shell
scrapy shell
```

Fetch the image url

```shell
fetch('https://www.pexels.com/photo/adult-and-cub-tiger-on-snowfield-near-bare-trees-39629/')
```

Try to css selector and extract image download link

```shell
response.css('a.btn__primary.js-download::attr(href)').extract()
```

And result is what we need, the full static url to `jpeg` file

![2017-11-04_9-58-25](/assets\images\2017-11-04_9-58-25.jpg)



# Define How to Crawl with CrawlSpider

Create a new scrapy project call `pexels` with command

```shell
scrapy startproject pexels
```

Create a new `crawl` spider name `nature_image` on domain `pexels.com`

```shell
scrapy genspider -t crawl nature_image pexels.com
```

Let change the `start_urls ` to  https://www.pexels.com/search/natural/ .And spider file `nature_image.py` look like this

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NatureImageSpider(CrawlSpider):
    name = 'nature_image'
    allowed_domains = ['pexels.com']
    start_urls = ['https://www.pexels.com/search/natural/']

    rules = (
        Rule(LinkExtractor(allow=r'photo/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
```

Now let's explain what going on in this file:

* `CrawlSpider` : Scrapy provide 2 kind of spider
  *  `Spider` is basic one, with this kind of spider we need to care about how to move from page to page by our self
  *  `CrawlSpider` provide a mechanism to follow links automatically. Our remain job is specify what kind of link we want to follow. We will use `Rule` and `LinkExtractor` classes for this task
* `Rule` : specify following information:
  * `LinkExtractor` specify what kind of link we want engine to make request. All links are requested need to filtered by regular expression specify by `allow` parameter. In this case, we only do request on link which has `photo/` inside
  * `callback` specify function which handle response. In this case is `parse_item` function. We will put parse logic to this function to extract all information we want, in this case is the downloadable image url.
  * `follow` we need to specify value to `True` if we want spider follow the link

Let's do some small change with `parse_item` function and make it print out url of detail images

```python
def parse_item(self, response):
    print response.url
```

Change directory to `pexels` and run spider with command

```shell
cd pexels
scrapy crawl nature_image
```

The detail image urls show up from console

![2017-11-04_10-47-10](/assets\images\2017-11-04_10-47-10.jpg)

Now, put the css selector which we already investigate with `shell` to `parse_item` function, then try to print the downloadable image urls

```python
def parse_item(self, response):
        print response.css('a.btn__primary.js-download::attr(href)').extract()
```

Start again the crawl and we will see the `jpeg` file from console log.

![2017-11-04_10-54-07](/assets\images\2017-11-04_10-54-07.jpg)



# Download Image with ImagePipeline

Scrapy provide a way so it is very convenience way to download image. 

**Step 1** : Enable image pipeline and specify where we want to store images in `settings.py` file

```py
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = 'images'
```



**Step 2** : Edit `items.py` file, add to 2 predefine fields `images` and `image_urls`

```python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PexelsItem(scrapy.Item):
	image_urls = scrapy.Field()
	images = scrapy.Field()
```



**Step 3** : Change spider parse function, then `yield` out the item

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pexels.items import PexelsItem


class NatureImageSpider(CrawlSpider):
    # spider name
    name = 'nature_image'

    # only doing request in these domain
    allowed_domains = ['pexels.com']

    # starting points
    start_urls = ['https://www.pexels.com/search/natural/']

    # how to follow the link
    rules = (
        Rule(LinkExtractor(allow=r'photo/'), callback='parse_item', follow=True),
    )

    # parse response
    def parse_item(self, response):
        item = PexelsItem()
        item['image_urls'] = response.css('a.btn__primary.js-download::attr(href)').extract()
        yield item
```

That it, now try out `crawl` command

```shell
scrapy crawl nature_image
```

And here is result, seem endless stream of image flow from pexels to image folder

![2017-11-04_11-22-51](/assets\images\2017-11-04_11-22-51.jpg)

