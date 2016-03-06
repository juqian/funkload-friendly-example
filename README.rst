=========================
funkload-friendly-example
=========================

Example code for funkload-friendly.

https://github.com/tokibito/funkload-friendly

::

   $ virtualenv --python=python2.7 venv
   $ . venv/bin/activate
   $ pip install -r requirements.txt
   $ easy_install funkload
   $ pip install funkload-friendly
   $ cd myproject
   $ ./manage.py migrate
   $ ./manage.py runserver

login user:

:username: ``spam``
:password: ``P@ssw0rd``

load testing(once)::

   $ fl-run-test --config=funkload.conf loadtest

load testing(benchmark)::

   $ fl-run-bench --config=funkload.conf loadtest MainTest.test_top_page
   $ fl-run-bench --config=funkload.conf loadtest LoginTest.test_secret_page
   $ fl-run-bench --config=funkload.conf loadtest APITest.test_calculate_add

build benchmark report::

   $ fl-build-report --html -o bench/ bench/test_top_page.xml
   $ fl-build-report --html -o bench/ bench/test_secret_page.xml
   $ fl-build-report --html -o bench/ bench/test_calculate_add.xml

.. note:: fl-build-report requires gnuplot.
