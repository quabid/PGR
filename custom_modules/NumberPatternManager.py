import re

# Regex integers
integer_pattern = re.compile('^[0-9]+$')
float_pattern = re.compile('^[0-9]+(\.[0-9]+){1}$')
