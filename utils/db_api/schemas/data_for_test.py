from sqlalchemy import Integer, Column,  String, sql

from utils.db_api.db_gino import TimedBaseModel


class Data_Test(TimedBaseModel):
    __tablename__ = 'data_test'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(2800))
    options = Column(String(3000))
    points = Column(Integer)




    query: sql.Select
