
import uuid

import sqlalchemy
import datetime

from PythonMaps1.data.PythonMaps.sqlalchemy_base import SqlAlchemyBase


class Timeseries (SqlAlchemyBase):

    __tablename__ = 'Timeseries'

    # ts_id, agency_cd, HydroCode

    uuid = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
                           default=lambda: str(uuid.uuid4()))
    agency_cd = sqlalchemy.Column( sqlalchemy.String )
    HydroCode = sqlalchemy.Column(sqlalchemy.String)
    site_no = sqlalchemy.Column(sqlalchemy.String)
    TSDateTime = sqlalchemy.Column(sqlalchemy.String)
    TSValue = sqlalchemy.Column(sqlalchemy.Float)
    uuid1 = sqlalchemy.Column( sqlalchemy.String )
    Qualified = sqlalchemy.Column(sqlalchemy.String)
    Param = sqlalchemy.Column(sqlalchemy.String)
    TS_duplcts = sqlalchemy.Column(sqlalchemy.String)
    TSTypeID = sqlalchemy.Column(sqlalchemy.Integer)
    FeatureID = sqlalchemy.Column(sqlalchemy.Integer)
    TSRemarks = sqlalchemy.Column(sqlalchemy.String)
    TSComments = sqlalchemy.Column(sqlalchemy.String)
    BaseVsEvent = sqlalchemy.Column(sqlalchemy.String)
    Transferable = sqlalchemy.Column(sqlalchemy.String)
    source1 = sqlalchemy.Column(sqlalchemy.String)
    ProcNotes = sqlalchemy.Column(sqlalchemy.String)

