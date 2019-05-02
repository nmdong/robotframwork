*** Settings ***
Documentation    Suite description
Library      ../Library/chrome.py
Library      chrome.Chrome                  WITH NAME      chr

Test Teardown   Run Keyword If Test Failed    clean_up

*** Test Cases ***
TC02 Chrome not use selenium
    [Tags]    DEBUG
    log to console  1. Lauch App
    chr.launch browser       10.102.1.102     4622      appium.io
    log to console  3. exit app
    chr.exit app

*** Keywords ***
clean_up
    log to console  clean_up successfully