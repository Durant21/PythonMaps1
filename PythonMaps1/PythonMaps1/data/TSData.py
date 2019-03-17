import uuid
import sqlalchemy
import datetime

from PythonMaps1.data.sqlalchemy_base import SqlAlchemyBase


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


# [ProcNotes] = sqlalchemy.Column( sqlalchemy.String )

    def to_dict(self):
        return {
            'ts_id': self.ts_id,
            'agency_cd': self.agency_cd,
            'HydroCode': self.HydroCode,
            'TSDateTime': self.TSDateTime.isoformat(),
            'TSValue': self.TSValue,
            'uuid1': self.uuid1,
        }
