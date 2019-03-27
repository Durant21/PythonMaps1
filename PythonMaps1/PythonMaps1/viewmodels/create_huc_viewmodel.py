from dateutil.parser import parse

from PythonMaps1.data.HUCs import HUCs
from PythonMaps1.viewmodels.base_viewmodel import ViewModelBase


class CreateHucViewModel( ViewModelBase ):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.HUCs = None

    def compute_details(self):

        # teacherId = self.data_dict.get('teacherId', None)
        # if teacherId:
        #     teacherId = parse(teacherId)
        huc_id = self.data_dict.get( 'huc_id' )
        state1 = self.data_dict.get('state1')
        state2 = self.data_dict.get('state2' )
        # huc_name = self.data_dict.get( 'TSDateTime', -1 )
        huc_name = self.data_dict.get('huc_name')
        desc = self.data_dict.get( 'desc' )
        # uuid1 = self.data_dict.get('uuid1')
        # Qualified = self.data_dict.get('Qualified')
        # Param = self.data_dict.get('Param')
        # TS_duplcts = self.data_dict.get( 'TS_duplcts' )
        # TSTypeID = self.data_dict.get( 'TSTypeID' )
        # FeatureID = self.data_dict.get( 'FeatureID' )
        # TSRemarks = self.data_dict.get( 'TSRemarks' )
        # TSComments = self.data_dict.get( 'TSComments' )
        # BaseVsEvent = self.data_dict.get( 'BaseVsEvent' )
        # Transferable = self.data_dict.get( 'Transferable' )
        # source1 = self.data_dict.get( 'source1' )



        # last_seen =  self.data_dict.get( 'last_seen', -1 )


        # if not teacherId:
        #     self.errors.append("teacherId is a required field.")
        if not huc_name:
            self.errors.append("Huc_Name is a required field.")
        # if not TSDateTime:
        #     self.errors.append("TSDateTime is a required field.")
        # if TSValue is None:
        #     self.errors.append("TSValue is a required field.")
        # elif price < 0:
        #     self.errors.append("Price must be non-negative.")
        # if year is None:
        #     self.errors.append("You must specify a year")
        # elif year < 0:
        #     self.errors.append("Year must be non-negative.")

        if not self.errors:
            hucs = HUCs(
                huc_id=huc_id,
                state1=state1,
                state2=state2,
                # TSDateTime=TSDateTime.isoformat(),
                huc_name=huc_name,
                desc=desc,
            )
            self.HUCs = hucs

            # id, brand, name, damage, image, price, year, last_seen