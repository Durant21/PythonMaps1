from PythonMaps1.data.PythonMaps.TSData import TSData
from PythonMaps1.viewmodels.PythonMaps.base_viewmodel import ViewModelBase


class CreateTSViewModel( ViewModelBase ):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.TSData = None

    def compute_details(self):

        # teacherId = self.data_dict.get('teacherId', None)
        # if teacherId:
        #     teacherId = parse(teacherId)
        ts_id = self.data_dict.get( 'ts_id' )
        agency_cd = self.data_dict.get('agency_cd')
        HydroCode = self.data_dict.get('HydroCode' )
        site_no = self.data_dict.get('site_no')
        TSDateTime = self.data_dict.get( 'TSDateTime', -1 )
        TSValue = self.data_dict.get( 'TSValue' )
        uuid1 = self.data_dict.get('uuid1')
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
        # if not HydroCode:
        #     self.errors.append("HydroCode is a required field.")
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
            tsdata = TSData(
                    # brand=brand,
                    # name=name,
                    # damage=damage,
                    # image=image,
                    # price=price,
                    # year=year,
                    # last_seen=last_seen,
                    # id=id

            ts_id=ts_id,
            agency_cd=agency_cd,
            HydroCode=HydroCode,
            site_no=site_no,
            # TSDateTime=TSDateTime.isoformat(),
            TSDateTime=TSDateTime,
            TSValue=TSValue,
            uuid1=uuid1
            # Qualified=Qualified,
            # Param=Param,
            # TS_duplcts=TS_duplcts,
            # TSTypeID=TSTypeID,
            # FeatureID=FeatureID,
            # TSRemarks=TSRemarks,
            # TSComments=TSComments,
            # BaseVsEvent=BaseVsEvent,
            # Transferable=Transferable,
            # source1=source1
            )
            self.TSData = tsdata

            # id, brand, name, damage, image, price, year, last_seen