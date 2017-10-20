---
title: "Complete scrapy tutorial : scrape data from reddit"
categories:
  - web scraping
  - scrapy
excerpt_separator: "<!--more-->"
---


*The advantage of using a framework like Scrapy is it do a lot of thing for you. Your main job is understanding how Scrapy work and make it know what do you want.*

<!--more-->



### Part 1 : scrape titles, links, score in one page

One of my favorite place on Reddit is funny image, you could access at  [https://www.reddit.com/r/funny/](https://www.reddit.com/r/funny/) . First part of this tutorial will explain how to scrape the link, title and score from above link.

![2017-10-20_21-31-44](\assets\images\2017-10-20_21-31-44.jpg)



### Shell command : understanding how to extract data 

`scrapy shell` 



### Spider : define where to start and how to extract

This session explain how to make Scrapy understand where to start and how to extract data.



### Item : define what data to extract

This session explain how to make Scrapy understand what to extract.



### Crawl command : store data to json, csv, xml file

This session explain way to store scraped data to data file.



### Item Pipeline : filter with score

This session explain way to store scraped data to database



### Part 2 : scrape all pages

Scrape title and link from all pages which start from https://www.reddit.com/r/funny/



### Spider : extend method to specify how to extract

This session explain how to use Rules and Link Extractor to specify way to follow links



### Part 3 : scrape thumbs images

Scrape title, link and image from all pages which start from https://www.reddit.com/r/funny/



### Image Pipeline : download image

This session explain how to configure image pipeline to download save image to local.



### Review it all with architecture

Let look back at Scrapy architecture and understand it all.
