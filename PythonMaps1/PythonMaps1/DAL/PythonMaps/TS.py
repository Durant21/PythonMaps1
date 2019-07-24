from PythonMaps1.data.PythonMaps.TSData import TSData

from dateutil.parser import parse
from PythonMaps1.data.PythonMaps.db_factory import DbSessionFactory
import sqlite3
import os
import PythonMaps1

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
            db_ts.site_no = ts.site_no
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



    @classmethod
    def update_timeseries(cls, ts_rec):
        # key = person_data['id']
        # cls.__people_data[key] = person_data
        #
        # return person_data
        # id,name,title,company,email,url1,url2,description, address, city,state,img1

        session = DbSessionFactory.create_session()

        db_ts = session.query(TSData).filter(TSData.ts_id == ts_rec.ts_id).first()
        # db_car.last_seen = parse(car_data.last_seen)
        db_ts.Transferable = 'true'

        session.commit()

        return db_ts


    @classmethod
    def update_ts(cls,task):
        working_folder = os.path.dirname(PythonMaps1.__file__)
        file = os.path.join(working_folder,'db','USGS.sqlite')
        conn_string = 'sqlite:///' + file

        conn = sqlite3.connect(file)
        #
        # sql = ''' INSERT INTO Sections(doc_text, date_in)
        #            VALUES(?,?) '''


        sql = ''' UPDATE TSData SET Transferable = 'true'  WHERE uuid1 = (?) '''

        cur = conn.cursor()
        # cur.execute(sql, (task,))
        cur.execute( "UPDATE TSData SET Transferable = 'false' WHERE uuid1 = ?", ("13258723-5252-4be7-8bc4-a23d09891cd3",) )
        lrowid = cur.lastrowid

        conn.close()
        return lrowid