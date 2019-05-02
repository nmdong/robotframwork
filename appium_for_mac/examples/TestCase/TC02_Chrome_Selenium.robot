*** Settings ***
Documentation    Suite description
Library      ../Library/chrome_selenium.py
Library      chrome_selenium.Chrome_Selenium      10.102.1.102     4444      WITH NAME      chr

Test Teardown   Run Keyword If Test Failed    clean_up

*** Test Cases ***
TC02 Chrome use selenium
    [Tags]    DEBUG
    log to console  1. Lauch App
    chr.launch browser use selenium     http://appium.io
    log to console  3. exit app
    chr.exit app

*** Keywords ***
clean_up
    log to console  clean_up successfully