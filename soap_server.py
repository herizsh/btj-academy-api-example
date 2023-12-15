from spyne.application import Application
from spyne.decorator import rpc
from spyne.service import ServiceBase
from spyne.model.primitive import Unicode, Integer, String
from spyne.protocol.soap import Soap11, Soap12  # 1.1, 1.2
from spyne.server.wsgi import WsgiApplication


#  Class Service
class EmployeeService(ServiceBase):
    employees = {1: "Budi Setiawan", 2: "Siti Aisyah", 3: "Andi Sutanto"}

    @rpc(_returns=String)  # rpc, remote produce call
    def list_employees(ctx):
        return ", ".join(
            [f"{key}: {value}" for key, value in EmployeeService.employees.items()]
        )

    @rpc(Integer, _returns=Unicode)
    def get_employee(ctx, employee_id):
        return EmployeeService.employees.get(employee_id, "Unknown")

    @rpc(Integer, Unicode, Integer, _returns=Unicode)
    def add_employee(ctx, employee_id, employee_name):
        if employee_id in EmployeeService.employees:
            return "Employee ID already exists."
        EmployeeService.employees[employee_id] = employee_name
        return f"Employee {employee_name} added successfully."

    @rpc(Integer, Unicode, _returns=Unicode)
    def update_employee(ctx, employee_id, employee_name):
        if employee_id not in EmployeeService.employees:
            return "Employee not found."
        EmployeeService.employees[employee_id] = employee_name
        return f"Employee {employee_id} updated to {employee_name}."

    @rpc(Integer, _returns=Unicode)
    def delete_employee(ctx, employee_id):
        if employee_id not in EmployeeService.employees:
            return "Employee not found."
        del EmployeeService.employees[employee_id]
        return f"Employee {employee_id} deleted."


# Class Company
class CompanyService(ServiceBase):
    @rpc(_returns=Unicode)
    def get_company_name(ctx):
        return "Spyne"


application = Application(
    [EmployeeService],  # list services
    tns="spyne.examples.employee",  # target namespace
    in_protocol=Soap11(validator="lxml"),  # input protocol validator lxml
    out_protocol=Soap11(),
)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    server = make_server("127.0.0.1", 8000, WsgiApplication(application))
    server.serve_forever()
