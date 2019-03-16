from pyramid.config import Configurator
from pyramid.events import NewRequest

from pyramid.renderers import JSON

# Following references needed for Sqlite creation
from PythonMaps1.data.TSData import TSData
from PythonMaps1.data.db_factory import DbSessionFactory
# from PythonMaps1.data.repository import Repository

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        init_db( config )
        config.include('.routes')
        config.add_static_view( 'shapes', 'static/shapes' )
        config.add_route( 'stations_api', '/api/stations' )
        config.add_route( 'usgs_api', '/api/usgs' )
        # config.add_route( 'station_data_api', '/api/station_data' )
        # config.add_route( 'timeseries_data_api', '/api/timeseries_data' )
        config.scan()
    return config.make_wsgi_app()


def init_db(config):
    settings = config.get_settings()
    db_file = settings.get('db_filename')

    DbSessionFactory.global_init(db_file)
