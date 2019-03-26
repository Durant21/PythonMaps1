
import csv
import os
import uuid
from PythonMaps1.data.db_factory import DbSessionFactory
from PythonMaps1.data.stations import Stations

from PythonMaps1.data.stations import Stations


class stations_data:
    __stations_centralNM_data={}
    __stations_usgs_data = {}

    @classmethod
    def add_station(cls, st):
        # cls.__load_data()
        # key = str(uuid.uuid4())
        # car_data['id'] = key
        # cls.__car_data[key] = car_data
        #
        # return car_data

        try:


            session1 = DbSessionFactory.create_session()

            a = 12
            db_stations = Stations()
            db_stations.station_id = st.station_id
            db_stations.OrganizationIdentifier = st.OrganizationIdentifier  #parse(ts.TSDateTime)  # parse(teacher.certdate)
            db_stations.OrganizationFormalName = st.OrganizationFormalName
            db_stations.MonitoringLocationTypeName = st.MonitoringLocationTypeName
            db_stations.HUCEightDigitCode = st.HUCEightDigitCode

            db_stations.LatitudeMeasure = st.LatitudeMeasure
            db_stations.LongitudeMeasure = st.LongitudeMeasure
            db_stations.ProviderName = st.ProviderName

            # db_hucs.uuid1 = ts.uuid1
            # db_car.image = car.image if car.image else random.choice(cls.__fake_image_url)
            #db_ts.year = ts.year
            # db_car.teacherId = int(teacher.year)
            #db_ts.price = int( ts.price )


            session1.add( db_stations )

            session1.commit()

            return db_stations

        except Exception as e:
            print( e )  # for the repr
        # ...     print 'My exception occurred, value:', e.value

    @classmethod
    def all_stations_usgs_csv(cls,  limit=None):
        __stations_data = {}
        cls.__load_usgs_data()
        stations = list( cls.__stations_usgs_data.values() )

        # t = list(cls.__stations_usgs_data.get( "Interpolated from MAP." ))

        if limit:
            stations = stations[:limit]
            return stations
        else:
            return stations

    @classmethod
    def __load_usgs_data(cls):
        if cls.__stations_usgs_data:
            return

        file = os.path.join(
            os.path.dirname( __file__ ),
            '../data/station.csv'
        )

        with open( file, 'r', encoding='utf-8' ) as fin:
            # brand,name,price,year,damage,last_seen
            reader = csv.DictReader( fin )
            for row in reader:
                key = str( uuid.uuid4() )
                row['id'] = key
                cls.__stations_usgs_data[key] = row

    @classmethod
    def stations_by_huc(cls, huc_id,limit):
        # cls.__load_data()
        # return cls.__car_data.get(car_id)

        session = DbSessionFactory.create_session()

        stations = session.query(Stations).filter(Stations.HUCEightDigitCode == huc_id).all()#.first()

        session.close()

        return stations


    @classmethod
    def all_stations_centralNM_csv(cls, huc, limit=None):
        __stations_data = {}
        cls.__load_centralNM_data()
        stations = list( cls.__stations_centralNM_data.values() )
        if limit:
            stations = stations[:limit]
            return stations
        else:
            return stations

    @classmethod
    def __load_centralNM_data(cls):
        if cls.__stations_centralNM_data:
            return

        file = os.path.join(
            os.path.dirname( __file__ ),
            '../data/Stations_CentralNM.csv'
        )

        with open( file, 'r', encoding='utf-8' ) as fin:
            # brand,name,price,year,damage,last_seen
            reader = csv.DictReader( fin )
            for row in reader:
                key = str( uuid.uuid4() )
                row['id'] = key
                cls.__stations_centralNM_data[key] = row