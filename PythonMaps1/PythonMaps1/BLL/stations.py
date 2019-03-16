from PythonMaps1.DAL import stations as DAL_stations

class stations_data:
    __stations_data={}

    @classmethod
    def all_stations_csv(cls, huc, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())
        result_guid = DAL_stations.stations_data.all_stations_csv(huc=huc)
        return result_guid
