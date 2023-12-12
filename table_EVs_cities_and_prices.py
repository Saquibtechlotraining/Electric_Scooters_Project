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
    CREATE TABLE cities_and_prices(
    name VARCHAR(255) NULL,
    city VARCHAR(255) NULL, 
    price VARCHAR(255) NULL,
    recorded_date DATE NULL
);
"""

# Execute SQL Query To Create the Table

with connection.cursor() as cursor:            # Here, connection() is use to establish a connection between the Python an SQL (SSMS)
    cursor.execute(create_table_query)         # cursor() is the function of  connection , which is responsible # to execute SQL query
    connection.commit()                        # commit() is the function of connection, which is use to commit()s (ie, changes will be saved)
