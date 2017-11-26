---
title: "Scrapy Part 4: Get Games Data from Steam"
categories:
  - scrapy
excerpt_separator: "<!--more-->"
---

[https://tanpham.org](https://tanpham.org)

Explain **LinkExtractor**, **Paging** and **Form Request**.



<!--more-->

# Objective

In this tutorial, we will extract game data from [http://store.steampowered.com](http://store.steampowered.com). The starting point is this link [http://store.steampowered.com/search/?sort_by=Released_DESC](http://store.steampowered.com/search/?sort_by=Released_DESC) ,which contain collection of more than 30000 games title.

![2017-11-06_21-07-21](/assets\images\2017-11-06_21-07-21.jpg)

From here we could extract detail information for each game

![2017-11-06_21-10-44](/assets\images\2017-11-06_21-10-44.jpg)

# Extract Game Links from First Page

Start a new project call **steam**

```shell
scrapy startproject steam
```

Go inside **steam** folder and create crawl spider with name **game**

```shell
scrapy genspider -t crawl game steampowered.com
```

Change `start_urls` to [http://store.steampowered.com/search/?sort_by=Released_DESC.

Open a detail game page, for example http://store.steampowered.com/app/718080/Artifact_Quest_2/ .

You will see that every game url contain "/app/". So let change the `allow` parameter of `LinkExtractor`. Another thing with `LinkExtractor` is we do not want to follow link because this is detail game page so we want to get data only, not follow other link. So, we have spider.

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GameSpider(CrawlSpider):
    name = 'game'
    allowed_domains = ['steampowered.com']
    start_urls = ['http://store.steampowered.com/search/?sort_by=Released_DESC']

    rules = (
        Rule(LinkExtractor(allow=r'/app/(.+)'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        #print url to see if spider is request game link or not
        print response.url
```

Try to crawl with above spider with **--nolog** 

```shell
scrapy crawl game --nolog
```

and we have following result, seem are links we want. Some game need us to verify age before access, so it redirect to verify age form which include **"agecheck"**. We will deal with **"agecheck"** form later.

![2017-11-06_21-55-53](/assets\images\2017-11-06_21-55-53.jpg)

# Extract Game Links from All Pages

In above session, we only request for 1 page, but overall we have 1333 pages to deal with.

![2017-11-06_21-58-01](/assets\images\2017-11-06_21-58-01.jpg)

Now we need a way to travel between page. Click to page 2 and we see following url

http://store.steampowered.com/search/?sort_by=Released_DESC&page=2

So seem to travel between page, I just need to allow spider crawl url with contain "page". That it, let modify our spider by adding one more extract link rule. And because the second Rule just allow spider to travel between page, we set `follow=True` and do not need to specify a callback function.

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GameSpider(CrawlSpider):
    name = 'game'
    allowed_domains = ['steampowered.com']
    start_urls = ['http://store.steampowered.com/search/?sort_by=Released_DESC']

    rules = (
        Rule(LinkExtractor(allow=r'/app/'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'page',), follow=True),
    )

    def parse_item(self, response):
        print response.url
```

Let try to run crawl again and, seem the unlimited of detail url show up as we expected.

 ```shell
scrapy crawl game --nolog
 ```

# Need for Speed ?

With above spider, we already could travel between pages, but seem quite slow. Reason is spider find for url contain "page" in whole source page. From Chrome developer tool, try to inspection, we will see that link  for page only local inside a `div` tag which have class is `search_pagination`

![2017-11-06_22-41-43](/assets\images\2017-11-06_22-41-43.jpg)

So one way to speed up the spider is limit finding area with parameter `restrict_css`. Now we have following spider

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GameSpider(CrawlSpider):
    
    name = 'game'
    allowed_domains = ['steampowered.com']
    start_urls = ['http://store.steampowered.com/search/?sort_by=Released_DESC']

    rules = (
        
        Rule(LinkExtractor(allow=r'/app/'), callback='parse_item', follow=False),
        # restrict area before search for page link
        Rule(LinkExtractor(allow=r'page', restrict_css='.search_pagination_right')),

    )

    def parse_item(self, response):
        print response.url
```

Try crawl now and you could see how it supper fast now.

Want more speed ? Let's add `restrict_css` when searching for game also

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GameSpider(CrawlSpider):
    
    name = 'game'
    allowed_domains = ['steampowered.com']
    start_urls = ['http://store.steampowered.com/search/?sort_by=Released_DESC']

    rules = (
        # limit area before search for app link
        Rule(LinkExtractor(allow=r'/app/', restrict_css='#search_result_container'), callback='parse_item', follow=False),
        # limit area before search for page link
        Rule(LinkExtractor(allow=r'page', restrict_css='.search_pagination_right')),

    )

    def parse_item(self, response):
        print response.url
```

# Dealing with Age Form

Some of above links show up with **agecheck** like this one [http://store.steampowered.com/agecheck/app/249082/?snr=1_7_7_230_150_1158](http://store.steampowered.com/agecheck/app/249082/?snr=1_7_7_230_150_1158) . Because this type of game make sure you above some age before allow you to access.

![2017-11-06_22-52-44](/assets\images\2017-11-06_22-52-44.jpg)

Now to deal with this situation, Scrapy has some thing call `FormRequest` . With `FormRequest` , we need to put in data so we simulate a POST method to server with defined data.

![2017-11-06_23-46-59](/assets\images\2017-11-06_23-46-59.jpg)

So we change `parse_item` as following

```python
    def parse_item(self, response):

        if '/agecheck/app' in response.url:
            
            # print response.url
            
            yield FormRequest(
                url=response.url,
                method='POST',
                formdata={
                    'snr': '1_agecheck_agecheck__age-gate',
                    'ageDay': '1',
                    'ageMonth': '1',
                    'ageYear': '1955'        
                },
                callback=self.parse_item
            )

        else:
            print response.url
```

Try to run and we will not see "**agecheck**" link  any more.

# Understand Game Detail Page

Now we already has response for all detail page. Let's do some investigate to extract detail data for each game. Enter the shell and try to fetch one game page.

```shell
scrapy shell
```

```shell
fetch('http://store.steampowered.com/app/518790/theHunter_Call_of_the_Wild/')
```

For game title, following selector could extract

```shell
response.css('.apphub_AppName::text').extract()
```

For game summary, use following selector

```shell
response.css('#game_area_description::text').extract()
```

![2017-11-07_0-19-59](/assets\images\2017-11-07_0-19-59.jpg)

# Enjoy Your Game Data

That it, let modify our parse item, so we could get some data.

```python
    def parse_item(self, response):

        if '/agecheck/app' in response.url:
            
            # print response.url

            yield FormRequest(
                url=response.url,
                method='POST',
                formdata={
                    'snr': '1_agecheck_agecheck__age-gate',
                    'ageDay': '1',
                    'ageMonth': '1',
                    'ageYear': '1955'        
                },
                callback=self.parse_item
            )

        else:
            title = response.css('.apphub_AppName::text').extract()
            desc  = response.css('#game_area_description::text').extract()
            # print title
            # print desc
            yield {'title':title,'desc':desc}
```

That it, enjoy your steam data.