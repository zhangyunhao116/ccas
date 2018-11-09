from functools import partial

__all__ = ('camel_to_snake', 'snake_to_camel')


def camel_to_snake_base(string: str) -> str:
    """Base function to convert an camel-case string to snake-case string."""
    res = bytearray()

    # For speed up, wo don't check type here, but raise a AttributeError.
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

    res = res.decode('ascii')

    return res


def snake_to_camel_base(string: str, lower_first=True) -> str:
    """Base function to convert an snake-case string to camel-case string."""
    res = bytearray()

    # For speed up, wo don't check type here, but raise a AttributeError.
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

    res = res.decode('ascii')

    return res


def convert_json(obj, fn: snake_to_camel_base or camel_to_snake_base):
    if isinstance(obj, list):
        return [convert_json(i, fn) for i in obj]
    elif isinstance(obj, tuple):
        return tuple((convert_json(i, fn) for i in obj))
    elif isinstance(obj, dict):
        return {fn(k): convert_json(v, fn) for k, v in obj.items()}
    return obj


def camel_to_snake(obj):
    fn = camel_to_snake_base
    if isinstance(obj, str):
        return fn(obj)
    elif isinstance(obj, (list, tuple, dict)):
        return convert_json(obj, fn)
    else:
        raise TypeError('obj excepted type in ("str","tuple","list","dict") got {}'.format(type(obj)))


def snake_to_camel(obj, lower_first=True):
    fn = partial(snake_to_camel_base, lower_first=lower_first)
    if isinstance(obj, str):
        return fn(obj)
    elif isinstance(obj, (list, tuple, dict)):
        return convert_json(obj, fn)
    else:
        raise TypeError('obj excepted type in ("str","tuple","list","dict") got {}'.format(type(obj)))
