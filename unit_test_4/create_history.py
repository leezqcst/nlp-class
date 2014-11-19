import json
from pprint import pprint


def get_tuples():
    history_list = []
    f = open("all_data.json")
    json_data = json.load(f)
    for x in json_data['root']:
        data = x['data']
        for y in data:
            updates = y['updates']
            for z in range(len(updates)):
                if (updates[z]['tag'] == 'Model'):
                    updates[z]['tag'] = 'Family'
                if (updates[z]['tag'] == 'Family' or updates[z]['tag'] == 'Org'):
                    pass
                else:
                    updates[z]['tag'] = 'Other'

                if (z == 0):
                    history_list.append([None, None, updates[z]['word'],updates[z]['tag'],  z])
                elif (z == 1):
                    history_list.append([None, updates[z -1]['tag'], updates[z]['word'], updates[z]['tag'], z])
                else:
                    history_list.append([updates[z - 2]['tag'], updates[z - 1]['tag'], updates[z]['word'], updates[z]['tag'],  z])
    return history_list

