from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/template1.pt')
def my_view(request):
    return {'project': 'PythonMaps1'}


@view_config(route_name='v2', renderer='../templates/template5.pt')
def about_view(request):
    return {'project': 'PythonMaps1'}


@view_config(route_name='testko', renderer='../templates/template6.pt')
def ko_view(request):
    return {'project': 'PythonMaps1'}