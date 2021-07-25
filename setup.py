#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pandas>=1.1.0', 'numpy>=1.19.0', 'sklearn', 'seaborn', 'matplotlib', 'plotly', 'scipy', 'dvc']

test_requirements = ['pytest>=3', ]

setup(
    author="Daniel Zelalem",
    email="danielzelalemheru@gmail.com",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A/B hypothesis testing for an advertising company.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='scripts, sequential ab test, sprt, classic ab test, classic ab, AB testing, ab test, machine learning ab test, logistic regression, decision tree, xgboost',
    name='smartAd_abtest',
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/daniEL2371/abtest-mlops',
    version='0.1.0',
    zip_safe=False,
)