import json

# load, loads, dump, dumps
var = '''
{
    "People": [
        {
            "name": "P1",
            "age": 27,
            "location": "l1"
        },
        {
            "name": "P2",
            "age": 28,
            "location": "l2"
        },
        {
            "name": "P3",
            "age": 28,
            "location": "l3"
        }
    ]
}
'''

my_var = json.loads(var)
print(type(var))
print(type(my_var))

my_dict = [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}, {"a": 7, "b": 8, "c": 9}]
my_json_var = json.dumps(my_dict)
print(type(my_dict))
print(type(my_json_var))

with open("my_json.json", "w") as op_json:
    json.dump(my_var, op_json, indent=4)

with open("my_json.json") as ip_json:
    my_data = json.load(ip_json)
    print(type(my_data))
    print(my_data)


