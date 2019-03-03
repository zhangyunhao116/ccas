# CCAS

[![platform](https://img.shields.io/badge/python-3.5-green.svg)]()
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)]()

## Introduction

A simple utility used for convert object between camel-case and snake-case in python3.



## Installation

CCAS only running in python3 without third-party modules required. **Do not support python2**.

```
$ pip3 install ccas
```

Alternatively, you can just drop `ccas.py` file into your project—it is self-contained.



## QuickStart

Conversion supports only **dict**,**list**,**tuple**,**str** 



```python3
from ccas import camel_to_snake, snake_to_camel

"""Camel-case to snake-case."""
print(camel_to_snake('CamelCaseDemo'))
# camel_case_demo

print(camel_to_snake('checkAPIFramework'))
# check_api_framework

print(camel_to_snake({'CaseInsensitiveDict': 123}))
# {'case_insensitive_dict': 123}

print(camel_to_snake({'idCard': 'Not work in value.'}))
# {'id_card': 'Not work in value.'}

print(camel_to_snake({'allPeople': {'BoyAndrew': 'Value', 'GirlAlice': 'Value'}}))
# {'all_people': {'boy_andrew': 'Value', 'girl_alice': 'Value'}}


"""Snake-case to camel-case."""
print(snake_to_camel('snake_case_demo'))
# snakeCaseDemo

print(snake_to_camel('snake_case_demo', lower_first=False))
# SnakeCaseDemo

print(snake_to_camel('check_API_framework'))
# checkAPIFramework

print(snake_to_camel('__add_underscore_in_header_'))
# __addUnderscoreInHeader

print(snake_to_camel({'idCard': 'Not work in value.'}))
# {'idCard': 'Not work in value.'}

print(snake_to_camel({'all_people': {'boy_andrew': 'Value', 'girl_alice': 'Value'}}))
# {'allPeople': {'boyAndrew': 'Value', 'girlAlice': 'Value'}}

"""Others"""
print(camel_to_snake(None))
# None

print(camel_to_snake(True))
# True

print(camel_to_snake(123))
# 123

```



#### LRU API

Default maxsize = 64

```
"""With lru_cache"""
from ccas import (camel_to_snake_base_lru, camel_to_snake_lru,
                  loads_and_camel_to_snake_lru, loads_and_snake_to_camel_lru,
                  snake_to_camel_base_lru, snake_to_camel_lru)

```



## Benchmark

**Run benchmark.py**

Enviroment :

*macos 10.13.6 

*python3.7.1

*3.1 GHz Intel Core i7

```
camel_to_snake_base 100000 times:  0.38176393508911133
camel_to_snake_base_lru 100000 times:  0.0131072998046875 

camel_to_snake 100000 times:  0.6258797645568848
camel_to_snake_lru 100000 times:  0.20803093910217285 

loads_and_camel_to_snake 100000 times:  0.6583220958709717
loads_and_camel_to_snake_lru 100000 times:  0.012808084487915039 
```

