#!/usr/bin/env python3

from selenium import webdriver

import time

email = input("enter your mail : ")
password = input("enter your password : ")
message = input("enter your message : ")
friend = input("enter your friend : ")
count = int(input("enter your count : "))

try:
    browser = webdriver.Firefox()

    browser.get("https://facebook.com/messages/t/")

    email_input= browser.find_element_by_id("email")

    password_input= browser.find_element_by_id("pass")

    login_button= browser.find_element_by_id("loginbutton")

    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()

    ##search friend ###

    time.sleep(10)

    search_input = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input')

    search_input.send_keys(friend)

    ##click##

    time.sleep(20)

    first_account = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/div[1]/li/div/a/div/div[2]/div/div/span/span/span')

    first_account.click()

    for i in range(count):
    ##message##

        time.sleep(5)

        

        message_input = browser.find_element_by_css_selector('.notranslate')

        message_input.send_keys(message)


    ## send ##

        time.sleep(3)

        sumbbit = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')

        sumbbit.click()
        print("Success")

except:

    print("Fail")