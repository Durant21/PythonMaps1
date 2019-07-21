
# !/usr/bin/python
import psycopg2
from PythonMaps1.config1a import config11
from PythonMaps1.DAL.PythonMaps.Postgres import Postgres_data

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config11()

        # connect to the PostgreSQL server
        print( 'Connecting to the PostgreSQL database...' )
        conn = psycopg2.connect( **params )

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print( 'PostgreSQL database version:' )
        # cur.execute( 'SELECT version()' )
        cur.execute('SELECT * from public.council5;')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print( db_version )

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print( error )
    finally:
        if conn is not None:
            conn.close()
            print( 'Database connection closed.' )


def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        params = config11()
        conn = psycopg2.connect( **params )
        cur = conn.cursor()
        cur.execute( "SELECT * from public.council5;" )
        print( "The number of rows: ", cur.rowcount )
        row = cur.fetchone()

        while row is not None:
            print( row )
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print( error )
    finally:
        if conn is not None:
            conn.close()

def get_councilors():
    Postgres_data.get_councilors(1)
    #get_councilors()


def get_timeseries():
    Postgres_data.get_timeseries(1,tsdatetime=None);
    #get_councilors()


def create_timeseries():
    Postgres_data.insert_timeseries( 14, '2002', );
    #get_councilors()


if __name__ == '__main__':
    # connect()
    #get_vendors()
    # get_councilors()
    get_timeseries()
    # create_timeseries()

