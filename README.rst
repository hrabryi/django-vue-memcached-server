memcache_server
===============

Behold My Awesome Project!

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy memcache_server

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



Memcached server
--------------------

This is implementation of memcached protocol with storing data in SQLite.
Server listening 11211 port for incoming connection and data.

Storage commands
------------------

To store new key-value data client sends a command line which looks like this:

set \<key> \<value> \<exptime> \<bytes> \r\n"

Retrieval command:
------------------

The retrieval command "get" operate like this:

get \<key>*\r\n

- <key>* means one or more key strings separated by whitespace.

After this command, the client expects zero or more items, each of
which is received as a text line followed by a data block. After all
the items have been transmitted, the server sends the string

"END\r\n"

to indicate the end of response.

Each item sent by the server looks like this:

VALUE \<key> \<flags> \<bytes> \r\n
\<data block>\r\n

- \<key> is the key for the item being sent

- \<value> is the flags value set by the storage command

- \<bytes> is the length of the data block to follow, *not* including
  its delimiting \r\n

- \<data block> is the data for this item.

If some of the keys appearing in a retrieval request are not sent back
by the server in the item list this means that the server does not
hold items with such keys (because they were never stored, or stored
but deleted to make space for more items, or expired, or explicitly
deleted by a client).

Deletion
--------

The command "delete" allows for explicit deletion of items:

delete \<key> \r\n

- \<key> is the key of the item the client wishes the server to delete

The response line to this command can be one of:

- "DELETED\r\n" to indicate success

- "NOT_FOUND\r\n" to indicate that the item with this key was not
  found.

Exit
----
Use "quit" command to close the session.
