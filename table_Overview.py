import sqlalchemy    # These 2 libraries sqlalchemy and pyodbc are use to connect programming language with SQL (SSMS)
import pyodbc        # pyodbc is use to make a database connection

# Database Connection:-
server = 'saquibevserver.database.windows.net, 1433'  # Here, 1433 are the port no. use to connect python with SQL (SSMS)
database = 'saquib_database_ev'
username = 'ev_saquibadmin'
password = '#################'  # (Hide because of crediential purpose)
driver = '{SQL Server}'


# Create pyodbc connection string, by using this connection string we can establish a connection with SQL.
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the Database using pyodbc connection sting:-
connection = pyodbc.connect(connection_string)

# Create a sqlalchemy engine:-    (Use to process SQL Query, Execute etc)
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')

# Simple sql query to create a table:-

create_table_query = """
CREATE TABLE ev_scooter (
    name VARCHAR(500) NOT NULL,
    recorded_date DATE NULL,
    over_all_rating DECIMAL(10, 2) NULL, 
    price_range VARCHAR(500) NULL,
    range VARCHAR(500) NULL, 
    top_speed VARCHAR(500) NULL,
    power VARCHAR(500) NULL,
    front_suspension VARCHAR(500) NULL,
    rear_suspension VARCHAR(500) NULL, 
    front_type VARCHAR(500) NULL,
    wheel_type VARCHAR(500) NULL,
    total_no_of_reviews VARCHAR(500) NULL,
    design DECIMAL(10, 2) NULL, 
    comfort DECIMAL(10, 2) NULL, 
    reliability_maintenance DECIMAL(10, 2) NULL, 
    kerb_weight VARCHAR(500) NULL,
    charging_time VARCHAR(500) NULL,
    seat_height VARCHAR(500) NULL,
    max_power VARCHAR(500) NULL,
    battery_capacity VARCHAR(500) NULL,
    rear_type VARCHAR(500) NULL,
    mileage_performance DECIMAL(10, 2) NULL, 
    maintenance_cost DECIMAL(10, 2) NULL, 
    features DECIMAL(10, 2) NULL, 
    good_features VARCHAR(500) NULL,
    bad_features VARCHAR(500) NULL,
    performance DECIMAL(10, 2) NULL, 
    mileage DECIMAL(10, 2) NULL, 
    safety DECIMAL(10, 2) NULL, 
    value_for_money DECIMAL(10, 2) NULL, 
    styling DECIMAL(10, 2) NULL
);
"""

# Execute SQL Query To Create the Table

with connection.cursor() as cursor:            # Here, connection() is use to establish a connection between the Python an SQL (SSMS)
    cursor.execute(create_table_query)         # cursor() is the function of  connection , which is responsible # to execute SQL query
    connection.commit()                        # commit() is the function of connection, which is use to commit()s (ie, changes will be saved)



    
