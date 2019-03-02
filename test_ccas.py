from functools import partial

import pytest
from ccas import (camel_to_snake, camel_to_snake_base, snake_to_camel,
                  snake_to_camel_base)


def test_camel_to_snake_base():
    fn = camel_to_snake_base

    with pytest.raises(AttributeError):
        fn(123)
    assert fn('@#$%') == '@#$%'
    assert fn('case') == 'case'
    assert fn('Case') == 'case'
    assert fn('caseInsensitive') == 'case_insensitive'
    assert fn('CaseInsensitive') == 'case_insensitive'
    assert fn('checkAPIFramework') == 'check_api_framework'
    assert fn('wordEN') == 'word_en'
    assert fn('WORK') == 'work'


def test_snake_to_camel_base():
    fn = snake_to_camel_base

    with pytest.raises(AttributeError):
        fn(123)

    assert fn('_id') == '_id'
    assert fn('__id') == '__id'
    assert fn('__id_card') == '__idCard'

    assert fn('OWN_id_card') == 'ownIdCard'
    assert fn('_OWN_id_card') == '_ownIdCard'

    assert fn('@#$%') == '@#$%'
    assert fn('case') == 'case'
    assert fn('Page') == 'page'
    assert fn('case_insensitive') == 'caseInsensitive'

    assert fn('case_insensitive_dict') == 'caseInsensitiveDict'
    assert fn('Case_insensitive_dict') == 'caseInsensitiveDict'

    # Test big camel-case.
    assert fn('_id', lower_first=False) == '_Id'
    assert fn('__id', lower_first=False) == '__Id'
    assert fn('__id_card', lower_first=False) == '__IdCard'

    assert fn('OWN_id_card', lower_first=False) == 'OWNIdCard'
    assert fn('_OWN_id_card', lower_first=False) == '_OWNIdCard'

    assert fn('@#$%', lower_first=False) == '@#$%'
    assert fn('case', lower_first=False) == 'Case'
    assert fn('Case', lower_first=False) == 'Case'
    assert fn('case_insensitive_dict', lower_first=False) == 'CaseInsensitiveDict'


def test_camel_to_snake():
    fn = camel_to_snake

    assert fn(123) == 123
    assert fn(257) == 257
    assert fn(None) is None
    assert fn(True) is True

    _test_dict_1 = {'Test': 'DoNotWork'}
    _test_dict_1_snake = {'test': 'DoNotWork'}
    _test_dict_2 = {'Test': {'CCASFrameWork': 'DoNotWork'}}
    _test_dict_2_snake = {'test': {'ccas_frame_work': 'DoNotWork'}}
    assert fn(_test_dict_1) == _test_dict_1_snake
    assert fn(_test_dict_2) == _test_dict_2_snake

    assert fn([_test_dict_1, _test_dict_2]) == [_test_dict_1_snake, _test_dict_2_snake]
    assert fn((_test_dict_1, _test_dict_2)) == (_test_dict_1_snake, _test_dict_2_snake)


def test_snake_to_camel():
    fn = partial(snake_to_camel, lower_first=True)

    assert fn(123) == 123
    assert fn(257) == 257
    assert fn(None) is None
    assert fn(True) is True

    _test_dict_1 = {'_test': 'do_not_work'}
    _test_dict_1_camel = {'_test': 'do_not_work'}
    _test_dict_2 = {'test_key': {'ccas_frame_work': 'do_not_work'}}
    _test_dict_2_camel = {'testKey': {'ccasFrameWork': 'do_not_work'}}
    assert fn(_test_dict_1) == _test_dict_1_camel
    assert fn(_test_dict_2) == _test_dict_2_camel

    assert fn([_test_dict_1, _test_dict_2]) == [_test_dict_1_camel, _test_dict_2_camel]
    assert fn((_test_dict_1, _test_dict_2)) == (_test_dict_1_camel, _test_dict_2_camel)

    fn = partial(snake_to_camel, lower_first=False)

    assert fn(123) == 123
    assert fn(257) == 257
    assert fn(None) is None
    assert fn(True) is True

    _test_dict_1 = {'_test': 'do_not_work'}
    _test_dict_1_camel = {'_Test': 'do_not_work'}
    _test_dict_2 = {'test_key': {'ccas_frame_work': 'do_not_work'}}
    _test_dict_2_camel = {'TestKey': {'CcasFrameWork': 'do_not_work'}}
    assert fn(_test_dict_1) == _test_dict_1_camel
    assert fn(_test_dict_2) == _test_dict_2_camel

    assert fn([_test_dict_1, _test_dict_2]) == [_test_dict_1_camel, _test_dict_2_camel]
    assert fn((_test_dict_1, _test_dict_2)) == (_test_dict_1_camel, _test_dict_2_camel)
