from main import app
from flaskext.mysql import MySQL
mysqlObj = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'drowssap'
app.config['MYSQL_DATABASE_DB'] = 'glb_search_eng'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysqlObj.init_app(app)