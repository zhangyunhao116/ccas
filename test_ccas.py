import pytest
from ccas import camel_to_snake_base, snake_to_camel_base


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
