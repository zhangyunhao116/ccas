from functools import lru_cache, partial

try:
    import ujson as json
except ImportError:
    import json

__all__ = ('camel_to_snake', 'snake_to_camel', 'camel_to_snake_base',
           'snake_to_camel_base', 'loads_and_camel_to_snake', 'loads_and_snake_to_camel',
           'camel_to_snake_lru', 'snake_to_camel_lru', 'camel_to_snake_base_lru',
           'snake_to_camel_base_lru', 'loads_and_camel_to_snake_lru', 'loads_and_snake_to_camel_lru')


def camel_to_snake_base(string: str) -> str:
    """Base function to convert an camel-case string to snake-case string."""
    res = []

    # For speed up, we don't check type here, but raise a AttributeError.
    byte = string.encode('ascii')

    max_index = len(byte)

    _index = 0

    while _index < max_index:
        if 65 <= byte[_index] <= 90:
            # Upper case.
            if _index != 0:
                res.append(95)  # Add char "_".
            res.append(byte[_index] + 32)
            _index += 1
            while _index < max_index and 65 <= byte[_index] <= 90:
                # Check if next char also upper case.
                if _index + 1 < max_index:
                    # Have next two char
                    if 65 <= byte[_index + 1] <= 90:
                        # Next two char all upper case.
                        res.append(byte[_index] + 32)
                        _index += 1
                    else:
                        # Next char is upper case, but the next char's next char is not.
                        break
                else:
                    # Next char is last one.
                    res.append(byte[_index] + 32)
                    _index += 1
                    break
        else:
            # Lower case or others.
            res.append(byte[_index])
            _index += 1

    res = bytearray(res).decode('ascii')

    return res


def snake_to_camel_base(string: str, lower_first=True) -> str:
    """Base function to convert an snake-case string to camel-case string."""
    res = []

    # For speed up, we don't check type here, but raise a AttributeError.
    byte = string.encode('ascii')

    max_index = len(byte)

    _index = 0

    while _index < max_index and byte[_index] == 95:
        # Add char "_" in header of string.
        res.append(95)
        _index += 1
    if lower_first:
        while _index < max_index:
            # Lower first word.
            if 65 <= byte[_index] <= 90:  # This char is Upper case.
                res.append(byte[_index] + 32)
                _index += 1
            else:
                break
    else:
        # Try upper first case.
        if 97 <= byte[_index] <= 122:
            # Char is lower case.
            res.append(byte[_index] - 32)
            _index += 1

    while _index < max_index:
        if byte[_index] == 95:
            # Catch char "_".
            # Remove this char "_" and find next char != "_"
            _index += 1
            while _index < max_index and byte[_index] == 95:
                _index += 1
            # Then try to upper case this char(if it is lower).
            if not (_index < max_index):
                break  # Last char is underscore.
            if 97 <= byte[_index] <= 122:
                # Char is lower case.
                res.append(byte[_index] - 32)
                _index += 1
            else:
                # May be upper case or others.
                res.append(byte[_index])
                _index += 1
        else:
            # Catch lower case or others.
            res.append(byte[_index])
            _index += 1

    res = bytearray(res).decode('ascii')

    return res


def loads_and_camel_to_snake(raw_json: str or bytes):
    """WARNING: This method may cause some memory problems."""
    return camel_to_snake(json.loads(raw_json))


def loads_and_snake_to_camel(raw_json: str or bytes, lower_first=True):
    """WARNING: This method may cause some memory problems."""
    return snake_to_camel(json.loads(raw_json), lower_first=lower_first)


def _convert_json(obj, fn: snake_to_camel_base or camel_to_snake_base):
    if isinstance(obj, list):
        return [_convert_json(i, fn) for i in obj]
    elif isinstance(obj, tuple):
        return tuple((_convert_json(i, fn) for i in obj))
    elif isinstance(obj, dict):
        return {fn(k): _convert_json(v, fn) for k, v in obj.items()}
    return obj


def _convert_api(obj, fn, **kwargs):
    fn = partial(fn, **kwargs)
    if isinstance(obj, str):
        return fn(obj)
    elif isinstance(obj, (list, tuple, dict)):
        return _convert_json(obj, fn)
    else:
        return obj


camel_to_snake = partial(_convert_api, fn=camel_to_snake_base)
snake_to_camel = partial(_convert_api, fn=snake_to_camel_base)

"""LRU API"""
camel_to_snake_base_lru = lru_cache(maxsize=64)(camel_to_snake_base)
camel_to_snake_lru = partial(_convert_api, fn=camel_to_snake_base_lru)

snake_to_camel_base_lru = lru_cache(maxsize=64)(snake_to_camel_base)
snake_to_camel_lru = partial(_convert_api, fn=snake_to_camel_base_lru)

loads_and_camel_to_snake_lru = lru_cache(maxsize=64)(loads_and_camel_to_snake)
loads_and_snake_to_camel_lru = lru_cache(maxsize=64)(loads_and_snake_to_camel)
