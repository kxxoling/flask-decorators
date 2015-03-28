"""
Flask-Decorators
----------------
A list of Flask decorator utilities not include in the origin flask project.

Links
`````
* `GitHub <https://github.com/kxxoling/flask-decorators>`_
"""
from setuptools import setup


setup(
    name='Flask-Decorators',
    version='0.0.1',
    url='https://github.com/kxxoling/flask-decorators',
    license='MIT',
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    description='A list of Flask decorator utilities'
                'not include in the origin flask project.',
    long_description=__doc__,
    packages=['flask_decorators'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
    ],
    test_suite='test_decorators.suite',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
