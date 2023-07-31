"""
Write a function to convert a snake case string to camel case string.
"""

def snake_to_camel(word):
        assert isinstance(word, str), "invalid inputs" # $_CONTRACT_$
        assert len(word) > 0, "invalid inputs" # $_CONTRACT_$
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))



assert snake_to_camel('python_program')=='PythonProgram'
assert snake_to_camel('python_language')==('PythonLanguage')
assert snake_to_camel('programming_language')==('ProgrammingLanguage')
