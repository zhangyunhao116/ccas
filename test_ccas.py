from functools import partial

import pytest

from ccas import (camel_to_snake, camel_to_snake_base, snake_to_camel,
                  snake_to_camel_base)


def test_camel_to_snake_base():
    fn = camel_to_snake_base

    # AttributeError
    with pytest.raises(AttributeError):
        fn(123)

    # Non-alphabetic
    assert fn('@#$%') == '@#$%'

    # All lower case
    assert fn('case') == 'case'

    # All upper case
    assert fn('CASE') == 'case'

    # First upper case
    assert fn('Case') == 'case'

    # First lower case but include upper case
    assert fn('caseInsensitive') == 'case_insensitive'

    # First upper case and include another upper case
    assert fn('CaseInsensitive') == 'case_insensitive'

    # Continuous upper case in front of string
    assert fn('TCPApi') == 'tcp_api'
    assert fn('TCPApi_') == 'tcp_api_'

    # Continuous upper case with first lower case
    assert fn('checkAPIFramework') == 'check_api_framework'
    assert fn('checkAPIFramework_') == 'check_api_framework_'

    # Continuous upper case with first upper case
    assert fn('CheckAPIFramework') == 'check_api_framework'
    assert fn('CheckAPIFramework_') == 'check_api_framework_'

    # Continuous upper case in the end
    assert fn('checkAPI') == 'check_api'
    assert fn('checkAPI_') == 'check_api_'

    # Continuous upper case
    # and prefixed with continuous non-alphabetic characters
    assert fn('___CASEInsensitive') == '___case_insensitive'

    # Continuous upper case in the end
    # and prefixed with continuous non-alphabetic characters
    assert fn('___CASE') == '___case'

    # First lower case but include upper case
    # and prefixed with continuous non-alphabetic characters
    assert fn('___caseInsensitive') == '___case_insensitive'

    # First upper case and include upper case which prefixed with "_"
    # and prefixed with continuous non-alphabetic characters
    assert fn('___Case_Insensitive') == '___case_insensitive'
    assert fn('___Case__Insensitive') == '___case__insensitive'
    assert fn('___Case__InsensitiveWord') == '___case__insensitive_word'
    assert fn('___Case__Insensitive_Word') == '___case__insensitive_word'

    """Snake case to snake case"""
    assert fn('snake_case') == 'snake_case'
    assert fn('_snake_case') == '_snake_case'
    assert fn('__snake_case') == '__snake_case'
    assert fn('__snake_case__') == '__snake_case__'
    assert fn('__snake__case__') == '__snake__case__'


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
