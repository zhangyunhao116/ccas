# CCAS

[![platform](https://img.shields.io/badge/python-3.5-green.svg)]()
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)]()

## Introduction

A simple utility used for convert object between camel-case and snake-case in python3



## Installation

CCAS only running in python3 without third-party modules required. **Do not support python2**

```
$ pip3 install ccas
```

Alternatively, you can just drop `ccas.py` file into your project—it is self-contained



## QuickStart

Conversion supports only **dict**,**list**,**tuple**,**str**  if not return the input object itself

```
from ccas import (camel_to_snake, camel_to_snake_lru, snake_to_camel,
                  snake_to_camel_lru)

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

"""With LRU"""
print(camel_to_snake_lru('caseSensitive'))
# case_sensitive

print(snake_to_camel_lru('case_sensitive'))
# caseSensitive
```



## API

##### No cache API

```
camel_to_snake(obj:str or list or tuple or dict)

camel_to_snake_base(obj:str)

loads_and_camel_to_snake(obj:str or bytes)

loads_and_snake_to_camel(obj:str or bytes, lower_first=True)

snake_to_camel(obj:str or list or tuple or dict, lower_first=True)

snake_to_camel_base(obj:str, lower_first=True)
```



##### LRU API

Default maxsize=128 for API which do not begins with "loads_and"

If API begins with "loads_and" it's default maxsize=64

```
camel_to_snake_lru(obj:str or list or tuple or dict)

camel_to_snake_base_lru(obj:str)

loads_and_camel_to_snake_lru(obj:str or bytes)

loads_and_snake_to_camel_lru(obj:str or bytes, lower_first=True)

snake_to_camel_lru(obj:str or list or tuple or dict, lower_first=True)

snake_to_camel_base_lru(obj:str, lower_first=True)

```



## Benchmark

**Run benchmark.py**

Enviroment :

*macos 10.13.6 

*python3.7.1

*3.1 GHz Intel Core i7

```
---------camel to snake---------
camel_to_snake_base 100000 times:  0.4019458293914795
camel_to_snake_base_lru 100000 times:  0.011708259582519531 

camel_to_snake 100000 times:  0.635347843170166
camel_to_snake_lru 100000 times:  0.2188711166381836 

loads_and_camel_to_snake 100000 times:  0.7058398723602295
loads_and_camel_to_snake_lru 100000 times:  0.012506961822509766 

---------snake to camel---------
snake_to_camel_base 100000 times:  0.3905479907989502
snake_to_camel_base_lru 100000 times:  0.012526273727416992 

snake_to_camel 100000 times:  0.5907618999481201
snake_to_camel_lru 100000 times:  0.2144930362701416 

loads_and_snake_to_camel 100000 times:  0.6846120357513428
loads_and_snake_to_camel_lru 100000 times:  0.012782096862792969 
```

