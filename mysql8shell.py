#
# MySQL 8 Shell
#
# This example shows a simple X DevAPI script to work with relational data
#
from mysqlsh import mysqlx # needed in case you run the code outside of the shell
# SQL CREATE TABLE statement
CREATE_TBL = """
CREATE TABLE `SuperPY`.`Caixer` (
  `Id_Caixer` int auto_increment,
  `DNI_Caixer` varchar(9) NOT NULL UNIQUE,
  `Nom_Caixer` char(30) NOT NULL,
  `Cognom_Caixer` char(30) NOT NULL,
  `Ntelf_Caixer` varchar(9) NOT NULL UNIQUE,
  PRIMARY KEY `Id_Caixer` (`Id_Caixer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""

# column list, user data structure
COLUMNS = ['DNI_Caixer', 'Nom_Caixer', 'Cognom_Caixer', 'Ntelf_Caixer']
user_info = {
  'host': 'localhost',
  'port': 33060,
  'user': 'root',
  'password': 'root',
}

# Get a session (connection)
my_session = mysqlx.get_session(user_info)

# Precautionary drop schema
my_session.drop_schema('SuperPY')

# Create the database (schema)
my_db = my_session.create_schema('SuperPY')

# Execute the SQL statement to create the table
sql_res = my_session.sql(CREATE_TBL).execute()

# Get the table object
my_tbl = my_db.get_table('SuperPY')

# Insert some rows (data)
my_tbl.insert(COLUMNS).values('paint_vat_temp', 32.815, 'Celsius').execute()
my_tbl.insert(COLUMNS).values('tongue_height_variance', 1.52, 'mm').execute()
my_tbl.insert(COLUMNS).values('ambient_temperature', 24.5, 'Celsius').execute()
my_tbl.insert(COLUMNS).values('gross_weight', 1241.01, 'pounds').execute()
# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after inserting all rows.")
my_res = my_tbl.select(COLUMNS).execute()
