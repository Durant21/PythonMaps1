from pyramid.config import Configurator
from pyramid.events import NewRequest

from pyramid.renderers import JSON

# Following references needed for Sqlite creation
from PythonMaps1.data.TSData import TSData
from PythonMaps1.data.HUCs import HUCs
from PythonMaps1.data.stations import Stations
from PythonMaps1.data.db_factory import DbSessionFactory
# from PythonMaps1.data.repository import Repository

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        init_db( config )
        config.include('.routes')

        configure_renderers( config )

        config.add_static_view( 'shapes', 'static/shapes' )
        config.add_route( 'stations_api', '/api/stations' )
        config.add_route( 'stations1_api', '/api/usgs_stations' )
        config.add_route( 'stations2_api', '/api/load_stations' )
        config.add_route( 'stations3_api', '/api/stations_by_huc' )
        config.add_route( 'usgs_api', '/api/usgs' )                     # TS by huc
        config.add_route( 'usgs2_api', '/api/usgs2' )                   # TS by station
        config.add_route( 'usgs1_api', '/api/usgs1/{guid_id}' )

        config.add_route( 'hucs_api', '/api/hucs' )
        config.add_route( 'hucs1_api', '/api/load_hucs' )
        # config.add_route( 'station_data_api', '/api/station_data' )
        # config.add_route( 'timeseries_data_api', '/api/timeseries_data' )
        config.scan()
    return config.make_wsgi_app()


def init_db(config):
    settings = config.get_settings()
    db_file = settings.get('db_filename')

    DbSessionFactory.global_init(db_file)


def configure_renderers(config):
    json_renderer = JSON(indent=4)
    json_renderer.add_adapter(TSData, lambda c, _: c.to_dict())
    json_renderer.add_adapter(HUCs, lambda p, _: p.to_dict() )
    json_renderer.add_adapter( Stations, lambda p, _: p.to_dict() )
    config.add_renderer('json', json_renderer)