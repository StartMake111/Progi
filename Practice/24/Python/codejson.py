import json
with open('in.json', 'r') as f:
    j = json.load(f)
vivod = []

for zadacha in j:
    userID = zadacha['userId']
    complited = zadacha['completed']

    check = None
    for cheloveck in vivod:
        if cheloveck['userId'] == userID:
            check = cheloveck
            break
    
    if check == None:
        check = {}
        check['userId'] = userID
        check['task_completed'] = 0
        vivod.append(check)
    if complited:
        check['task_completed'] += 1
with open('out.json', 'w') as f:
    f.write(json.dumps(vivod, indent=2))