#
# MySQL 8 Shell
#
# This example shows a simple X DevAPI script to work with relational data
#
from mysqlsh import mysqlx # needed in case you run the code outside of the shell
# SQL CREATE TABLE statement
CREATE_TBL = """
CREATE TABLE `factory_sensors`.`trailer_assembly` (
  `id` int auto_increment,
  `sensor_name` char(30) NOT NULL,
  `sensor_value` float DEFAULT NULL,
  `sensor_event` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `sensor_units` char(15) DEFAULT NULL,
  PRIMARY KEY `sensor_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""
# column list, user data structure
COLUMNS = ['sensor_name', 'sensor_value', 'sensor_units']
user_info = {
  'host': 'localhost',
  'port': 33060,
  'user': 'root',
  'password': 'root',
}
print("Listing 4-6 Example - Python X DevAPI Demo with Relational Data.")
# Get a session (connection)
my_session = mysqlx.get_session(user_info)
# Precautionary drop schema
my_session.drop_schema('factory_sensors')
# Create the database (schema)
my_db = my_session.create_schema('factory_sensors')
# Execute the SQL statement to create the table
sql_res = my_session.sql(CREATE_TBL).execute()
# Get the table object
my_tbl = my_db.get_table('trailer_assembly')
# Insert some rows (data)
my_tbl.insert(COLUMNS).values('paint_vat_temp', 32.815, 'Celsius').execute()
my_tbl.insert(COLUMNS).values('tongue_height_variance', 1.52, 'mm').execute()
my_tbl.insert(COLUMNS).values('ambient_temperature', 24.5, 'Celsius').execute()
my_tbl.insert(COLUMNS).values('gross_weight', 1241.01, 'pounds').execute()
# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after inserting all rows.")
my_res = my_tbl.select(COLUMNS).execute()
