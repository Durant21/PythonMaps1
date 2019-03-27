import uuid
import sqlalchemy
import datetime

from PythonMaps1.data.sqlalchemy_base import SqlAlchemyBase


class HUCs(SqlAlchemyBase):
    __tablename__ = 'HUCs'
    # columns: fname, lname, title, position, company, email, url1, url2, address, city, state, date_edited
    # id = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
    # default=lambda: str(uuid.uuid4()))
    # fname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    # title = sqlalchemy.Column(sqlalchemy.String)
    # date_created = sqlalchemy.Column(sqlalchemy.DateTime, index=True, default=datetime.datetime.now)

    huc_id = sqlalchemy.Column( sqlalchemy.String, primary_key=True, default=lambda: str( uuid.uuid4() ) )
    state1 = sqlalchemy.Column( sqlalchemy.String )
    state2 = sqlalchemy.Column( sqlalchemy.String )
    huc_name = sqlalchemy.Column(sqlalchemy.String)
    desc = sqlalchemy.Column( sqlalchemy.String )


    def to_dict(self):
        return {
            'huc_id': self.huc_id,
            'state1': self.state1,
            'state2': self.state2,
            'huc_name': self.huc_name,
            'desc': self.desc,
        }
