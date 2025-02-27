##############################
Contributing to django-machina
##############################

Here are some simple rules to help you contribute to *django-machina*. You can contribute in many ways!

Contributing code
=================

The preferred way to contribute to *django-machina* is to submit pull requests to the `project's Github repository
<https://github.com/ellmetha/django-machina>`_. Here are some general tips regarding pull requests.

.. warning::

    Keep in mind that should propose new features on the `project's issue tracker <https://github.com/ellmetha/django-machina/issues>`_ before starting working on your ideas! Remember that the central aim of *django-machina* is to provide a solid core of a forum project - without much of extra functionality included!

Development environment
-----------------------

You should first fork the `django-machina's repository <https://github.com/ellmetha/django-machina>`_. Then you can get a working copy of the project using the following commands:

.. code-block:: bash

    $ git clone git@github.com:<username>/django-machina.git
    $ cd django-machina && mkvirtualenv machina
    (machina) $ make install

Coding style
------------

Please make sure that your code is compliant with the `PEP8 style guide <https://www.python.org/dev/peps/pep-0008/>`_. You can ignore the "Maximum Line Length" requirement but you should still pay attention to the length of your lines. Remember that your code will be checked using `flake8 <https://pypi.python.org/pypi/flake8>`_. You can use the *django-machina*'s `tox <https://pypi.python.org/pypi/tox>`_ configuration to perform this validation:

.. code-block:: bash

    $ tox -e lint

Tests
-----

You should not submit pull requests without providing tests. *Django-machina* uses `pytest <http://pytest.org/latest/>`_ as a test runner but also as a syntax for tests instead of unittest. So you should write your tests using `pytest <http://pytest.org/latest/>`_ instead of unittest and you should not use the built-in ``django.test.TestCase``.

You can run the whole test suite using the following command:

.. code-block:: bash

    $ py.test

Code coverage should not decrease with pull request! You can easily get the code coverage of the project using the following command:

.. code-block:: bash

    $ make coverage

Using the issue tracker
=======================

You should use the `project's issue tracker <https://github.com/ellmetha/django-machina/issues>`_ if you've found a bug or if you want to propose a new feature. Don't forget to include as many details as possible in your tickets (eg. tracebacks if this is appropriate).
