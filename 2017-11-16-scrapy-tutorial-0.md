---
title: "Scrapy Part 0 : Scrapy the Big Picture and Fundamental"
categories:
  - scrapy
excerpt_separator: "<!--more-->"
---


Explain core skill need to prepare before using Scrapy

<!--more-->

# The Big Picture

![2017-11-16_21-55-27](/assets\images\2017-11-16_21-55-27.jpg)



The data flow in **Scrapy** is controlled by the execution engine, and goes like this:

1. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) gets the initial Requests to crawl from the [Spider](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spiders).

2. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) schedules the Requests in the [Scheduler](https://docs.scrapy.org/en/latest/topics/architecture.html#component-scheduler) and asks for the next Requests to crawl.

3. The [Scheduler](https://docs.scrapy.org/en/latest/topics/architecture.html#component-scheduler) returns the next Requests to the [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine).

4. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) sends the Requests to the [Downloader](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader), passing through the [Downloader Middlewares](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader-middleware) (see [`process_request()`](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.DownloaderMiddleware.process_request)).

5. Once the page finishes downloading the [Downloader](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader) generates a Response (with that page) and sends it to the Engine, passing through the [Downloader Middlewares](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader-middleware) (see [`process_response()`](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.DownloaderMiddleware.process_response)).

6. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) receives the Response from the [Downloader](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader) and sends it to the [Spider](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spiders) for processing, passing through the [Spider Middleware](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spider-middleware) (see [`process_spider_input()`](https://docs.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_input)).

7. The [Spider](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spiders) processes the Response and returns scraped items and new Requests (to follow) to the [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine), passing through the [Spider Middleware](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spider-middleware) (see [`process_spider_output()`](https://docs.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_output)).

8. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) sends processed items to [Item Pipelines](https://docs.scrapy.org/en/latest/topics/architecture.html#component-pipelines), then send processed Requests to the [Scheduler](https://docs.scrapy.org/en/latest/topics/architecture.html#component-scheduler) and asks for possible next Requests to crawl.

9. The process repeats (from step 1) until there are no more requests from the [Scheduler](https://docs.scrapy.org/en/latest/topics/architecture.html#component-scheduler).

   ​

# So What is Your Job ?

When using framework for scrape data, it do a lot for you in a systematic way, from download , extracting and saving data. So your most important job while using Scrapy will be :

* Specify **where** you want to scraping data ?. Basically is a set of url, so Scrapy will crawl data from.
* Specify  **what** you want in each data page ?.  Name, title, image ...



# For Example

For example, We want to get all funny title from Reddit which you could access from link https://www.reddit.com/r/funny/

![2017-11-17_4-26-34](/assets\images\2017-11-17_4-26-34.jpg)

**Where to scrape?**. It is collection of pages which you could access by click to `Next` button at bottom of page.

![2017-11-17_4-28-30](/assets\images\2017-11-17_4-28-30.jpg)

In detail, it will be following Urls.

```python
https://www.reddit.com/r/funny/
https://www.reddit.com/r/funny/?count=25&after=t3_7d8adu
https://www.reddit.com/r/funny/?count=50&after=t3_7dey2i
...
```

**What to scrape ?**. So with each funny story, I care about **title**, **image**, and **score**.

![2017-11-17_5-09-47](/assets\images\2017-11-17_5-09-47.jpg)



# Select Url with Regular Expression

The first important question is how to feed Scrapy with right collection of URL ?. So Scrapy will help you crawl HTML from that pages.

Scrapy using Regular Expression to filter out urls (You will see this in detail next parts). For examples, we want Scrapy crawl following urls

```shell
https://www.reddit.com/r/funny/
https://www.reddit.com/r/funny/?count=25&after=t3_7d8adu
https://www.reddit.com/r/funny/?count=50&after=t3_7dey2i
...
```

What regular expression could filter out theses urls. Let try to find out this in real time with [https://regexr.com/](https://regexr.com/) 

![2017-11-17_8-02-20](/assets\images\2017-11-17_8-02-20.jpg)



# Select HTML Tags with CSS and Xpath



# 

