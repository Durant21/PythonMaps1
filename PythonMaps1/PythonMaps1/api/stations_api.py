from pyramid.view import view_config
from PythonMaps1.data.repository_stations import Repository_stations
from PythonMaps1.BLL.stations import BLL_stations
from PythonMaps1.data.repository_station_data import Repository_station_data
from PythonMaps1.data.repository_timeseries_data import Repository_timeseries_data
from pyramid.request import Request
from pyramid.response import Response
from PythonMaps1.BLL.stations import stations_data

@view_config(route_name='stations_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def all_stations_centralNM(_):
    # stations = Repository_stations.all_stations_csv( limit=25 )
    s = BLL_stations.all_stations_centralNM_csv( huc="0101010" )
    return s

@view_config(route_name='stations1_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def all_stations_usgs(_):
    # stations = Repository_stations.all_stations_csv( limit=25 )
    s = BLL_stations.all_stations_usgs_csv( huc="0101010", limit=10 )
    return s


@view_config(route_name='stations3_api',
             request_method='POST',
             accept='application/json',
             renderer='json')
def stations_by_huc(request: Request):
    try:
        hucs_list = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # stations = Repository_stations.all_stations_csv( limit=25 )
    # state_name = 'SD'
    # hucs = stations_data.stations_by_huc(hucs_list['huc_id'],limit=1000)

    hucs = BLL_stations.stations_by_huc(hucs_list,limit=None)

    return hucs


@view_config(route_name='stations2_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def load_stations_into_DB_from_file(_):
    # stations = Repository_stations.all_stations_csv( limit=25 )
    stations = BLL_stations.load_stations_into_DB_from_file(limit=1000)

    return stations



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
