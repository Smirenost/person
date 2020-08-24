======
person
======


.. image:: https://img.shields.io/pypi/v/person.svg
        :target: https://pypi.python.org/pypi/person

.. image:: https://img.shields.io/travis/0LL13/person.svg
        :target: https://travis-ci.com/0LL13/person

.. image:: https://readthedocs.org/projects/person/badge/?version=latest
        :target: https://person.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/0LL13/person/shield.svg
     :target: https://pyup.io/repos/github/0LL13/person/
     :alt: Updates


A person's points and particulars with plenty of place for paralipomena



* Free software: MIT license
* Documentation: https://person.readthedocs.io.


Features
--------

Currently names of this structure are supported::

    first_name middle_name_1 middle_name_2 last_name/s
    academic_title/s first_name ... last_name/s
    peer_title/s first_name ... last_name/s
    first_name ... peer_preposition last_name/s
    academic/peer_title first_name ... peer_preposition last_name/s

    There can be first_names like "Robert-Toby"
    A maximum of three first names is supported
    There can be last_names like "Smith-Waterman" or "Große Brömer"
    Academic titles like "Prof.", "MBA" or "Dr." are supported
    Peer prepositions like "van", "de", "y", "vom" are supported
    Peer titles like "Freifrau" or "Junker" are supported

..

A person can be given a profile. Current profiles are academic, noble,
politician, member of parliament.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
