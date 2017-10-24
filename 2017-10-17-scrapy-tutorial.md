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

This session explain how to make Scrapy understand where to start and how to extract data.



## Item : define what to extract

This session explain how to make Scrapy understand what to extract.



## Crawl : store data to json, csv, xml file

This session explain way to store scraped data to data file.



## Item Pipeline : filter with score

This session explain way to store scraped data to database



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



