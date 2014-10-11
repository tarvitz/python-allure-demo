Python allure mini-demo
=======================

.. contents:: :local:
   :depth: 2

Requirements
------------

Python dependecies:

- pytest-2.6+
- pytest-allure-adaptor-1.5.0
- lxml-3.4+

Allure dependecies:

- allure-cli 2.2+
- alure-core 1.4.3

Run
---
.. code-block:: bash

   py.test --alluredir=db/allure tests.py
   allure generate db/allure -o db/reports -v 1.4.3

