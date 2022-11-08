# Delivery App
A command line program to simulate a delivery usecase in command line app. This program allows the users to interact with the database from the command line executable, such as creating a new order, finding out all orders, and taking out the orders.

## Explaining the technology in use

### Python
Python is used to build a command line app of the IT logistic operation. CMD Program is a program which operates from the command line or from a shell. The reason of using Python to create the project is due to its flexiblity and working well with existing program. There are lots of Python libraries and modules to create a command line app from parsing arguments and options options to flagging to a CLI frameworks. Comparing to other programming, Python is a relatively lightweight languages, that is suitable to create a small size of CMD app to simulate the operation of IT logistic.

### Click
Click is a Python package easily to create a beautiful command line user interface with a little code. In this project, the module of click command and click group are suggested to be used for distinguish different commands of usage.
Reference: https://click.palletsprojects.com/en/8.1.x/

### Sqlite3
SQLite is a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine. It is a lightweighted relational database system (RDS) which support the query operation by SQL. It is good for prototyping and data extraction, while it also allows us to take out, insert, delete the record simply by the SQL queries.
Reference: https://docs.python.org/3/library/sqlite3.html


## Instruction to run the project

### Step 1 - Run the setup.sh to configure the environment
![image](https://user-images.githubusercontent.com/79916645/165115296-da4cabec-38d2-4dbb-b056-3a8199972f6e.png)

`./setup.sh`
Include the "pip install -e ." to create the executable 
Include the "python3 database.py" to create the configuration of database

### Step 2 - View the command options of llm
![image](https://user-images.githubusercontent.com/79916645/165115894-c20f837d-aa4e-49f2-b8c3-c646d33345a1.png)

`llm create-order [from] [to]`
returns a unique ID for this order.
from and to are required.

`llm list-orders`
List all the available (non-taken) orders with this format
`ID,FROM,TO\n`

`llm take-order [id]`
Try to take the order with the given ID, returns an error if order is already taken.
id is required.

### Step 3 - Execute the commands of create-order, list-orders, take-order
![image](https://user-images.githubusercontent.com/79916645/165115826-c6ec4e5a-b66c-4e3d-926f-ee28d9a72bea.png)
