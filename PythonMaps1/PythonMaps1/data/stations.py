import uuid
import sqlalchemy
import datetime

from PythonMaps1.data.sqlalchemy_base import SqlAlchemyBase


class Stations(SqlAlchemyBase):
    __tablename__ = 'stations'
    # columns: fname, lname, title, position, company, email, url1, url2, address, city, state, date_edited
    # id = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
    # default=lambda: str(uuid.uuid4()))
    # fname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    # title = sqlalchemy.Column(sqlalchemy.String)
    # date_created = sqlalchemy.Column(sqlalchemy.DateTime, index=True, default=datetime.datetime.now)

    station_id = sqlalchemy.Column( sqlalchemy.String, primary_key=True, default=lambda: str( uuid.uuid4() ) )
    # state1 = sqlalchemy.Column( sqlalchemy.String )
    # state2 = sqlalchemy.Column( sqlalchemy.String )
    # huc_name = sqlalchemy.Column(sqlalchemy.String)
    # desc = sqlalchemy.Column( sqlalchemy.String )

    OrganizationIdentifier = sqlalchemy.Column( sqlalchemy.String )#: "USGS-MN",
    OrganizationFormalName = sqlalchemy.Column( sqlalchemy.String )    #: "USGS Minnesota Water Science Center",
    # "MonitoringLocationIdentifier": "MN040-441203092255201",
    # "MonitoringLocationName": "109N14W36DAADAB01",
    MonitoringLocationTypeName = sqlalchemy.Column( sqlalchemy.String )    #: "Well",
    # "MonitoringLocationDescriptionText": "",
    HUCEightDigitCode = sqlalchemy.Column( sqlalchemy.String )    #: "07040004",
    # "DrainageAreaMeasure/MeasureValue": "",
    # "DrainageAreaMeasure/MeasureUnitCode": "",
    # "ContributingDrainageAreaMeasure/MeasureValue": "",
    # "ContributingDrainageAreaMeasure/MeasureUnitCode": "",
    LatitudeMeasure =  sqlalchemy.Column( sqlalchemy.FLOAT )   #: "44.2007994",
    LongitudeMeasure =  sqlalchemy.Column( sqlalchemy.FLOAT )   #: "-92.431291",
    # "SourceMapScaleNumeric": "24000",
    # "HorizontalAccuracyMeasure/MeasureValue": "1",
    # "HorizontalAccuracyMeasure/MeasureUnitCode": "seconds",
    # "HorizontalCollectionMethodName": "Interpolated from MAP.",
    # "HorizontalCoordinateReferenceSystemDatumName": "NAD83",
    # "VerticalMeasure/MeasureValue": "1169.72",
    # "VerticalMeasure/MeasureUnitCode": "feet",
    # "VerticalAccuracyMeasure/MeasureValue": ".68",
    # "VerticalAccuracyMeasure/MeasureUnitCode": "feet",
    # "VerticalCollectionMethodName": "Interpolated from Digital Elevation Model",
    # "VerticalCoordinateReferenceSystemDatumName": "NAVD88",
    # "CountryCode": "US",
    # "StateCode": "27",
    # "CountyCode": "157",
    # "AquiferName": "",
    # "FormationTypeText": "",
    # "AquiferTypeName": "Mixed (confined and unconfined) multiple aquifers",
    # "ConstructionDateText": "19791112",
    # "WellDepthMeasure/MeasureValue": "420",
    # "WellDepthMeasure/MeasureUnitCode": "ft",
    # "WellHoleDepthMeasure/MeasureValue": "420",
    # "WellHoleDepthMeasure/MeasureUnitCode": "ft",
    ProviderName = sqlalchemy.Column( sqlalchemy.String )    #: "NWIS"

    def to_dict(self):
        return {
            'station_id': self.station_id,
            'OrganizationIdentifier': self.OrganizationIdentifier,
            'OrganizationFormalName': self.OrganizationFormalName,
            'MonitoringLocationTypeName': self.MonitoringLocationTypeName,
            'HUCEightDigitCode': self.HUCEightDigitCode,
            'LatitudeMeasure': self.LatitudeMeasure,
            'LongitudeMeasure': self.LongitudeMeasure,
            'ProviderName': self.ProviderName,
        }
