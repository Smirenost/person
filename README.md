# Overview

[![docs](https://readthedocs.org/projects/person/badge/?version=latest)](https://person.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/5a29d30f3ec7470cb17085a29a4c6a8f)](https://www.codacy.com/manual/0LL13/person?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=0LL13/person&amp;utm_campaign=Badge_Grade)
[![version](https://pyup.io/repos/github/0LL13/person/python-3-shield.svg)](https://pyup.io/repos/github/0LL13/person)
[![supported-versions](https://img.shields.io/pypi/pyversions/person-roles.svg)](https://pypi.python.org/pypi/person-roles)
[![supported-implementations](https://img.shields.io/pypi/implementation/person-roles.svg)](https://pypi.python.org/pypi/person-roles)
![license](https://img.shields.io/cocoapods/l/AFNetworking.svg)
[![update](https://pyup.io/repos/github/0LL13/person/shield.svg)](https://pyup.io/repos/github/0LL13/person)
[![coverage](https://codecov.io/gh/0LL13/person/branch/master/graph/badge.svg)](https://codecov.io/gh/0LL13/person)
[![travis](https://travis-ci.org/0LL13/person.svg?branch=master)](https://travis-ci.org/0LL13/person)

Roles (academic, politician, ...)  of persons, their particulars

## Features

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

## Credits

This package was created with
[`Cookiecutter`](https://github.com/audreyr/cookiecutter) and the 
[`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage)
project template.


## Installation

    pip install person-roles

## Usage

    import person

    Tom = person.Academic("Thomas H.", "Smith", academic_title="MBA")
    print(Tom)

    Academic:
    academic_title=MBA
    first_name=Thomas
    last_name=Smith
    middle_name_1=H.

## Contribute

- [Issue Tracker](https://github.com/0LL13/person/issues)
- [Source](https://github.com/0LL13/person)

## Support

Feel free to fork and improve.

## Warranty

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

## License

MIT License

Copyright (c) 2020 Oliver Stapel
