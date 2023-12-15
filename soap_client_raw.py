import requests


def send_soap_request(xml):
    headers = {"Content-Type": "text/xml; charset=utf-8"}
    response = requests.post("http://127.0.0.1:8000", data=xml, headers=headers)
    return response.text


# List Employees
list_employees_xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:emp="spyne.examples.employee">
    <soapenv:Header/>
    <soapenv:Body>
        <emp:list_employees/>
    </soapenv:Body>
</soapenv:Envelope>
"""
print("List Employees Response:")
print(send_soap_request(list_employees_xml))

# # Get Employee
get_employee_xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:emp="spyne.examples.employee">
    <soapenv:Header/>
    <soapenv:Body>
        <emp:get_employee>
            <emp:employee_id>1</emp:employee_id>
        </emp:get_employee>
    </soapenv:Body>
</soapenv:Envelope>
"""
print("\nGet Employee Response:")
print(send_soap_request(get_employee_xml))

# # Add Employee
add_employee_xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:emp="spyne.examples.employee">
    <soapenv:Header/>
    <soapenv:Body>
        <emp:add_employee>
            <emp:employee_id>4</emp:employee_id>
            <emp:employee_name>Alice Brown</emp:employee_name>
        </emp:add_employee>
    </soapenv:Body>
</soapenv:Envelope>
"""
print("\nAdd Employee Response:")
print(send_soap_request(add_employee_xml))

# Update Employee
update_employee_xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:emp="spyne.examples.employee">
    <soapenv:Header/>
    <soapenv:Body>
        <emp:update_employee>
            <emp:employee_id>2</emp:employee_id>
            <emp:employee_name>Jeni Lane</emp:employee_name>
        </emp:update_employee>
    </soapenv:Body>
</soapenv:Envelope>
"""
print("\nUpdate Employee Response:")
print(send_soap_request(update_employee_xml))

# Delete Employee
delete_employee_xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:emp="spyne.examples.employee">
    <soapenv:Header/>
    <soapenv:Body>
        <emp:delete_employee>
            <emp:employee_id>3</emp:employee_id>
        </emp:delete_employee>
    </soapenv:Body>
</soapenv:Envelope>
"""
print("\nDelete Employee Response:")
print(send_soap_request(delete_employee_xml))
