import time

from ccas import *

"""camel to snake"""
print('---------camel to snake---------')
t = time.time()
for i in range(100000):
    camel_to_snake_base('CamelToSnake')
print('camel_to_snake_base 100000 times: ', time.time() - t)

t = time.time()
for i in range(100000):
    camel_to_snake_base_lru('CamelToSnake')
print('camel_to_snake_base_lru 100000 times: ', time.time() - t, '\n')

t = time.time()
for i in range(100000):
    camel_to_snake({'CamelToSnake': 'NotWork'})
print('camel_to_snake 100000 times: ', time.time() - t)

t = time.time()
for i in range(100000):
    camel_to_snake_lru({'CamelToSnake': 'NotWork'})
print('camel_to_snake_lru 100000 times: ', time.time() - t, '\n')

t = time.time()
for i in range(100000):
    loads_and_camel_to_snake('{"CamelToSnake":"NotWork"}')
print('loads_and_camel_to_snake 100000 times: ', time.time() - t)

t = time.time()
for i in range(100000):
    loads_and_camel_to_snake_lru('{"CamelToSnake":"NotWork"}')
print('loads_and_camel_to_snake_lru 100000 times: ', time.time() - t, '\n')

"""snake to camel"""
print('---------snake to camel---------')
t = time.time()
for i in range(100000):
    snake_to_camel_base('snake_to_snake')
print('snake_to_camel_base 100000 times: ', time.time() - t)

t = time.time()
for i in range(100000):
    snake_to_camel_base_lru('snake_to_snake')
print('snake_to_camel_base_lru 100000 times: ', time.time() - t, '\n')

t = time.time()
for i in range(100000):
    snake_to_camel({'snake_to_snake': 'not_work'})
print('snake_to_camel 100000 times: ', time.time() - t)

t = time.time()
for i in range(100000):
    snake_to_camel_lru({'snake_to_snake': 'not_work'})
print('snake_to_camel_lru 100000 times: ', time.time() - t, '\n')

t = time.time()
for i in range(100000):
    loads_and_snake_to_camel('{"snake_to_camel":"not_work"}')
print('loads_and_snake_to_camel 100000 times: ', time.time() - t)

t = time.time()
for i in range(100000):
    loads_and_snake_to_camel_lru('{"snake_to_camel":"not_work"}')
print('loads_and_snake_to_camel_lru 100000 times: ', time.time() - t, '\n')
