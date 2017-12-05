---
title: "Python Working with JSON data"
categories:
  - Python for Data Engineer
excerpt_separator: "<!--more-->"
---

Explain JSON format and how to working with JSON in Python.

<!--more-->

# What is JSON ?

JSON is data format for sharing data. It is readable lightweight and is good replace for XML. Following is  JSON data example.

![2017-12-06_4-41-42](/assets\images\2017-12-06_4-41-42.jpg)

Some important notes on JSON from example are:

- a JSON object is start with `{` and end with `}` 

- JSON is constructed by `"key":"value"` structure

- JSON `value` could be one of 6 following type:
  - strings

  - numbers

  - objects

  - arrays

  - Booleans (true of false)

    ​

# Import JSON package

To working with JSON, Python has `json` package. So, the first step is import the package

```python
import json
```

`json` package provide the ability to transfer between `JSON text` and `Python object (like dictionary)` 

# Working with JSON string

For working with JSON string, `json package` provide 2 functions :

- `loads` : load from JSON string to Python dictionary. (`s` in `loads` stand for `string`)
- `dumps` : dump from Python dictionary to JSON string. (`s` in `loads` stand for `string`) 

For example following code load `pets` in to `parsed_json` object

```python
import json

# example of json string
pets = '''{
  "pets": [
    {
      "name" : "Purrsloud",
      "species" : "Cat",
      "favFoods" : ["wet food", "dry food", "any food"],
      "birthYear" : 2016,
      "photo" : "https://learnwebcode.github.io/json-example/images/cat-2.jpg"
    },
    {
      "name" : "Barksalot",
      "species" : "Dog",
      "birthYear" : 2008,
      "photo" : "https://learnwebcode.github.io/json-example/images/dog-1.jpg"
    }
  ]
}'''

# from JSON-string to Python-dictionary
parsed_json = json.loads(pets)
```



Now if you want to access the name of first pet :

```python
# access the name of first pet
print(parsed_json['pets'][0]['name'])
```



Let do some explain here, and understand how it work

- `parsed_json['pets']` will access the `value` of `pets key` , it is a array pet object which construct by `[]`
- `parsed_json['pets'][0]` will access the first element inside array
- `parsed_json['pets'][0]['name']` access `value` of `key name` from first object inside array



Now if you want dump back from Python object to JSON string

```python
# dump back from dictionary to json string
back_to_json_string = json.dumps(parsed_json)
print back_to_json_string
```



# Working with JSON file

2 following function used to working with JSON file (which has extension is `.json`) :

- `load` : load from JSON file to Python dictionary. 
- `dump` : dump from Python dictionary to JSON file.

Suppose we want to load data from `sample.json` file (this file has same JSON content)

```python
parsed_json_from_file = json.load(open('sample.json'))
```

After that the way to access data from Python object is the same

```python
# access the name of first pet
print(parsed_json_from_file['pets'][0]['name'])
```

Now if you want to dump back from Python object to file

```python
with open('sample_dump.json', 'w') as outfile:
	json.dump(parsed_json_from_file, outfile)
```



[All my best course on python and data engineer](https://courses.tanpham.org/collections)