import uuid
import sqlalchemy

from PythonMaps1.data.PythonMaps.sqlalchemy_base import SqlAlchemyBase


class TSData(SqlAlchemyBase):
    __tablename__ = 'TSData'
    # columns: fname, lname, title, position, company, email, url1, url2, address, city, state, date_edited
    # id = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
    # default=lambda: str(uuid.uuid4()))
    # fname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    # title = sqlalchemy.Column(sqlalchemy.String)
    # date_created = sqlalchemy.Column(sqlalchemy.DateTime, index=True, default=datetime.datetime.now)

    ts_id = sqlalchemy.Column( sqlalchemy.String, primary_key=True, default=lambda: str( uuid.uuid4() ) )
    agency_cd = sqlalchemy.Column( sqlalchemy.String )
    HydroCode = sqlalchemy.Column( sqlalchemy.String )
    site_no = sqlalchemy.Column( sqlalchemy.String )
    TSDateTime = sqlalchemy.Column(sqlalchemy.DateTime, index=True)
    TSValue=sqlalchemy.Column( sqlalchemy.FLOAT )
    uuid1 = sqlalchemy.Column( sqlalchemy.String )
    # Qualified = sqlalchemy.Column( sqlalchemy.String )
    # Param = sqlalchemy.Column( sqlalchemy.String )
    # TS_duplcts = sqlalchemy.Column( sqlalchemy.String )
    # TSTypeID=sqlalchemy.Column( sqlalchemy.INT )
    # FeatureID=sqlalchemy.Column( sqlalchemy.INT )
    # TSRemarks = sqlalchemy.Column( sqlalchemy.String )
    # TSComments = sqlalchemy.Column( sqlalchemy.String )
    # BaseVsEvent = sqlalchemy.Column( sqlalchemy.String )
    # Transferable = sqlalchemy.Column( sqlalchemy.String )
    # source1 = sqlalchemy.Column( sqlalchemy.String )



    # agency_cd= sqlalchemy.Column( sqlalchemy.String )
    # HydroCode= sqlalchemy.Column( sqlalchemy.String )
    # TSDateTime = datetime
    # TSValue = sqlalchemy.Column( sqlalchemy.FLOAT )
    Qualified  =  sqlalchemy.Column( sqlalchemy.String )
    Param  =  sqlalchemy.Column( sqlalchemy.String )
    TS_duplcts  =  sqlalchemy.Column( sqlalchemy.String )
    TSTypeID = sqlalchemy.Column( sqlalchemy.INT )
    FeatureID = sqlalchemy.Column( sqlalchemy.INT )
    TSRemarks  =  sqlalchemy.Column( sqlalchemy.String )
    TSComments  =  sqlalchemy.Column( sqlalchemy.String )
    BaseVsEvent  =  sqlalchemy.Column( sqlalchemy.String )
    Transferable  =  sqlalchemy.Column( sqlalchemy.String )
    source1  =  sqlalchemy.Column( sqlalchemy.String )
    ProcNotes  =  sqlalchemy.Column( sqlalchemy.String )

# [ProcNotes] = sqlalchemy.Column( sqlalchemy.String )

    def to_dict(self):
        return {
            'ts_id': self.ts_id,
            'agency_cd': self.agency_cd,
            'HydroCode': self.HydroCode,
            'site_no': self.site_no,
            'TSDateTime': self.TSDateTime.isoformat(),
            'TSValue': self.TSValue,
            'uuid1': self.uuid1,
            'Qualified': self.Qualified,
            'Param': self.Param,
            'TS_duplcts': self.TS_duplcts,
            'TSTypeID': self.TSTypeID,
            'FeatureID': self.FeatureID,
            'TSRemarks': self.TSRemarks,
            'TSComments': self.TSComments,
            'BaseVsEvent': self.BaseVsEvent,
            'Transferable': self.Transferable,
            'source1': self.source1,
            'ProcNotes': self.ProcNotes,
        }
