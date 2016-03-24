__author__ = 'valentine'
from odm2api.ODMconnection import dbconnection
from odm2api.ODM2.models import *
import pytest
from sqlalchemy.engine import reflection

# assumes that pytest is being run from ODM2PythonAPI director
dbs = [
 #   ['mysql', 'localhost', 'odm2', 'ODM', 'odm'],
 #      ["sqlite", "./tests/spatialite/odm2_test.sqlite",None, None]
    ["mssql", "localhost",'odm2_lbr', 'odm', 'odm'],
    ["sqlite", ".spatialite/odm2_test.sqlite",None, None,None]
]
class Connection:
    def __init__(self, request):
        #session_factory = dbconnection.createConnection('mysql', 'localhost', 'odm2', 'ODM', 'odm')
        db = request.param
        session_factory = dbconnection.createConnection(db[0],db[1],db[2],db[3],db[4])
        insp = reflection.Inspector.from_engine(session_factory.engine)
        tables = insp.get_table_names()
        self.session = session_factory.getSession()


#
#              params=["sqlite+pysqlite:///../../ODM2PythonAPI/tests/spatialite/odm2_test.sqlite", "mail.python.org"])
@pytest.fixture(scope="session", params = dbs)
def setup(request):
    return Connection(request)


#connect to all 4 database types( mssql, mysql, postgresql, sqlite, mssql on mac)
def test_connection(setup):

    q= setup.session.query(CVElevationDatum)
    results= q.all()
    #print results
    assert len(results) > 0



