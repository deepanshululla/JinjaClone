## Jinja Clone

A toy templating engine written using python and Antlr.

`What's more fun than writing code`

### **`Writing code that writes code.`**

### What is Jinja?
Jinja(https://jinja.palletsprojects.com/en/2.11.x/) is a templating engine in python to automatically generate html documents, based on the arguments passed into the template.

This project is an attempt to create a template engine that
uses Antlr(https://www.antlr.org/) to create grammar as well as the abstact syntax tree for our template engine.


### Demo
```bash

docker run deepanshululla/jinja_clone

```
The above command assumes the directory is ./test_files/basics.

To use this in your custom project, you need to have exactlu
one json(namespace params) and temlate file.

```bash
echo MY_DIR_LOCATION="my location for files"

docker run  -v $$MY_DIR_LOCATION:/data deepanshululla/jinja_clone --directory=/data

```


### What we currently support

1) Assignment operations
2) Arithmetic operations
3) if else-if and else statements
4) While loop support.


