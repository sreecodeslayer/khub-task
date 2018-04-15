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

from mongoengine.errors import (
    NotUniqueError,
    DoesNotExist
)
from datetime import date
import json

conn = connect('AGMAPI')


class Commidities(Document):
    types = ListField()
    name = StringField(unique=True)

    meta = {
        'indexes': ['name', 'types']
    }


class States(Document):
    name = StringField(unique=True)


class Mandis(Document):
    name = StringField()
    state = ReferenceField(States)

    meta = {
        'indexes': ['name', 'state']
    }


class Stocks(Document):
    commodity = ReferenceField(Commidities)
    state = ReferenceField(States)
    mandi = ReferenceField(Mandis)
    date = DateTimeField()
    modal_price = StringField()
    min_price = StringField()
    max_price = StringField()
    arrivals = StringField()

    meta = {
        'indexes': ['date', 'modal_price', 'min_price', 'max_price']
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
                    try:
                        state = States(name=crop_state)
                        state.save()
                    except NotUniqueError:
                        state = States.objects.get(name=crop_state)
            else:
                try:
                    commodity = Commidities(name=crop_name, types=['Cereals'])
                    commodity.save()
                except NotUniqueError:
                    commodity = Commidities.objects.get(name=crop_name)

                crop_doc = Stocks(
                    commodity=commodity, state=state)

                crop_mandi = det.get('market center')

                try:
                    '''
                    Query with state incl to avoid empty mandi being unique
                    across states
                    '''
                    mandi = Mandis.objects.get(name=crop_mandi, state=state)
                    crop_doc.mandi = mandi

                except DoesNotExist:
                    mandi = Mandis(name=crop_mandi, state=state)
                    mandi.save()
                    crop_doc.mandi = mandi

                crop_doc.arrivals = det.get('arrivals', 'NR')
                crop_doc.min_price = det.get('minimum price')
                crop_doc.max_price = det.get('maximum price')
                crop_doc.modal_price = det.get('modal price')
                crop_doc.date = date(2018, 4, day)
                crop_doc.save()
        except IndexError:
            print("end")
