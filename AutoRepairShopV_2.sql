-- Owner: {owner_id} -> {first_name, last_name, phone, email}
-- Employee: {emp_id} -> {first_name, last_name, hire_date}
-- Car: {car_id} -> {make, model, year, owner_id}
-- Service: {service_id} -> {service_name, service_description}
-- Check for candidate keys and eliminate partial dependencies.
-- Owner: owner_id is already a candidate key.
-- Employee: emp_id is already a candidate key.
-- Car: car_id is already a candidate key. There is a partial dependency of {car_id} -> {owner_id, make, model, year}, so we can create a new table for Owner-Car relationship.
-- Service: service_id is already a candidate key.
-- Repair: repair_id is already a candidate key.

CREATE TABLE Owner (
owner_id INT PRIMARY KEY,
first_name VARCHAR(35),
last_name VARCHAR(35),
phone INT,
email VARCHAR(35)
);

CREATE TABLE Car (
car_id INT PRIMARY KEY,
make VARCHAR(50),
model VARCHAR(50),
year INT
);

CREATE TABLE Owner_Car (
owner_id INT,
car_id INT,
FOREIGN KEY (owner_id) REFERENCES Owner(owner_id),
FOREIGN KEY (car_id) REFERENCES Car(car_id),
PRIMARY KEY (owner_id, car_id)
);

CREATE TABLE Service (
service_id INT PRIMARY KEY,
service_name VARCHAR(35),
service_description VARCHAR(750)
);

CREATE TABLE Employee (
emp_id INT PRIMARY KEY,
first_name VARCHAR(35),
last_name VARCHAR(35),
hire_date DATE
);

CREATE TABLE Repair (
repair_id INT PRIMARY KEY,
repair_date DATE,
service_id INT,
car_id INT,
emp_id INT,
FOREIGN KEY (service_id) REFERENCES Service(service_id),
FOREIGN KEY (car_id) REFERENCES Car(car_id),
FOREIGN KEY (emp_id) REFERENCES Employee(emp_id)
);

