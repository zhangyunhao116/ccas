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
    """Base function to convert a camel-case string to snake-case string."""
    res = []

    # For speed up, we don't check type here, but raise a AttributeError here
    byte = string.encode('ascii')

    max_index = len(byte)

    _index = 0

    # Append all non-alphabetic characters in front of string
    # for purpose of find the first letter
    while _index < max_index and not (65 <= byte[_index] <= 90) and not (97 <= byte[_index] <= 122):
        res.append(byte[_index])
        _index += 1

    # If first letter is upper case, do not need begins with "_"
    if _index < max_index and 65 <= byte[_index] <= 90:

        # Convert it to lower case and check next char
        res.append(byte[_index] + 32)
        _index += 1

        # Check if next char also upper case
        while _index < max_index and 65 <= byte[_index] <= 90:
            if _index + 1 < max_index:
                # There are next two chars
                if 65 <= byte[_index + 1] <= 90:
                    # Next two char are all upper case
                    #  we just lower the first one and append
                    # it to result (in this condition
                    # it must not the first upper case
                    # in a camel-case word)
                    res.append(byte[_index] + 32)
                    _index += 1
                elif not (97 <= byte[_index + 1] <= 122):
                    # The first one is upper case but
                    # next one is non-alphabetic character
                    # so lower first one and append it
                    res.append(byte[_index] + 32)
                    res.append(byte[_index + 1])
                    _index += 2
                else:
                    # The first one is upper case and
                    # next one is lower case
                    # it means that first one is
                    # the first upper case in camel-case
                    # word
                    if res[-1] != 95:
                        res.append(95)
                    res.append(byte[_index] + 32)
                    res.append(byte[_index + 1])
                    _index += 2
                    break
            else:
                # Next char is last one and it is upper case
                # so lower it and append to the result
                res.append(byte[_index] + 32)
                _index += 1
                break

    while _index < max_index:
        if 65 <= byte[_index] <= 90:
            # Upper case, we should add
            # "_" in front of it normally

            # If last one char in the result
            # is "_" we don't add extra
            # "_" in this condition
            if res[-1] != 95:
                res.append(95)

            res.append(byte[_index] + 32)
            _index += 1

            # Check if next char also upper case
            while _index < max_index and 65 <= byte[_index] <= 90:
                if _index + 1 < max_index:
                    # There are next two chars
                    if 65 <= byte[_index + 1] <= 90:
                        # Next two char are all upper case
                        #  we just lower the first one and append
                        # it to result (in this condition
                        # it must not the first upper case
                        # in a camel-case word)
                        res.append(byte[_index] + 32)
                        _index += 1
                    elif not (97 <= byte[_index + 1] <= 122):
                        # The first one is upper case but
                        # next one is non-alphabetic character
                        # so lower first one and append it
                        res.append(byte[_index] + 32)
                        res.append(byte[_index + 1])
                        _index += 2
                    else:
                        # The first one is upper case and
                        # next one is lower case
                        # it means that first one is
                        # the first upper case in camel-case
                        # word
                        if res[-1] != 95:
                            res.append(95)
                        res.append(byte[_index] + 32)
                        res.append(byte[_index + 1])
                        _index += 2
                        break
                else:
                    # Next char is last one and it is upper case
                    # so lower it and append to the result
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
    """Base function to convert a snake-case string to camel-case string."""
    res = []

    # For speed up, we don't check type here, but raise a AttributeError here
    byte = string.encode('ascii')

    max_index = len(byte)

    _index = 0

    # Add all "_" in front of string
    while _index < max_index and byte[_index] == 95:
        res.append(95)
        _index += 1

    # Add all non-alpha characters exclude "_"
    # for purpose of find the first letter
    while _index < max_index and not (65 <= byte[_index] <= 90) and not (97 <= byte[_index] <= 122):
        if byte[_index] == 95:
            _index += 1
            continue
        res.append(byte[_index])
        _index += 1

    if lower_first:
        # Lower first word if possible
        while _index < max_index:
            if 65 <= byte[_index] <= 90:
                res.append(byte[_index] + 32)
                _index += 1
            else:
                break
    else:
        # Upper first character if possible (just once)
        if _index < max_index and 97 <= byte[_index] <= 122:
            # Char is lower case.
            res.append(byte[_index] - 32)
            _index += 1

    while _index < max_index:
        if byte[_index] == 95:
            # Catch char "_" then skip it
            _index += 1

            # Ignore all following "_"
            while _index < max_index and byte[_index] == 95:
                _index += 1

            # Break if last char is underscore
            if _index >= max_index:
                break

            # Then try to upper case first letter
            if 97 <= byte[_index] <= 122:
                # Char is lower case.
                res.append(byte[_index] - 32)
                _index += 1
            else:
                # May be upper case or others just append it
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
