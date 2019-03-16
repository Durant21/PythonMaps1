import sys
import csv
import os
import uuid
import random

from PythonMaps1.data.TSData import TSData
from dateutil.parser import parse
from PythonMaps1.data.db_factory import DbSessionFactory


class Repository:
    @classmethod
    def add_ts(cls, ts):
        # cls.__load_data()
        # key = str(uuid.uuid4())
        # car_data['id'] = key
        # cls.__car_data[key] = car_data
        #
        # return car_data

        try:


            session1 = DbSessionFactory.create_session()

            a = 12
            db_ts = TSData()
            db_ts.ts_id = ts.ts_id
            db_ts.TSDateTime = parse(ts.TSDateTime)  # parse(teacher.certdate)
            db_ts.agency_cd = ts.agency_cd
            db_ts.HydroCode = ts.HydroCode
            db_ts.TSValue = ts.TSValue
            db_ts.uuid1 = ts.uuid1
            # db_car.image = car.image if car.image else random.choice(cls.__fake_image_url)
            #db_ts.year = ts.year
            # db_car.teacherId = int(teacher.year)
            #db_ts.price = int( ts.price )


            session1.add( db_ts )

            session1.commit()

            return db_ts

        except Exception as e:
            print( e )  # for the repr
        # ...     print 'My exception occurred, value:', e.value

