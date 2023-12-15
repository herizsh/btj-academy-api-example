from zeep import Client

# Initialize the Zeep client with the WSDL URL
client = Client("http://127.0.0.1:8000/?wsdl")

# List Employees
print("Listing all employees:")
print(client.service.list_employees())

# Get an Employee
print("\nGetting employee with ID 1:")
print(client.service.get_employee(1))

# Add an Employee
print("\nAdding a new employee:")
print(client.service.add_employee(4, "Alice Brown"))

# Update an Employee
print("\nUpdating employee with ID 2:")
print(client.service.update_employee(2, "Jeni Lane"))

# Delete an Employee
print("\nDeleting employee with ID 3:")
print(client.service.delete_employee(3))
