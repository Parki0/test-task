import json
import sys
paths = sys.argv[1:]
print(paths)
 # A:\common textbook 2\code\job testing\
with open(paths[0],'r') as f:
    tests = json.loads(f.read())['tests']

with open(paths[1],'r') as f:
    values = json.loads(f.read())['values'] 

def get_value(id):
    for v in values:
        if v['id'] == id:
            return v['value']

def assign_values(tests):
    for test in tests:

        test['value'] = get_value(test['id'])

        if 'values' in test.keys():
            assign_values(test['values'])

assign_values(tests)

# print('======')
# for test in tests:
#     print(test)
#     print('----')

out = json.dumps({ 'tests': tests }, sort_keys=True, indent=4)


with open('report.json', 'w') as f:
    f.write(out)