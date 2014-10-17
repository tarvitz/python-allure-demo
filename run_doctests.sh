#!/bin/bash
ALLURE_CLI="allure"
ALLURE_REPORTS="db/doctests"
ALLURE_DIR="db/allure_doctsts"
echo "run doctests"
py.test --doctest-modules helpers.py

echo "run doctests with allure report generating"
py.test --alluredir=$ALLURE_DIR --doctest-modules helpers.py
echo "run allure, generating reports"
$ALLURE_CLI generate $ALLURE_DIR -o $ALLURE_REPORTS -v 1.4.3
