import os
import sys

from setuptools import find_packages, setup

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('pip3 install twine')
    os.system('pip3 install wheel')
    os.system('python3 setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    os.system('rm -rf build dist .egg ccas.egg-info')
    sys.exit()

# 'setup.py test' shortcut.
if sys.argv[-1] == 'test':
    os.system('pip3 install pytest')
    os.system('pytest test_ccas.py')
    sys.exit()

# 'setup.py isort' shortcut.
if sys.argv[-1] == 'isort':
    os.system('isort -rc *.py')
    sys.exit()

# 'setup.py flake8' shortcut.
if sys.argv[-1] in ('flake8', 'flake'):
    os.system('flake8 --ignore=E501 *.py')
    sys.exit()

setup(
    name='ccas',
    version='0.0.1',

    author='ZYunH',
    author_email='zyunhjob@163.com',

    description='ccas allows you to convert string between camel-case and snake-case in python3.',
    long_description='ccas(Convert between Camel-case And Snake-case)'
                     'allows you to convert string between camel-case and snake-case in python3.',
    keywords='email python3 package',

    url='https://github.com/ZYunH/ccas',
    license="MIT Licence",
    py_modules=['ccas'],

    platforms='all',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),

    packages=find_packages(),
    include_package_data=True,

)
