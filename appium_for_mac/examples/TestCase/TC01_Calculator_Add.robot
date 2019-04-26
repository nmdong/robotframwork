*** Settings ***
Documentation    Suite description
Library      ../Library/calculator.py

Library       calculator.Calculator          WITH NAME       cal

Test Teardown   Run Keyword If Test Failed    clean_up
*** Test Cases ***
TC01_Calculator_Add
    [Tags]    DEBUG
    log to console  1. Lauch App
    cal.lauch_app   10.102.1.102     4622


*** Keywords ***
clean_up
    log to console  Done