#!/usr/bin/python
from configparser import ConfigParser
from os import path
import PythonMaps1

def config11(filename='database.ini', section='postgresql'):
    working_folder = path.dirname(PythonMaps1.__file__)
    import os
    exists = os.path.isfile( working_folder + "/" + filename )
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read( working_folder + "/" + filename )

    # get section, default to postgresql
    db = {}
    t = parser.sections()
    if parser.has_section( section ):
        params = parser.items( section )
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception( 'Section {0} not found in the {1} file'.format( section, filename ) )

    return db



def init_db(config):
    settings = config.get_settings()
    db_file = settings.get('db_filename')

