from pyramid.view import view_config
from PythonMaps1.BLL.PythonMaps.HUCs import hucs_data
from pyramid.request import Request
from pyramid.response import Response

@view_config(route_name='hucs_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def all_hucs_csv(_):
    # stations = Repository_stations.all_stations_csv( limit=25 )
    hucs = hucs_data.all_hucs_csv(limit=1000)
    return hucs


@view_config(route_name='hucs_api',
             request_method='POST',
             accept='application/json',
             renderer='json')
def hucs_by_state(request: Request):
    try:
        states_list = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # stations = Repository_stations.all_stations_csv( limit=25 )
    # state_name = 'SD'
    hucs = hucs_data.hucs_by_state(states_list['state2'],limit=1000)
    return hucs


@view_config(route_name='hucs1_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def load_hucs_into_DB_from_file(_):
    # stations = Repository_stations.all_stations_csv( limit=25 )
    hucs = hucs_data.load_hucs_into_DB_from_file(limit=1000)

    return hucs


