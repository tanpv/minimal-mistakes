---
title: "Scrapy tutorial : scrape jobs from craigslist"
categories:
  - web scraping
excerpt_separator: "<!--more-->"
---



This tutorial will show up step by step how to using **Scrapy** to scrape data from **craigslist.com**

<!--more-->



[TOC]

### Mission Possible

Suppose you are interested about job market on Craigslist. Open the link https://sfbay.craigslist.org/d/software-qa-dba-etc/search/sof from browser and you can see all software job which listed at San Francisco bay area. We will scrape information from all of this job.

![2017-10-14_22-13-47](/assets/images/2017-10-15_9-10-41.jpg)



### Install Scrapy

To install Scrapy with pip, start command prompt on Windows (on Mac is terminal) and running following command.

```shell
pip install scrapy
```

After install Scrapy. Typing `scrapy` to command prompt, the list of all available commands will show up. We will return with some of these commands in next sessions.

```shell
scrapy
```

![2017-10-15_23-11-58](C:\site\minimal-mistakes\assets\images\2017-10-15_23-11-58.jpg)



### Play with Scrapy shell

#### Start the shell

Scrapy contain a very handy tool call **shell**. Normally play with shell is the first step I did to begin any scraping project. The shell help us understand how to scrape data work, and this understanding will be applied when we writing code for extracting data. Play with the shell will be very fun part.

To start shell, typing to command prompt, shell will start and ready for use.

```shell
scrapy shell
```

![2017-10-15_23-21-55](C:\site\minimal-mistakes\assets\images\2017-10-15_23-21-55.jpg)



#### Fetch webpage

```shell
fetch("https://sfbay.craigslist.org/d/software-qa-dba-etc/search/sof")
```

#### The "response" object

```shell
view(response)
```

```shell
response.url
```

```shell
response.text
```

#### **Extract data with selector**

```shell
response.css(".result-title")
```

```shell
response.css(".result-title::text").extract()
```

```shell
response.css(".result-title::attr(href)").extract()
```

```shell
response.css(".result-date::text").extract()
```

Note: Using tab for auto complete and auto suggestion.

### Create a new scrapy project

```shell
scrapy startproject craigslist
```

#### Scrapy project structure



### Create a new spider

```shell
cd craigslist
scrapy genspider software_jobs_sfbay craigslist.org
```

#### Spider structure



### Running spider

### Export scrape result to csv / json