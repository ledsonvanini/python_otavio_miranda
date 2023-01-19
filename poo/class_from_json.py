
import json
from from_class_to_json import PATH, Pessoa

with open(PATH, 'r', encoding='utf8') as file:
    person = json.load(file)
    p1 = Pessoa(**person[0])
    p2 = Pessoa(**person[1])
    p3 = Pessoa(**person[2])

    print(p1.get_idade())