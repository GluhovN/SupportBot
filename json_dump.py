import json

print('json connected')

def new_admin(id):
    with open('admins.json') as json_file:
        data = json.load(json_file)
        if id in data['admins']:
            return False
        else:
            data['admins'].append(id)
            with open('admins.json', 'w+') as outfile:
                json.dump(data, outfile)
            return True

def get_admins():
    with open('admins.json') as json_file:
        data = json.load(json_file)
        if data['admins'] is not None:
            try:
                data['admins'][0]
                return str(data['admins']).replace('[', '').replace(']', '')
            except:
                return 'Список Админов пуст'
        else:
            return 'Список Админов пуст'

def delete_admin(id):
    with open('admins.json') as json_file:
        data = json.load(json_file)
        if id in data['admins']:
            data['admins'].remove(id)
            with open('admins.json', 'w') as outfile:
                json.dump(data, outfile)
            return True
        else:
            return False

def change_number():
    with open('kostil.json') as json_file1:
        data1 = json.load(json_file1)
        data1['number'] = data1['number'] + 1
        with open('kostil.json', 'w') as json_file1:
            json.dump(data1, json_file1)

def get_number():
    with open('kostil.json') as json_file1:
        data1 = json.load(json_file1)
    return data1['number']

def work_in_porcess(id, number, q_id):
    with open('kostil.json') as json_file1:
        data1 = json.load(json_file1)
        with open('kostil.json', 'w') as json_file1:
            data1[id] = [number, q_id]
            json.dump(data1, json_file1)

def qvs_id(id):
    with open('kostil.json') as json_file1:
        data1 = json.load(json_file1)
    return data1[id][1]

def get_txt():
    with open('text.json', encoding='utf-8') as json_file1:
        data1 = json.load(json_file1)
    return data1['intro_message']

def change_txt(text):
     with open('text.json') as json_file1:
        data1 = json.load(json_file1)
        with open('text.json', 'w', encoding='utf-8') as json_file1:
                data1['intro_message'] = str(text)
                json.dump(data1, ensure_ascii=False, fp=json_file1)
        