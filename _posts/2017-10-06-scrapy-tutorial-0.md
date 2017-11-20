---
title: "Scrapy Part 0 : Scrapy the Big Picture and Fundamental"
categories:
  - scrapy
excerpt_separator: "<!--more-->"
---


Explain core skill need to prepare before using Scrapy : **regular expression, css selector**.

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

# So What is Your Remain Job ?

When using framework for scrape data, it do a lot for you in a systematic way, from schedule, download , extracting and saving data. So your most important job while using Scrapy will be :

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
https://www.reddit.com/r/funny/?count=25&after=t3_7e16ie
https://www.reddit.com/r/funny/?count=50&after=t3_7e42mi
https://www.reddit.com/r/funny/?count=75&after=t3_7e1n14
https://www.reddit.com/r/funny/?count=100&after=t3_7dw9e5
https://www.reddit.com/r/funny/?count=125&after=t3_7e4u1p
...
```

**What to scrape ?**  With each funny story, I care about **title**, **image**, and **score**. Important thing : these information are keep inside HTML tags. So our job is select these tags using `css selector` or `xpath` .

![2017-11-17_5-09-47](/assets\images\2017-11-17_5-09-47.jpg)



# Select Urls with Regular Expression

The first important question is how to feed Scrapy with right collection of URL ?. So Scrapy will help you crawl HTML from that pages.

Scrapy using Regular Expression to filter out urls (You will see this in detail next parts). For examples, we want Scrapy crawl following urls

```shell
https://www.reddit.com/r/funny/
https://www.reddit.com/r/funny/?count=25&after=t3_7e16ie
https://www.reddit.com/r/funny/?count=50&after=t3_7e42mi
https://www.reddit.com/r/funny/?count=75&after=t3_7e1n14
https://www.reddit.com/r/funny/?count=100&after=t3_7dw9e5
https://www.reddit.com/r/funny/?count=125&after=t3_7e4u1p
...
```

What regular expression could filter out theses urls. Let try to find out this in real time with [https://regexr.com/](https://regexr.com/) 

Following regular expression will match required urls

![2017-11-20_9-42-56](/assets\images\2017-11-20_9-42-56.jpg)



Let explain some thing about this regular expression and you will understand how regular expression work.

![2017-11-20_9-45-45](/assets\images\2017-11-20_9-45-45.jpg)

For more detail and practice on regular expression, please access this site https://regexone.com/

# Select HTML Tags with CSS Selector

The second important thing is define what data you want when HTML already crawled. For example you open this page from Chrome browser https://www.reddit.com/r/funny/ . Move mouse above a title and right click then choose ***"Inspect"***. 

![2017-11-20_15-13-00](/assets\images\2017-11-20_15-13-00.jpg)



Chrome inspection tool will show up with all HTML tags from current page. Type in ***"Ctrl + F"*** search tool appear, allow us try to use css selector to select HTML tags.

![2017-11-20_15-25-22](/assets\images\2017-11-20_15-25-22.jpg)

For example, to search for `a` tag with class `title` , we put in following css selector `a.title` then click **Enter** . The result will show up tag by tag.

![2017-11-20_15-30-16](/assets\images\2017-11-20_15-30-16.jpg)

That is how css selector work. To make more clear and detail about css selector, please refer to link 

https://www.w3schools.com/cssref/css_selectors.asp