import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ga11oway!",
  database="AutoRepairShop_V1"
  port = '3306'
)

# Define a function to add a new owner to the Owner table
def add_owner(first_name, last_name, phone, email):
    mycursor = mydb.cursor()
    sql = "INSERT INTO Owner (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)"
    val = (first_name, last_name, phone, email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Define a function to add a new employee to the Employee table
def add_employee(first_name, last_name, hire_date):
    mycursor = mydb.cursor()
    sql = "INSERT INTO Employee (first_name, last_name, hire_date) VALUES (%s, %s, %s)"
    val = (first_name, last_name, hire_date)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Define a function to add a new car to the Car and Owner_Car tables
def add_car(make, model, year, owner_id):
    mycursor = mydb.cursor()
    # Add a new row to the Car table
    sql = "INSERT INTO Car (make, model, year) VALUES (%s, %s, %s)"
    val = (make, model, year)
    mycursor.execute(sql, val)
    mydb.commit()
    car_id = mycursor.lastrowid  # Get the ID of the newly inserted car
    # Add a new row to the Owner_Car table
    sql = "INSERT INTO Owner_Car (owner_id, car_id) VALUES (%s, %s)"
    val = (owner_id, car_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Define a function to add a new service to the Service table
def add_service(service_name, service_description):
    mycursor = mydb.cursor()
    sql = "INSERT INTO Service (service_name, service_description) VALUES (%s, %s)"
    val = (service_name, service_description)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Define a function to add a new repair to the Repair table
def add_repair(repair_date, service_id, car_id, emp_id):
    mycursor = mydb.cursor()
    sql = "INSERT INTO Repair (repair_date, service_id, car_id, emp_id) VALUES (%s, %s, %s, %s)"
    val = (repair_date, service_id, car_id, emp_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Test the functions by adding some new data
add_owner("John", "Doe", "555-1234", "john.doe@example.com")
add_employee("Jane", "Smith", "2022-01-01")
add_car("Toyota", "Corolla", 2010, 1)
add_service("Oil Change", "Replace engine oil and filter")
add_repair("2023-04-05", 1, 1, 1)

# Close the database connection
mydb.close
