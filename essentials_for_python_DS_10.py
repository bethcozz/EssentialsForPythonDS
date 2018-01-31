! pip install BeautifulSoup
from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
'''
#this is our html document

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)
#pass in our html_doc
#get the html.parser
#BS transforms the markup into a parse tree, a set of linked objects
#representing the structure of the document
#here, hard to read b/c no structure. 

#next, call prettify method
print soup.prettify()[0:350]
#added structure and made easier to read 
#TAG OBJECTS: have names and attributes 

#working w/ names
soup = BeautifulSoup('<b body="description"">Product Description</b>', 'html')
#html tells constructor to interpret tag as html markup

tag=soup.b
#tells BS that tag's name is b. reference to our html that we passed in
type(tag)

print tag

tag.name
#returns "b", the name of the tag

tag.name = 'bestbooks'
tag
#change name to 'bestbooks'

#Working w/ attributes
tag['body']
#this is directly from markup we returned in constructor

tag.attrs
#access dictionary of attributes 

tag['id'] = 3
tag.attrs
#add a new attribute to tag, setting it equal to some value
tag
#now have body attribute and id attribute

del tag['body']
del tag['id']
tag
#delete both attrs
tag
#now attrs is empty. all left in this is name bestbooks and "product Description"

html_doc = '''
<html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
'''
#recreate our original html doc
soup = BeautifulSoup(html_doc, 'html.parser')
#recreate soup object using html parser
soup.head
#gives head<>title<>best books
soup.title
#<title>Best books</title>
soup.body.b
#<b>DATA SCIENCE FOR DUMMIES</b>
soup.body
#this gives us too much, everything in the body 
soup.ul
#gives only tags associated w/ unordered list
soup.a
#gives first tag that contains a web link in html.doc

##10.2 Navigatable String objects
soup = BeautifulSoup('<b body="description">Product description</b>')

tag= soup.b
type(tag)
#soup.b is a tag object
#out: bs4.element.Tag
tag.name
#verify name of tag is b
tag.string
#out:  u'Product Description'
#returns sting that's inside of tag named b

type(tag.string)
#nav string

nav_string = tag.string
nav_string

nav_string.replace_with('Null')
tag.string
#replaces 'Product Description' w/ 'Null'

html_doc = '''
<html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
'''
soup = BeautifulSoup(html_doc, 'html.parser')
#convert to parsed string

for string in soup.stripped_strings: print(repr(string))
#return all of strings in the object - white space is ignored
#out: all of the text, starting each line w/ u 'text'
#leaves u's, must be removed later

title_tag = soup.title
title_tag
#out: titleBestBooks/title
title_tag.parent
#out: head/title/BestBooks/title/head
title_tag.string
#u 'Best Books'
title_tag.string.parent
#<title> Best Books</title>

#nav string objects help us retrieve chunks of text that are stored w/i tags

##10.3 Parse Data
import pandas as pd

from bs4 import BeautifulSoup

import re
#regular expression objects
#defines set of strings that matches it

r = '''
<html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
'''
soup = BeautifulSoup(r, 'lxml')
#using lxml parser, not html parser
type(soup)
print soup.prettify()[0:100]

text_only = soup.get_text()
print(text_only)
#strips out the html code and gives you plain text

soup.find_all("li")
#li - name of tag we're interested in
#retrieves everything with li tag

soup.find_all(id="link 3")
#keyword argument
#want all tags with id attribute of 3
#only gives piece that has id link3

soup.find_all('ul')
#string argument
#filter based on exact string
#returns all tags containing string value of ul 

soup.find_all(['ul', 'b'])
#list object filtering
#everything w/ tag name of ul or b
#reads out in same order as html

l = re.compile('l')
#compile regular expression pattern in to re object
#for use in match method
#string l is converted into regular expression
for tag in soup.find_all(l): print(tag.name)
#for each tag in soup object, return and print name of each tag containing l in name attribute
# filtering w/ regular expression


for tag in soup.find_all(True): print(tag.name)
#pring all html tags from within soup object
#true is argument to find_all method
#returns all html tags in original html doc
#filter boolean value

for link in soup.find_all('a'): print(link.get('href'))
#returns all web links within soup object
#search for all a tags, prints href value (which is link)

soup.find_all(string=re.compile("data"))
#return all strings w/ regular expression, can filter by re
#return all strings that contain "data"
#findall gives all strings from OG web page

#10.4 BS in practice
#1. scrape webpage
#2. save results in external file 
from bs4 import BeautifulSoup
import urllib
import re

r = urllib.urlopen('https://analytics.usa.gov').read()
#call variable r
#use url open function - pass in url of page want to scape
#can use any weblink you want
soup = BeautifulSoup(r, "lxml")
#use lxml parser
type(soup)
#created BS object

print soup.prettify()[:100]

for link in soup.find_all('a'): print(link.get('href'))
#loop to find all a tags and retrieve all href vals from them
#for each a tag, print link.get href

for link in soup.findAll('a', attrs={'href': re.compile("^http")}): print link
#find all a tags w/ attribute of href 
#of all those tags, match against them regular expression http
#print only links that start w/ http

file = open('parsed_data.txt', 'wb')
#create new text file to save our scrap
#wb = write into this text file
for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
    soup_link = str(link)
    print soup_link
    file.write(soup_link)
file.flush()
file.close()
#for each link found, covert to string before printing
#soup_link = output of link convert to string
#to write, say file.write(soup_link)
#flush file
#close file 
%pwd
#find out where your file is 
#still stray tags, so needs to be cleaned 


