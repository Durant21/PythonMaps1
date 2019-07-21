from PythonMaps1.DAL.PythonMaps import HUCs as DAL_hucs
from PythonMaps1.viewmodels.PythonMaps.create_huc_viewmodel import CreateHucViewModel
from PythonMaps1.DAL.PythonMaps.HUCs import Repository


class hucs_data:
    __hucs_data={}

    @classmethod
    def all_hucs_csv(cls, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())
        hucs = DAL_hucs.hucs_data.all_hucs_csv(limit=limit)
        return hucs

    @classmethod
    def load_hucs_into_DB_from_file(cls, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())
        lst_hucs = DAL_hucs.hucs_data.all_hucs_csv(limit=limit)

        for line in lst_hucs:  # you iterate through the list, and print the single lines
            # t = line.split()
            t = line['state1']
            # if (t):
            #     if (t[0] != '#'):
            #         print( line )
            sentence_dict = {}
            sentence_dict.update( {'huc_id': line['id']} )
            sentence_dict.update( {'state1': line['state1']} )
            sentence_dict.update( {'state2': line['state2']} )
            sentence_dict.update( {'huc_name': line['huc']} )
            sentence_dict.update( {'desc': line['desc']} )
            #         ee = 1
            #
            #         # create a data object based on each line
            #
            #         # TODO  validation
            vm = CreateHucViewModel( sentence_dict )
            vm.compute_details()
            if vm.errors:
                print( 'error in vm' )
            #     return Response( status=400, body=vm.error_msg )

            try:
                TSdata = Repository.add_huc( vm.HUCs )
                # return Response( status=201, json_body=TSdata.to_dict() )
                print( 'new record added' )
            except Exception as x:
                # return Response( status=400, body='Could not save TSdata.' )
                print( 'Could not save HUC data' )

        return lst_hucs

    @classmethod
    def hucs_by_state(cls, state_name,limit=None):
        # cls.__load_data()
        # hucs=list(cls.__stations_data.values())

        hucs = DAL_hucs.hucs_data.hucs_by_state(state_name,limit=limit)
        return hucs


