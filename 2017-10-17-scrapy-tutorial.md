---
title: "Complete scrapy tutorial : scrape data from reddit"
categories:
  - scrapy
excerpt_separator: "<!--more-->"
---


*The advantage of using a framework like Scrapy is it do a lot of thing for you. Your main job is understanding how Scrapy work and make it know what do you want.*

<!--more-->



## Part 1 : scrape titles, links, score in one page

![2017-10-20_21-31-44](/assets\images\2017-10-20_21-31-44.jpg)

One of my favorite place on Reddit is funny image, you could access at  [https://www.reddit.com/r/funny/](https://www.reddit.com/r/funny/) . First part of this tutorial will explain how to scrape the link, title and score from above link.

## Shell command : understanding how to extract data 

### Start the shell

Scrapy framework include a very handy tool called `shell    `  . With `shell` you could try to fetch url, then try to extract data from `response` object. To access `shell` , from command prompt typing in `scrapy shell` , now the shell ready to accept your commands.

![2017-10-22_23-06-43](/assets\images\2017-10-22_23-06-43.jpg)

### Fetch url

Typing in `fetch('https://www.reddit.com/r/funny/')` . After execute above command, a object call `response` is created, `response` object represent result of command `fetch` , so it contain all data from above Reddit url.

### `Response`  object

- From `shell` typing in `view(response)` , a local HTML page is show up from local. Allow us visually know what contain in the page.
- From `shell` typing in `response.url` , this command will show up original url.
- From `shell` typing in `response.text` , this command showup whole HTML source code for this page.

### Extract data from `Response` object

The main thing we need to tell to Scrapy is how to extract data from `response` object. Have 2 way to extract data, using `css selector` or `xpath` . In this tutorial we will use `css selector`. 

From Chrome browser, open url  https://www.reddit.com/r/funny/ , move your mouse above one of title , right click and select `inspect` 





## Spider : define where to start and how to extract

This session explain how to make Scrapy understand where to start and how to extract data.



## Item : define what data to extract

This session explain how to make Scrapy understand what to extract.



## Crawl command : store data to json, csv, xml file

This session explain way to store scraped data to data file.



## Item Pipeline : filter with score

This session explain way to store scraped data to database



## Part 2 : scrape all pages

Scrape title and link from all pages which start from https://www.reddit.com/r/funny/



## Spider : extend method to specify how to extract

This session explain how to use Rules and Link Extractor to specify way to follow links



## Part 3 : scrape thumbs images

Scrape title, link and image from all pages which start from https://www.reddit.com/r/funny/



## Image Pipeline : download image

This session explain how to configure image pipeline to download save image to local.



## Review it all with architecture

Let look back at Scrapy architecture and understand it all.
