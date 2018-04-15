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
from sys import exit
import argparse

parser = argparse.ArgumentParser(
    description='Process commodities data and feed into MongoDB.')
parser.add_argument('--uri',
                    default='mongodb://localhost:27017',
                    help='Please provide a Mongo '
                    'connection URI for auth based DBs')

args = parser.parse_args()
host = args.uri
print("Connecting to Mongo via %s" % host)
conn = connect('AGMAPI', host=host)


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
print("Finished!")
