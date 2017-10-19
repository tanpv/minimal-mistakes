---
title: "Complete scrapy tutorial : scrape data from reddit"
categories:
  - web scraping
excerpt_separator: "<!--more-->"
---

The advantage of using a framework like Scrapy to scrape data is it do a lot of thing for you. 

<!--more-->


<!-- {% include toc %} -->


### Target 1 : scrape titles, links, score in one page

Scrape all title and link from Reddit funny topics which listed at https://www.reddit.com/r/funny/

For this beginning we only scrape data from just one page.



### Shell command : understanding how to extract data 

This session explain how to use Scrapy shell command to manually finding and testing the way to extract data.

```shell
scrapy shell
```





### Spider : define where to start and how to extract

This session explain how to make Scrapy understand where to start and how to extract data.



### Item : define what data to extract

This session explain how to make Scrapy understand what to extract.



### Crawl command : store data to json, csv, xml file

This session explain way to store scraped data to data file.



### Item Pipeline : filter with score

This session explain way to store scraped data to database



### Target 2 : scrape all pages

Scrape title and link from all pages which start from https://www.reddit.com/r/funny/



### Spider : extend method to specify how to extract

This session explain how to use Rules and Link Extractor to specify way to follow links



### Target 3 : scrape thumbs images

Scrape title, link and image from all pages which start from https://www.reddit.com/r/funny/



### Image Pipeline : download image

This session explain how to configure image pipeline to download save image to local.



### Review it all with architecture

Let look back at Scrapy architecture and understand it all.



