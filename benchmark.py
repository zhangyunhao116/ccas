import time

from ccas import *

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
