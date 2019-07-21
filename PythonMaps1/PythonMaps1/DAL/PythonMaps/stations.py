
import csv
import os
import uuid
import requests
from bs4 import BeautifulSoup as bs
from PythonMaps1.data.PythonMaps.db_factory import DbSessionFactory

from PythonMaps1.data.PythonMaps.stations import Stations


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
    def load_usgs_stations_by_huc(cls,huc ):
        # url = "http://waterdata.usgs.gov/MN/nwis/dv?referred_module=sw&huc_cd=" + huc + "&site_tp_cd=OC&site_tp_cd=OC-CO&site_tp_cd=ES&site_tp_cd=LK&site_tp_cd=ST&site_tp_cd=ST-CA&site_tp_cd=ST-DCH&site_tp_cd=ST-TS&index_pmcode_00060=1&sort_key=site_no&group_key=NONE&sitefile_output_format=html_table&column_name=agency_cd&column_name=site_no&column_name=station_nm&range_selection=date_range&begin_date=" + date_from + "&end_date=" + date_to + "&format=rdb&date_format=MM-DD-YYYY&rdb_compression=value&rdb_meas_compression=file&list_of_search_criteria=huc_cd_by_code%2Csite_tp_cd%2Crealtime_parameter_selection"

        url = "https://waterdata.usgs.gov/MN/nwis/inventory?huc_cd=" + huc + "&group_key=huc_cd&format=sitefile_output&sitefile_output_format=rdb&column_name=agency_cd&column_name=site_no&column_name=station_nm&column_name=site_tp_cd&column_name=lat_va&column_name=long_va&column_name=dec_lat_va&column_name=dec_long_va&column_name=coord_meth_cd&column_name=coord_acy_cd&column_name=coord_datum_cd&column_name=dec_coord_datum_cd&column_name=district_cd&column_name=state_cd&column_name=county_cd&list_of_search_criteria=huc_cd_by_code"

        print(url)
        request = requests.get(url)

        # requires
        #  $ pip install lxml
        soup = bs(request.text,"lxml")

        # soup.text is to get the returned text
        # split function, splits the entire text into different lines (using '\n') and stores in a list. You can define your own splitter.
        # each line is stored as an element in the allLines list.
        allLines = soup.text.split('\n')

        # for line in allLines: # you iterate through the list, and print the single lines

            # t = line.split()
            # if (t):
            #     if (t[0] != '#'):
            #         print( line )
            #         # print(":" + t[0])


        print('leaving DAL')

        # return the guid
        return allLines



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