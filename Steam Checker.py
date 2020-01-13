# check steam ID's or group's from list.
import selenium
import time
from selenium import webdriver
# get the chromedriver from my mac's bin
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
# read and write. diff files.
names = open('names.txt', 'r')
available = open('available.txt', 'w')
not_available = open('not_available.txt', 'w')
# ask user which they wanna check
grouporid = int(input("Would you like to check groups (1) or ID's (2)? "))

def checkIDs(string) :
    # check the URL for the word
    browser.get('https://steamcommunity.com/id/' + string)
    # check for text on the page that would indicate it's unmade.
    if ("The specified" in browser.page_source) :
        string.strip()
        available.write(string)

    if not ("The specified" in browser.page_source) :
        string.strip()
        not_available.write(string)

def checkgroups(string) :
    # check the group URL for the word
    browser.get('https://steamcommunity.com/groups/' + string)
    # check for text on the page that would indicate it's unmade.
    if ("No group could be retrieved" in browser.page_source) :
        string.strip()
        available.write(string)

    if not ("No group could be retrieved" in browser.page_source) :
        string.strip()
        not_available.write(string)

# grab the time before checking
now = time.time()
amount = 0
# check the list
if (grouporid == 1) :
    for line in names :
        checkgroups(line)
        # increment amount of names
        amount = amount + 1
elif (grouporid == 2) :
    for line in names :
        checkIDs(line)
        amount = amount + 1

# grab the time after checking
rightnowthough = time.time()
# do the math to find time taken
total = rightnowthough - now
# tries per second
tps = amount / total
# close the files
browser.close()
names.close()
available.close()
not_available.close()
print("Checker finished.")
print("Amount of names: " + str(amount))
print("Time taken: " + str(round(total, 3)))
print("Tries per second: " + str(round(tps, 3)))
