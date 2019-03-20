from pyramid.view import view_config
from PythonMaps1.data.repository_stations import Repository_stations
from PythonMaps1.BLL.HUCs import hucs_data
from PythonMaps1.data.repository_station_data import Repository_station_data
from PythonMaps1.data.repository_timeseries_data import Repository_timeseries_data


@view_config(route_name='hucs_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def all_hucs(_):
    # stations = Repository_stations.all_stations_csv( limit=25 )
    hucs = hucs_data.all_hucs_csv(limit=1000)
    return hucs


