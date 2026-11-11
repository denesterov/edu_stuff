# work in progress
import re

with open('t24-28765.txt', 'rt') as f:
    S = f.read()

S = 'ABCCBC_DDBCABCCCAEBCEDDDDEEEBCEBC'

# BCBCxxBCxxBCzzzBC

# r = re.findall(r'((?:[ADEF]*BC[ADEF]*){3,3})', S)
r = re.findall(r'(?:[ADEF]*BC[ADEF]*){3,3}', S)

print(len(r))
print(r)
