from pyramid.view import view_config
from PythonMaps1.data.repository_stations import Repository_stations
from PythonMaps1.BLL.stations import stations_data
from PythonMaps1.data.repository_station_data import Repository_station_data
from PythonMaps1.data.repository_timeseries_data import Repository_timeseries_data


@view_config(route_name='stations_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def all_stations(_):
    # stations = Repository_stations.all_stations_csv( limit=25 )
    s = stations_data.all_stations_csv(huc="0101010")
    return s


# @view_config(route_name='station_data_api',
#              request_method='GET',
#              accept='application/json',
#              renderer='json')
# def data_by_stationid(_):
#     station_data = Repository_station_data.all_stations_data(limit=25)
#
#     return station_data
#
#
# @view_config(route_name='timeseries_data_api',
#              request_method='GET',
#              accept='application/json',
#              renderer='json')
# def all_timeseries_data(_):
#     ts_data = Repository_timeseries_data.all_timeseries_data(limit=25)
#
#     return ts_data
