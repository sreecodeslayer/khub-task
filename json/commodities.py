import json
from mongoengine import (
    connect,
    Document,
    StringField,
    IntField,
    ListField,
    DateTimeField,
    FloatField,
    ReferenceField
)
from mongoengine.errors import NotUniqueError

conn = connect('AGMAPI')


class Commidities(Document):
    types = ListField()
    name = StringField(unique=True)

    meta = {
        'indexes': ['name', 'types']
    }


with open('Agriculture Marketing_mar_4.json') as fp:
    data = json.load(fp)

comm_type = ''
for val in data:
    try:
        if len(val) == 1:
            comm_type = val[0].split(',')
        else:
            for comm in val:
                try:
                    commodity = Commidities(types=comm_type, name=comm)
                    commodity.save()
                except NotUniqueError:
                    print("commodity %s already feeded" % comm)
    except Exception as err:
        raise
