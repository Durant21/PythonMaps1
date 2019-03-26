from dateutil.parser import parse

from PythonMaps1.data.stations import Stations
from PythonMaps1.viewmodels.base_viewmodel import ViewModelBase


class CreateStationViewModel( ViewModelBase ):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.Stations = None

    def compute_details(self):

        # teacherId = self.data_dict.get('teacherId', None)
        # if teacherId:
        #     teacherId = parse(teacherId)
        station_id = self.data_dict.get( 'station_id' )
        OrganizationIdentifier = self.data_dict.get('OrganizationIdentifier')
        OrganizationFormalName = self.data_dict.get('OrganizationFormalName' )
        # huc_name = self.data_dict.get( 'TSDateTime', -1 )
        MonitoringLocationTypeName = self.data_dict.get('MonitoringLocationTypeName')
        HUCEightDigitCode = self.data_dict.get( 'HUCEightDigitCode' )
        LatitudeMeasure = self.data_dict.get('LatitudeMeasure')
        LongitudeMeasure = self.data_dict.get('LongitudeMeasure')
        ProviderName = self.data_dict.get('ProviderName')
        # TS_duplcts = self.data_dict.get( 'TS_duplcts' )
        # TSTypeID = self.data_dict.get( 'TSTypeID' )
        # FeatureID = self.data_dict.get( 'FeatureID' )
        # TSRemarks = self.data_dict.get( 'TSRemarks' )
        # TSComments = self.data_dict.get( 'TSComments' )
        # BaseVsEvent = self.data_dict.get( 'BaseVsEvent' )
        # Transferable = self.data_dict.get( 'Transferable' )
        # source1 = self.data_dict.get( 'source1' )



        # if not teacherId:
        #     self.errors.append("teacherId is a required field.")
        if not LatitudeMeasure:
            self.errors.append("LatitudeMeasure is a required field.")
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
            stations = Stations(
                station_id=station_id,
                OrganizationIdentifier=OrganizationIdentifier,
                OrganizationFormalName=OrganizationFormalName,
                # TSDateTime=TSDateTime.isoformat(),
                MonitoringLocationTypeName=MonitoringLocationTypeName,
                HUCEightDigitCode=HUCEightDigitCode,
                LatitudeMeasure=LatitudeMeasure,
                LongitudeMeasure=LongitudeMeasure,
                ProviderName=ProviderName,
            )
            self.Stations = stations

            # id, brand, name, damage, image, price, year, last_seen