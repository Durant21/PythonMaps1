
import csv
import os
import uuid

from PythonMaps1.data.db_factory import DbSessionFactory
from PythonMaps1.data.HUCs import HUCs
from dateutil.parser import parse


class Repository:
    @classmethod
    def add_huc(cls, ts):
        # cls.__load_data()
        # key = str(uuid.uuid4())
        # car_data['id'] = key
        # cls.__car_data[key] = car_data
        #
        # return car_data

        try:


            session1 = DbSessionFactory.create_session()

            a = 12
            db_hucs = HUCs()
            db_hucs.huc_id = ts.huc_id
            db_hucs.state1 = ts.state1  #parse(ts.TSDateTime)  # parse(teacher.certdate)
            db_hucs.state2 = ts.state2
            db_hucs.huc_name = ts.huc_name
            db_hucs.desc = ts.desc
            # db_hucs.uuid1 = ts.uuid1
            # db_car.image = car.image if car.image else random.choice(cls.__fake_image_url)
            #db_ts.year = ts.year
            # db_car.teacherId = int(teacher.year)
            #db_ts.price = int( ts.price )


            session1.add( db_hucs )

            session1.commit()

            return db_hucs

        except Exception as e:
            print( e )  # for the repr
        # ...     print 'My exception occurred, value:', e.value


class hucs_data:
    __hucs_data={}

    @classmethod
    def all_hucs_csv(cls, limit=None):
        __hucs_data = {}
        cls.__load_data()
        hucs = list( cls.__hucs_data.values() )
        if limit:
            hucs = hucs[:limit]
            return hucs
        else:
            return hucs

    @classmethod
    def hucs_by_state(cls, state_name,limit):
        # cls.__load_data()
        # return cls.__car_data.get(car_id)

        session = DbSessionFactory.create_session()

        hucs1 = session.query(HUCs).filter(HUCs.state2 == state_name).all()
        # hucs2 = session.query.distinct( HUCs.huc_name ).limit( 5 )

        hucs = session.query( HUCs.huc_name ). \
            filter( HUCs.state2 == state_name ). \
            distinct(HUCs.huc_name). \
            all()

        #.first()

        session.close()

        return hucs


    @classmethod
    def __load_data(cls):
        if cls.__hucs_data:
            return

        file = os.path.join(
            os.path.dirname( __file__ ),
            '../data/HUCs_csv.csv'
        )

        with open( file, "r" ) as f:
            # convert file to list
            test = f.read().splitlines()

            print("len " + str(len(test)))

        # print( test )

        fileHandle = open( file, 'r' )

        for line in fileHandle:
            fields = line.split( '|' )

            for u in fields:
                print("u=" + u )
                row = {}
                key = str( uuid.uuid4() )
                row['id'] = key
                row['state1'] = fields[1]
                row['state2'] = fields[2]
                row['huc'] = fields[3]
                row['desc'] = fields[4]
                cls.__hucs_data[key] = row

            print( fields[0] )  # prints the first fields value
            print( fields[1] )  # prints the second fields value

        fileHandle.close()



        # with open( file, 'r', encoding='utf-8' ) as fin:
        #     # brand,name,price,year,damage,last_seen
        #     reader = csv.DictReader( fin )
        #     for row in reader:
        #         key = str( uuid.uuid4() )
        #         row['id'] = key
        #         cls.__hucs_data[key] = row