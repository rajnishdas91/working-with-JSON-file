# The goal is to extract name of states and their abbreviation from sample_states file


import json
#opening the sample file and loading json data
with open('sample_states.json') as f1:
    json_obj=json.load(f1)
    # print(json_obj)
# print(json.dumps(json_obj, indent=4)) #----To print the json data in a readable format------

#iterate the json list and perform modification
for state in json_obj['states']:
    print(state["name"], state["abbreviation"])
    del state["area_codes"]
# print(json_obj)

#write the final json text to a new file
with open('states_output.json', 'w') as f2:
    json.dump(json_obj,f2,indent=4)