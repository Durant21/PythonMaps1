from PythonMaps1.DAL import stations as DAL_stations
from PythonMaps1.viewmodels.create_station_viewmodel import CreateStationViewModel
from PythonMaps1.data.db_factory import DbSessionFactory
from PythonMaps1.DAL.stations import stations_data
from PythonMaps1.DAL import stations as stations
import uuid

class BLL_stations:
    __stations_data={}

    @classmethod
    def all_stations_centralNM_csv(cls, huc, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())
        result_guid = DAL_stations.stations_data.all_stations_centralNM_csv( huc=huc )
        return result_guid


    @classmethod
    def all_stations_usgs_csv(cls, huc, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())
        result_guid = DAL_stations.stations_data.all_stations_usgs_csv( huc=huc,limit=limit )
        return result_guid

    @classmethod
    def stations_by_huc(cls, hucs_list,limit=None):
        # cls.__load_data()
        # hucs=list(cls.__stations_data.values())

        #hucs = stations.hucs_data.hucs_by_state(hucs_list,limit=limit)

        uuid1 = str( uuid.uuid4())
        stations_group = []
        only_stations = []
        lst_hucs = hucs_list['huc_id'].split(',')

        for huc in lst_hucs:
            print(huc)
            # hucs = stations_data.stations_by_huc(huc,limit=10)
            stations = stations_data.load_usgs_stations_by_huc(huc=huc)

            for station in stations:  # you iterate through the list, and print the single lines
                s = station.split()
                if (s):
                    # if (s[0] != '#'):
                    if (s[0] == 'USGS'):
                        print( station )
                        # print(":" + t[0])
                        q = s[1]
                        only_stations.append( s[1] )



            stations_group = only_stations + stations_group

        return stations_group

    @classmethod
    def load_stations_into_DB_from_file(cls, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())
        lst_stations = DAL_stations.stations_data.all_stations_usgs_csv(limit=limit)

        for line in lst_stations:  # you iterate through the list, and print the single lines

            sentence_dict = {}
            sentence_dict.update( {'station_id': line['id']} )
            sentence_dict.update( {'OrganizationIdentifier': line['OrganizationIdentifier']} )
            sentence_dict.update( {'OrganizationFormalName': line['OrganizationFormalName']} )
            sentence_dict.update( {'MonitoringLocationTypeName': line['MonitoringLocationTypeName']} )
            sentence_dict.update( {'HUCEightDigitCode': line['HUCEightDigitCode']} )
            sentence_dict.update( {'LatitudeMeasure': line['LatitudeMeasure']} )
            sentence_dict.update( {'LongitudeMeasure': line['LongitudeMeasure']} )
            sentence_dict.update( {'ProviderName': line['ProviderName']} )

            #
            #         # create a data object based on each line
            #
            #         # TODO  validation
            vm = CreateStationViewModel( sentence_dict )
            vm.compute_details()
            if vm.errors:
                print( 'error in stations vm' )
            #     return Response( status=400, body=vm.error_msg )

            try:
                station_data = stations_data.add_station( vm.Stations )
                # return Response( status=201, json_body=station_data.to_dict() )
                print( 'new station record added' )
            except Exception as x:
                # return Response( status=400, body='Could not save station_data.' )
                print( 'Could not save station data' )

        return lst_stations