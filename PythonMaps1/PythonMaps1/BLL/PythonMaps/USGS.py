import uuid

from PythonMaps1.DAL.PythonMaps import USGS
from PythonMaps1.DAL.PythonMaps.TS import Repository
from PythonMaps1.viewmodels.PythonMaps.create_ts_viewmodel import CreateTSViewModel
from PythonMaps1.data.PythonMaps.db_factory import DbSessionFactory
from PythonMaps1.data.PythonMaps.TSData import TSData
from PythonMaps1.DAL.PythonMaps.Postgres import Postgres_data

from PythonMaps1.DAL.PythonMaps.USGS import USGS_data
from PythonMaps1.DAL.PythonMaps.Postgres import Postgres_data
from PythonMaps1.DAL.PythonMaps.TS import Repository

class USGS_data:
    __stations_data={}

    @classmethod
    def all_ts(cls, limit=None):
        ts = USGS.USGS_data.all_ts( limit=25 )

        return ts


    @classmethod
    def validate(cls,guid_id, limit=None):
        # get all the records by guid

        # check the server for duplicates.
        # non-duplicates marked as 'transferable'
        #     for each r in ts:
        #         bDuplicate = USGS.USGS_data.run_exe( strSQL)
        #
        #         if (bDuplicate):
        #             iDups = iDups + 1
        #
        #               # add duplicate's record_id to array
        #
        # update all local TS records by the array (set transferable = false)

        ts = USGS.USGS_data.ts_by_guid_id( guid_id )
        #
        for TSData in ts:
            tsvalue = TSData.TSValue
            site_no = TSData.site_no
            tsdatetime = TSData.TSDateTime
            tsrecs = Postgres_data.get_timeseries(site_no=site_no,tsdatetime=tsdatetime)
            print(str(tsrecs.__len__()) + " recs")

            if (tsrecs.__len__() == 0):
                doc_name = 'a doc name'
                task = (guid_id)
                Repository.update_ts(task)


        #
        # sql = "SELECT * from public.council5;"
        #
        # ts = Postgres_data.run_exe( sql )


        # count records by guid where 'transferable = true'


        # return: {duplicates: <n> , non-duplicates: <n> , transferable: <n>}


        return ts



    @classmethod
    def load_by_HUC(cls, hucs,date_from,date_to, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())

        uuid1 = str( uuid.uuid4())

        lst_hucs = hucs.split(',')

        for huc in lst_hucs:
            result_guid = USGS.USGS_data.usgs_load_by_HUC( huc, date_from, date_to, limit )

            for line in result_guid: # you iterate through the list, and print the single lines
                t = line.split()
                if t:
                    if t[0] != '#' and t[0] != 'No':
                        print( line )
                        sentence_dict = {}
                        sentence_dict.update( {'agency_cd': t[0]} )
                        # sentence_dict.update( {'HydroCode': t[1]} )
                        sentence_dict.update( {'site_no': t[1]} )
                        # sentence_dict.update( {'ts_id': '22222'} )
                        sentence_dict.update( {'TSDateTime': t[2]} )

                        try:
                            sentence_dict.update( {'TSValue': t[3]} )
                        except (IndexError, ValueError):
                            sentence_dict.update( {'TSValue': '0'} )

                        # if t[3]:
                        #     sentence_dict.update( {'TSValue': t[3]} )
                        # else:
                        #     sentence_dict.update( {'TSValue': '0'} )

                        sentence_dict.update( {'uuid1': uuid1} )
                        ee = 1

                        # create a data object based on each line

                        # TODO  validation
                        vm = CreateTSViewModel( sentence_dict )
                        vm.compute_details()
                        if vm.errors:
                            print('error in vm')
                        #     return Response( status=400, body=vm.error_msg )

                        try:
                            TSdata = Repository.add_ts( vm.TSData )
                            # return Response( status=201, json_body=TSdata.to_dict() )
                            print('new record added')
                        except Exception as x:
                            # return Response( status=400, body='Could not save TSdata.' )
                            print('Could not save TSdata')


            # TODO insert into local DB


        print('done')

        # if the data was loaded, pull it from the BD
        # data = USGS.USGS_data.get_by_session(session_guid=uuid1)
        data = USGS_data.ts_by_guid_id( uuid1 )
        if limit:
            data=data[:limit]
            return data

        return uuid1

    @classmethod
    def load_by_station(cls, stations,date_from,date_to, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())

        uuid1 = str( uuid.uuid4())

        lst_stations = stations.split(',')

        for station in lst_stations:
            result_guid = USGS.USGS_data.usgs_load_by_station( station, date_from, date_to, limit )

            for line in result_guid: # you iterate through the list, and print the single lines
                t = line.split()
                if t:
                    if t[0] != '#' and t[0] != 'No':
                        print( line )
                        sentence_dict = {}
                        sentence_dict.update( {'agency_cd': t[0]} )
                        # sentence_dict.update( {'HydroCode': t[1]} )
                        sentence_dict.update( {'site_no': t[1]} )
                        # sentence_dict.update( {'ts_id': '22222'} )
                        sentence_dict.update( {'TSDateTime': t[2]} )

                        try:
                            sentence_dict.update( {'TSValue': t[3]} )
                        except (IndexError, ValueError):
                            sentence_dict.update( {'TSValue': '0'} )

                        # if t[3]:
                        #     sentence_dict.update( {'TSValue': t[3]} )
                        # else:
                        #     sentence_dict.update( {'TSValue': '0'} )

                        sentence_dict.update( {'uuid1': uuid1} )
                        ee = 1

                        # create a data object based on each line

                        # TODO  validation
                        vm = CreateTSViewModel( sentence_dict )
                        vm.compute_details()
                        if vm.errors:
                            print('error in vm')
                        #     return Response( status=400, body=vm.error_msg )

                        try:
                            TSdata = Repository.add_ts( vm.TSData )
                            # return Response( status=201, json_body=TSdata.to_dict() )
                            print('new record added')
                        except Exception as x:
                            # return Response( status=400, body='Could not save TSdata.' )
                            print('Could not save TSdata')


            # TODO insert into local DB


        print('done')

        # if the data was loaded, pull it from the BD
        # data = USGS.USGS_data.get_by_session(session_guid=uuid1)
        data = USGS_data.ts_by_guid_id( uuid1 )
        if limit:
            data=data[:limit]
            return data

        return uuid1

    @classmethod
    def ts_by_guid_id(cls, guid_id):
        # cls.__load_data()
        # return cls.__people_data.get(person_id)
        #return None

        ts = USGS.USGS_data.ts_by_guid_id( guid_id )

        return ts

    @classmethod
    def all_ts11(cls, limit=None):
        # cls.__load_data()
        #
        # cars = list(cls.__car_data.values())
        # if limit:
        #     cars = cars[:limit]
        #
        # return cars

        session = DbSessionFactory.create_session()

        query = session.query(TSData).order_by(TSData.HydroCode)  # .order_by(Teacher.lName)

        if limit:
            ts = query[:limit]
        else:
            ts = query.all()

        session.close()


        return ts