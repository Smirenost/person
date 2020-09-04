Overview
========

.. list-table::
    :widths: 10 100
    :stub-columns: 1

    * - .
      - | |Codacy Badge| |coverage| |build|
    * - .
      - | |py3| |supported-versions| |supported-implementations|
    * - .
      - | |license| |update| |docs| |pypi|

.. |docs| image:: https://readthedocs.org/projects/person/badge/?version=latest
    :target: https://person.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |Codacy Badge| image:: https://app.codacy.com/project/badge/Grade/5a29d30f3ec7470cb17085a29a4c6a8f
    :target: https://www.codacy.com/manual/0LL13/person?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=0LL13/person&amp;utm_campaign=Badge_Grade)  

.. |build| image:: https://travis-ci.org/0LL13/person.svg?branch=master
    :alt: Travis-CI Build Status

.. |py3| image:: https://pyup.io/repos/github/0LL13/person/python-3-shield.svg
    :target: https://pyup.io/repos/github/0LL13/person/
    :alt: Python 3

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/person-roles.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/person-roles

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/person-roles.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/person-roles

.. |license| image:: https://img.shields.io/cocoapods/l/AFNetworking.svg
    :alt: CocoaPods

.. |update| image:: https://pyup.io/repos/github/0LL13/person/shield.svg
    :target: https://pyup.io/repos/github/0LL13/person/
    :alt: Updates

.. |coverage| image:: https://codecov.io/gh/0LL13/person/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/0LL13/person

.. |pypi| image:: https://pypi/v/person-roles
    :target: https://img.shields.io/pypi/v/person-roles
    :alt: PyPI


A set of dataclasses concerning roles (academic, politician, ...)  of persons and their particulars

Features
--------

Currently names of this structure are supported::

    Names:                       first_name middle_name_1 middle_name_2 last_name/s
    Names with academic title:   academic_title/s first_name ... last_name/s
    Names with peer title:       peer_title/s first_name ... last_name/s
    Names with peer preposition: first_name ... peer_preposition last_name/s
    Names with all titles:       academic/peer_title first_name ... peer_preposition last_name/s

These roles have been sketched::

    Academic - academic_title
    Person - gender, born, age, deceased
    Noble - peer_title, peer_preposition
    Politician - electoral_ward, ward_no, voter_count, minister, offices, party, parties
    MdL - legislature, parl_pres, parl_vicePres

Usage
=====

::

    import person

    Tom = person.Academic("Thomas H.", "Smith", academic_title="MBA")
    print(Tom)

    Academic:
    academic_title=MBA
    first_name=Thomas
    last_name=Smith
    middle_name_1=H.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Installation
------------


    pip install person-roles

Contribute
----------

- Issue Tracker: https://github.com/0LL13/person/issues
- Source: https://github.com/0LL13/person

Support
-------

Feel free to fork and improve.

Warranty
--------

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL
THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY
DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

License
-------

MIT License

Copyright (c) 2020 Oliver Stapel
