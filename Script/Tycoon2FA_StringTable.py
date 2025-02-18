import ast
import re


with open('ob.js', 'r') as f:
    js = f.read()

# Recover strings table
strings = re.search(r"""_0x159937 = \[(.*?)\];""", js, re.DOTALL)
strings = ast.literal_eval(f'[{strings.group(1)}]')

# Find all string lookup methods
lookups = {'_0xe042e'}
while True:
    n = len(lookups)
    for lookup_m in list(lookups):
        for m in re.finditer(f'const (\\S+) = {lookup_m};', js, re.DOTALL):
            lookups.add(m.group(1))
    if len(lookups) == n:
        break

# Recover all strings
for lookup_m in lookups:
    for m in re.finditer(f'{lookup_m}\\(0x([0-9a-f]+)\\)', js, re.DOTALL):
        s = strings[int(m.group(1), 16) - 458]
        js = js.replace(m.group(0), f'`{s}`')

print(js)
