import re


def replace_with_variables(input_string: str, pattern: str) -> str:
    """ "Searches for the pattern in the input string and replaces each match
         with dynamically created variables."

    Args:
        input_string: Takes an input string.
        pattern: Takes the pattern that will be searched for within the input_string.

    Returns: A string where, if found, the pattern matches have been replaced with dynamically created variables.

    """

    match_count = 0
    
    def replacement(m):
        nonlocal match_count
        match_count += 1
        var_name = f'placeholder_{match_count}'
        return var_name

    result = re.sub(pattern, replacement, input_string, flags=re.UNICODE)
    return result


test_string = 'Hello ###world###!, Hello ###foo###!, Hello ###bar###!'
test_pattern = r'###[\w]+###'

print(replace_with_variables(test_string, test_pattern))
