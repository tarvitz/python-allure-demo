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

PIP & VirtualENV
~~~~~~~~~~~~~~~~
.. code-block:: bash

   $ virtualenv --no-site-packages ve --python python2.7
   $ source ve/bin/activate
   (ve) $ pip install -r requirements.txt

Issue #39
---------
`Issue #39 <https://github.com/allure-framework/allure-python/issues/39>`_
Use
.. code-block:: bash

   (ve) $ ./run_tests.sh

Or
.. code-block:: bash

   (ve) $ py.test --alluredir=db/allure tests.py
   $ allure generate db/allure -o db/reports -v 1.4.3

Issue #40
---------
`Issue #40 <https://github.com/allure-framework/allure-python/issues/40>`_
Use
.. code-block:: bash

   (ve) $ ./run_doctests.sh

.. code-block:: bash

   (ve) $ py.test --alluredir=db/allure_doctests --doctest-modules helpers.py
   $ allure generate db/allure_doctests db/doctests -v 1.4.3

