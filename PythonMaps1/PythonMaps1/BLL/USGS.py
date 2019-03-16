import csv
import os
import uuid

from PythonMaps1.DAL import USGS
from PythonMaps1.DAL.TS import Repository
from PythonMaps1.viewmodels.create_ts_viewmodel import CreateTSViewModel

class USGS_data:
    __stations_data={}

    @classmethod
    def load_by_HUC(cls, hucs, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())
        r = uuid.uuid4()

        uuid1 = str( uuid.uuid4())

        lst_hucs = hucs.split(',')

        for huc in lst_hucs:
            result_guid = USGS.USGS_data.usgs_load_by_HUC( huc )

            for line in result_guid: # you iterate through the list, and print the single lines
                t = line.split()
                if (t):
                    if (t[0] != '#'):
                        print( line )
                        sentence_dict = {}
                        sentence_dict.update( {'agency_cd': t[0]} )
                        sentence_dict.update( {'HydroCode': t[1]} )
                        # sentence_dict.update( {'ts_id': '22222'} )
                        sentence_dict.update( {'TSDateTime': t[2]} )
                        sentence_dict.update( {'TSValue': t[3]} )
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
            data = USGS.USGS_data.get_by_session(session_guid=result_guid)
            if limit:
                data=data[:limit]
                return data


    @classmethod
    def ts_by_guid_id(cls, guid_id):
        # cls.__load_data()
        # return cls.__people_data.get(person_id)
        #return None

        # session = DbSessionFactory.create_session()
        #
        # person = session.query(Person).filter(Person.id == person_id).first()
        #
        # session.close()
        #
        # return person

        return None