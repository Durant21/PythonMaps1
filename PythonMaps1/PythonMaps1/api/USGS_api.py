
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from PythonMaps1.BLL.PythonMaps.USGS import USGS_data


# @view_config(route_name='usgs_api',
#              request_method='GET',
#              accept='application/json',
#              renderer='json')
# def get_usgs_timeseries_by_guid(_):
#     # stations = Repository_stations.all_stations(limit=25)
#     # huc_id = Request.matchdict.get( 'huc_id' )
#     huc_id = "04010101"
#     data = USGS_data.load_by_HUC( hucs=huc_id )
#
#     return data

@view_config(route_name='usgs_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def all_ts(_):
    ts = USGS_data.all_ts(limit=25)
    return ts


@view_config(route_name='usgs4_api',
             request_method='POST',
             accept='application/json',
             renderer='json')
def validate_ts(request: Request):
    # matchdict = request.matchdict
    # guid_id = request.matchdict.get("uuid")
    hucs_list = request.json_body
    guid_id = hucs_list["uuid"]
    # guid_id2 = request.matchdict['uuid']

    ts = USGS_data.validate(guid_id,limit=25)
    return ts


@view_config(route_name='usgs1_api',
             request_method='GET',
             renderer='json')
def get_usgs_timeseries_by_guid(request: Request):
    guid_id = request.matchdict.get('guid_id')
    ts = USGS_data.ts_by_guid_id(guid_id)

    if not ts:
        msg = "The guid with id '{}' was not found.".format(guid_id)
        return Response(status=404,json_body={'error:': msg})

    return ts


@view_config(route_name='usgs_api',
             request_method='POST',
             accept='application/json',
             renderer='json')
def load_usgs_timeseries_by_huc(request: Request):
    try:
        hucs_list = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # stations = Repository_stations.all_stations(limit=25)
    # huc_id = Request.matchdict.get( 'huc_id' )
    # huc_id = "04010101"

    guid_id = USGS_data.load_by_HUC( hucs=hucs_list['huc_id'],date_from=hucs_list['date_from'],date_to=hucs_list['date_to'], limit=None )

    ts = USGS_data.ts_by_guid_id(guid_id)

    if not ts:
        msg = "The guid with id '{}' was not found.".format(guid_id)
        return Response(status=404,json_body={'error:': msg})

    return ts


@view_config(route_name='usgs2_api',
             request_method='POST',
             accept='application/json',
             renderer='json')
def load_usgs_timeseries_by_station(request: Request):
    try:
        stations_list = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # stations = Repository_stations.all_stations(limit=25)
    # huc_id = Request.matchdict.get( 'huc_id' )
    # huc_id = "04010101"

    guid_id = USGS_data.load_by_station( stations=stations_list['station_id'],date_from=stations_list['date_from'],date_to=stations_list['date_to'], limit=None )

    ts = USGS_data.ts_by_guid_id(guid_id)

    if not ts:
        msg = "The guid with id '{}' was not found.".format(guid_id)
        return Response(status=404,json_body={'error:': msg})

    return ts