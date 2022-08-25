from peewee import *

db = SqliteDatabase('test.db')

print('sql connected')

class test(Model):
    num = IntegerField()
    id = IntegerField()
    qvs = CharField()
    class Meta:
        database = db


db.connect()

def send_to_db(num, id, qvs):
    #user = test(id=id, qvs=qvs)
    test.get_or_create(num=num, id=id, qvs=qvs)

def checkusers(id):
    try:
        if str(test.get(test.id == id)) == str(id):
            return True
    except:
        return False

def check_base():
    #print(test.select())
    try:
        for person in test.select():
            number = person.num
            user = person.id
            qvestion = person.qvs
            #person.delete_instance()
            break
        return [number, user, qvestion]
    except:
        return False

        
def delete_from_base():
    for person in test.select():
        person.delete_instance()
        break
#print(check_base())
