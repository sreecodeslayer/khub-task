from mongoengine import (
    connect,
    Document,
    StringField,
    IntField,
    DateTimeField,
    FloatField,
    ReferenceField
)

from mongoengine.errors import NotUniqueError
from datetime import date
import json

conn = connect('AGMAPI')


class Commidities(Document):
    type = StringField()
    name = StringField(unique=True)

    meta = {
        'index': ['name', 'type']
    }


class Stocks(Document):
    commodity = ReferenceField(Commidities)
    state = StringField()
    mandi = StringField()
    date = DateTimeField()
    modal_price = StringField()
    min_price = StringField()
    max_price = StringField()
    arrivals = StringField()

    meta = {
        'index': ['state', 'date', 'modal_price', 'min_price', 'max_price']
    }


for day in [1, 2, 3, 6, 7]:
    print("Feeding day : %s" % day)
    with open('Agriculture Marketing_mar_%s.json' % day) as fp:
        data = json.load(fp)
        data = data[1:]
    crop_state = ''
    crop_name = ''
    commodity = None
    crop_doc = None
    for (i, det) in enumerate(data):
        try:
            if len(det) == 1:
                crop = {}
                if len(data[i+1]) == 1:
                    crop_name = det.get('market center')
                    crop_state = data[i+1].get('market center')
                else:
                    crop_state = det.get('market center')
            else:
                try:
                    commodity = Commidities(name=crop_name, type='Cereals')
                    commodity.save()
                except NotUniqueError:
                    commodity = Commidities.objects.get(name=crop_name)

                crop_doc = Stocks(
                    commodity=commodity, state=crop_state)
                crop_doc.mandi = det.get('market center')
                crop_doc.arrivals = det.get('arrivals', 'NR')
                crop_doc.min_price = det.get('minimum price')
                crop_doc.max_price = det.get('maximum price')
                crop_doc.modal_price = det.get('modal price')
                crop_doc.date = date(2018, 4, day)
                crop_doc.save()
        except IndexError:
            print("end")
