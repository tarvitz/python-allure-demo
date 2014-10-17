#!/bin/bash
ALLURE_CLI="allure"
py.test --alluredir=db/allure tests.py
echo "run allure, generating reports"
$ALLURE_CLI generate db/allure/ -o db/reports/ -v 1.4.3
