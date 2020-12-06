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
  'port': 3306,
  'user': 'root',
  'password': 'root',
}


print("Listing 4-6 Example - Python X DevAPI Demo with Relational Data.")
# Get a session (connection)
my_session = mysqlx.get_session(user_info)

# Precautionary drop schema
my_session.drop_schema('SuperPY')

# Create the database (schema)
my_db = my_session.create_schema('SuperPY')

# Execute the SQL statement to create the table
sql_res = my_session.sql(CREATE_TBL).execute()

# Get the table object
my_tbl = my_db.get_table('Caixer')

# Insert some rows (data)
my_tbl.insert(COLUMNS).values('42345678A','caixer1','cognom1','987654321').execute()
my_tbl.insert(COLUMNS).values('43345678B','caixer2','cognom2','977654322').execute()
my_tbl.insert(COLUMNS).values('44345678C','caixer3','cognom3','967654323').execute()
my_tbl.insert(COLUMNS).values('45345678D','caixer4','cognom4','957654324').execute()
# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after inserting all rows.")
my_res = my_tbl.select(COLUMNS).execute()

# Display the results . Demonstrates how to work with results
# Print the column names followed by the rows
column_names = my_res.get_column_names()
column_count = my_res.get_column_count()

for i in range(0,column_count):
    if i < column_count - 1:
        print ("{0}, ".format(column_names[i])),
    else:
        print ("{0}".format(column_names[i])),
print
for row in my_res.fetch_all():
    for i in range(0,column_count):
        if i < column_count - 1:
            print ("{0}, ".format(row[i])),
        else:
            print ("{0}".format(row[i])),
    print

# Update a row
my_tbl.update().set('Cognom_Caixer', 'Update1').where('Id_Caixer LIKE 1').execute()
my_res = my_tbl.select(COLUMNS).execute()

# Display the results
for row in my_res.fetch_all():
    print (row)
    
    
# Delete some rows
my_tbl.delete().where("Id_Caixer LIKE 3").execute()

# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after deleting rows with ID 3)
my_res = my_tbl.select(COLUMNS).execute()
# Display the results
for row in my_res.fetch_all():
    print (row)

