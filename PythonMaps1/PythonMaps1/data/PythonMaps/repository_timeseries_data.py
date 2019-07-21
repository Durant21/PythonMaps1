import csv
import os
import uuid


class Repository_timeseries_data:
    __stations_data={}

    @classmethod
    def all_timeseries_data(cls,limit=None):
        cls.__load_data()
        stations=list(cls.__stations_data.values())
        if limit:
            stations=stations[:limit]
            return stations

    @classmethod
    def __load_data(cls):
        if cls.__stations_data:
            return

        file = os.path.join(
            os.path.dirname(__file__),
            'timeseries_8343500.csv'
        )

        with open(file,'r',encoding='utf-8') as fin:
            #brand,name,price,year,damage,last_seen
            reader=csv.DictReader(fin)
            for row in reader:
                key=str(uuid.uuid4())
                row['id']=key
                cls.__stations_data[key]=row
