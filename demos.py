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
