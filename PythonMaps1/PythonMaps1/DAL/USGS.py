import requests
from bs4 import BeautifulSoup as bs
from PythonMaps1.data.db_factory import DbSessionFactory

class USGS_data:
    __stations_data={}

    @classmethod
    def usgs_load_by_HUC(cls, huc, limit=None):
        url = "https://www.amfiindia.com/spages/NAVAll.txt?t=23052017073640"

        url = "http://waterdata.usgs.gov/MN/nwis/dv?referred_module=sw&"
        "huc_cd=04010101&site_tp_cd=OC&site_tp_cd=OC-CO&site_tp_cd=ES&"
        "site_tp_cd=LK&site_tp_cd=ST&site_tp_cd=ST-CA&site_tp_cd=ST-DCH&"
        "site_tp_cd=ST-TS&index_pmcode_00060=1&sort_key=site_no&"
        "group_key=NONE&sitefile_output_format=html_table&column_name=agency_cd&"
        "column_name=site_no&column_name=station_nm&range_selection=date_range&"
        "begin_date=2006-4-24&end_date=2006-5-24&format=rdb&date_format=YYYY-MM-DD&"
        "rdb_compression=value&rdb_meas_compression=file&list_of_search_criteria=huc_cd_by_code%"
        "2Csite_tp_cd%2Crealtime_parameter_selection"

        url = "http://waterdata.usgs.gov/MN/nwis/dv?referred_module=sw&huc_cd=04010101&site_tp_cd=OC&site_tp_cd=OC-CO&site_tp_cd=ES&site_tp_cd=LK&site_tp_cd=ST&site_tp_cd=ST-CA&site_tp_cd=ST-DCH&site_tp_cd=ST-TS&index_pmcode_00060=1&sort_key=site_no&group_key=NONE&sitefile_output_format=html_table&column_name=agency_cd&column_name=site_no&column_name=station_nm&range_selection=date_range&begin_date=2006-4-24&end_date=2006-5-24&format=rdb&date_format=YYYY-MM-DD&rdb_compression=value&rdb_meas_compression=file&list_of_search_criteria=huc_cd_by_code%2Csite_tp_cd%2Crealtime_parameter_selection"
        request = requests.get(url)

        # requires
        #  $ pip install lxml
        soup = bs(request.text,"lxml")

        # soup.text is to get the returned text
        # split function, splits the entire text into different lines (using '\n') and stores in a list. You can define your own splitter.
        # each line is stored as an element in the allLines list.
        allLines = soup.text.split('\n')

        for line in allLines: # you iterate through the list, and print the single lines

            t = line.split()
            if (t):
                if (t[0] != '#'):
                    print( line )
                    # print(":" + t[0])


        print('leaving DAL')

        # return the guid
        return allLines

    @classmethod
    def get_by_session(cls,session_guid):
        return None


    @classmethod
    def ts_by_guid_id(cls, guid_id):
        # cls.__load_data()
        # return cls.__people_data.get(person_id)

        session = DbSessionFactory.create_session()

        person = session.query(Person).filter(Person.id == person_id).first()

        session.close()

        return person