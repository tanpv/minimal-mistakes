

# Overview excel structure

![2017-12-30_10-40-27](/assets\images\2017-12-30_10-40-27.jpg)



- Each ```xlsx``` file is called a ```workbook``` , in this course we will work with xlsx file call 500.xlsx which contain personal data of 1500 peoples (500 from US, 500 from UK and 500 from CA)

- Inside a ```workbook``` contain 1 or many ```worksheet``` . From image you can see 3 worksheets with name : us-500 , uk-500, ca-500.

- Inside ```worksheet``` contain ```columns``` and ```rows``` of data. Normally the first row will contain all column name.

- Each data ```cell``` is specified by it's ```column``` and ```row``` . For example company name "Printing Dimensions" is specified by row = 2 and column = "C"

  ![2017-12-30_10-17-36](/assets\images\2017-12-30_10-17-36.jpg)



# Install working environment

## Install python & openpyxl with anaconda

Both Python and openpyxl could be installed by Anaconda. Go to [download page](https://www.anaconda.com/download/) and download Anaconda for Python 3.6. After download, just double click to install with default option.

![2017-12-25_13-36-16](/assets\images\2017-12-25_13-36-16.jpg)



After install, open command prompt and typing in `python` . The anaconda and python version should show up as below

![2017-12-25_13-39-22](/assets\images\2017-12-25_13-39-22.jpg)

From python shell, import **openpyxl** to make sure that it is installed successfully.

![2017-12-25_13-41-35](/assets\images\2017-12-25_13-41-35.jpg)



## Install Sublime as python IDE

In this course I use [Sublimetext](https://www.sublimetext.com/) as Python IDE to writing code (you can choose any other text edition you want). I choose Sublimtext due to :

- We could run python right from editor by short cut key "Ctrl + B"

- It very fast text editor

- Have good theme to high light code

  ​



# Part 1 : Working with existing xlsx file

## Loading workbook from local file

First thing we need to do is import module `openpyxl` with

```python
import openpyxl
```

This module provide function allow us to to create a workbook or load a workbook from a file. In the first part of this course we will load a existing workbook from a `500.xlsx` file.

```python
# loading workbook from file
wb = openpyxl.load_workbook('500.xlsx')
```

## Access worksheet from workbook

After load workbook, we could access current active worksheet with code. Only has one active worksheet at a time, and you could access data only from active worksheet. Default active worksheet is the first sheet.

```python
# get current active worksheet
current_active_worksheet = wb.get_active_sheet()
print(current_active_worksheet)
```

To get name of all worksheets

```python
# get all sheet name
all_sheet_names = wb.get_sheet_names()
print(all_sheet_names)
```

Now, you can set active sheet by name

```python
current_active_worksheet = wb.get_sheet_by_name('uk-500')
print(current_active_worksheet)
```

Following loop could help to access all sheet

```python
# for loop to access all sheet inside workbook
for ws in wb:
	print(ws.title)
```

## Access one cell from worksheet

With MS Excel:

* Column is named from by one or combine of many alphabet characters  A, B, C ...
* Row is named with numbers 1, 2, 3 ...

One cell could be accessed simply by specify column and row combination. And then actual data could be accessed with `value` property

```python
# print out data at column A and row 2 of current worksheet
print(ws['A2'].value)
# set value for one cell
ws['A2'] = 'Tan Pham'
# print out new data
print(ws['A2'].value)
```

## Access one row, column from worksheet

If we only specify just column, we could access all data inside that column

```python
# print all data from column A (the first column)
for cell in ws['A']:
	print(cell.value)
```

If we only specify just row, we could access all data inside that row

```python
# print all data from row 1
for cell in ws['1']:
	print(cell.value)
```

## Access all rows, all columns from worksheet

Incase we want to scan the whole sheet, `openpyl` provide property call `rows` and `columns`.

```python
# access all data , row by row
for row in ws.rows:
    for cell in row:
        print(cell.value)
        
# access all data , column by column
for column in ws.columns:
	for cell in column:
		print(cell.value)
```

## Save workbook

After doing modify data, to save workbook with name

```python
# save workbook with name
wb.save("500.xlsx")
```

# Part 2 : Create workbook and fill data from memory

## Create a new workbook in memory



## Add worksheet

## Add data

## Save workbook

# Part 3 :  Add Filter, Set Sort, Add Chart, Set Styles

## Filter & sort

## Chart

## Styles