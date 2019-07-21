import psycopg2
from PythonMaps1.config1a import config11
from PythonMaps1.domain.timeseries import Timeseries

class Postgres_data:
    __stations_data = {}

    @classmethod
    def run_exe(sql):
        """ query data from the vendors table """
        conn = None
        try:
            # sql = "SELECT * from public.council5;"
            params = config11()
            conn = psycopg2.connect( **params )
            cur = conn.cursor()
            cur.execute( sql )
            print( "The number of rows: ", cur.rowcount )
            row = cur.fetchone()

            while row is not None:
                print( row )
                row = cur.fetchone()

            cur.close()

            return row

        except (Exception, psycopg2.DatabaseError) as error:
            print( error )
        finally:
            if conn is not None:
                conn.close()


    @classmethod
    def get_councilors(cls, councilor_id):
        """ get parts provided by a vendor specified by the vendor_id """
        conn = None
        try:
            # read database configuration
            params = config11()
            # connect to the PostgreSQL database
            conn = psycopg2.connect( **params )
            # create a cursor object for execution
            cur = conn.cursor()
            # another way to call a stored procedure
            # cur.execute("SELECT * FROM get_parts_by_vendor( %s); ",(vendor_id,))
            cur.callproc( 'get_councilors', (councilor_id,) )
            # process the result set
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
            # close the communication with the PostgreSQL database server
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print( error )
        finally:
            if conn is not None:
                conn.close()
#
    @classmethod
    def get_timeseries(cls, site_no,tsdatetime):
        """ get parts provided by a vendor specified by the vendor_id """
        conn = None
        try:
            # read database configuration
            params = config11(filename='database.ini', section='postgresql')
            # connect to the PostgreSQL database
            conn = psycopg2.connect( **params )
            # create a cursor object for execution
            cur = conn.cursor()
            # another way to call a stored procedure
            # cur.execute("SELECT * FROM get_parts_by_vendor( %s); ",(site_no,))
            # cur.execute("SELECT * FROM timeseries;")
            cur.callproc( 'get_timeseries', (site_no,) )
            # process the result set
            row = cur.fetchone()
            locTS = Timeseries()
            lstTS = []

            while row is not None:
                print( row )
                locTS.site_no = row[2]
                lstTS.append(locTS)
                row = cur.fetchone()


            # close the communication with the PostgreSQL database server
            cur.close()
            print('ts done')
            return lstTS

        except (Exception, psycopg2.DatabaseError) as error:
            print( error )
        finally:
            if conn is not None:
                conn.close()


    @classmethod
    def insert_timeseries(cls, tsvalue, site_no):

        conn = None
        try:
            # read database configuration
            params = config11()
            # connect to the PostgreSQL database
            conn = psycopg2.connect( **params )
            # create a cursor object for execution
            cur = conn.cursor()
            # another way to call a stored procedure
            # cur.execute("SELECT * FROM get_parts_by_vendor( %s); ",(site_no,))
            # cur.execute("SELECT * FROM timeseries;")
            cur.callproc( 'create_timeseries', (tsvalue,site_no,) )
            # process the result set
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
            # close the communication with the PostgreSQL database server
            cur.close()
            print('ts done')
        except (Exception, psycopg2.DatabaseError) as error:
            print( error )
        finally:
            if conn is not None:
                conn.close()
