from flask import Flask, jsonify, request
from business.book_manager import Book
from datetime import datetime
from random import randint
import socket 


app = Flask(__name__)
APP_KEY = 'xQvVXrVcaZh4diC8wQ5s'

# print(__name__)
# mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'test_db'

mysql = MySQL(app)

@app.route('/api/register', methods=['POST'])
def register_api():
    application_key = request.headers['Application-Key'];

    if application_key is not None and application_key == APP_KEY:
        if request.method == 'POST':
            message = {}
            _name = request.POST['name'];
            _email = request.POST['email'];

            if _name is None or _email is None) :
                    # SAVE TO LOG([], 'N', '403', 'Please provide name and email both');
                    save_api_log("register_api", "N", "403", "Please provide name and email both")
                    message = {
                        'status': False,
                        'message': 'Please provide name and email both'
                    };
                else :
                    # GET USER TYPES WHO HAS TYPE AS API
                    now = datetime.now()
                    timestamp = datetime.timestamp(now)

                    random_number = timestamp * randint (101,999) * randint (101,999);
                    access_key = hash(random_number);

                    nextday_date = datetime.today() + timedelta(days=1)
                    # NextDay_Date_Formatted = NextDay_Date.strftime ('%d%m%Y')
                    timeout = datetime.timestamp(nextday_date)

                    save_array = {
                        'name' : _name,
                        'email' : _email,
                        'access_key' : accessKey,
                        'timeout' : timeout,
                        'user_type' : #user_type,
                        'enable' : 1
                    };

                    existing_access_token = request.headers['Access-Key'] if request.headers['Access-Key'] is not None else None

                    # GET CURRENT USER OBJECT BY EMAIL TO CHECK WHETHER THIS USER IS ALREADY REGISTERED.
                    existing_user_object = None

                    if existing_user_object is not None:
                        if existing_user_object.access_key is not None and existing_user_object.access_key = existing_access_token :
                            # UPDATE THE USER OBJECT ['access_key' => access_key, 'timeout' => timeout]
                            message = {
                                "status" : True,
                                "message" : access_key
                            }
                            
                            save_api_log("register_api", [], "Y", "200", "New access key updated and sent to the request");
                        else:
                            message = {
                                "status" : False,
                                "message" : "There is a already registered user for the email. Please send the existing access key to renew"
                            }
                    else:
                        # SAVE SAVE_ARRAY OBJECT TO THE DATABASE AS A NEW USER
                        message = {
                            "status" : True,
                            "message" : access_key
                        }

                        save_api_log("register_api", [], "Y", "200", "New user created with the new access_key");
                }

def validate_access_key(request_access_key):
    
    current_time = datetime.now()
    timestamp = datetime.timestamp(now)

    #GET USER TYPE BY THE TYPE = API ['machine_name' => 'API']

    #GET CURRENT USER BY THE USER TYPE AND ACCESS KEY ['user_type' => $apiUserType->id, 'access_key' => $accessKey]
    current_user = None
    message = {}

    if current_user is not None:
        expiretime = current_user.timeout

        if (current_time > expiretime):
            message = {
                'status' : 'error',
                'message' : 'Access token is expired. Please obtain a new token',
                'data' : [],
            };
        else:
            message = {
                'status' : 'success',
                'message' : 'Access token is valid',
                'data' : {},
            };
    else:
        message = {
            'status' : 'error',
            'message' : 'Access token is invalid. Please obtain a new token',
            'data' : {},
        };

    return message;

def save_api_log(method, params = [], authorized = 'Y', code = '200', message = None):
    hostname = socket.gethostname()    
    ip_address = socket.gethostbyname(hostname)

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    save_array = {
        'method' : method,
        'params' : jsonify(params) if params is not None else None,
        'ip_address' : ip_address,
        'time' : timestamp,
        'authorized' : authorized,
        'response_code' : code,
        'message' : message
    }

    # SAVE SAVE_ARRAY

# SEND ALL THE RESPONSES THROUGH THIS FUNCTION
def response_api_request():

app.run(port=5000)
