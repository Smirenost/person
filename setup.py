#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    long_description = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['beautifulsoup4', 'lxml', 'requests', 'gender-guesser', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Oliver Stapel",
    author_email='hardy.ecc95@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: POSIX :: Linux',
        'Topic :: Other/Nonlisted Topic',
    ],
    description="Roles of persons, their particulars",
    install_requires=requirements,
    license="MIT license",
    long_description=long_description + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='person, roles',
    name='person-roles',
    packages=find_packages(include=['person', 'person.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/0LL13/person',
    version='0.1.6',
    zip_safe=False,
    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest-cov'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/0LL13/person/issues',
        'Source': 'https://github.com/0LL13/person',
    },
)


#    entry_points={
#        'console_scripts': [
#            'person-roles = person-roles:main',
#            ],
#        },
