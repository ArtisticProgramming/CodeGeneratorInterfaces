from proj_struc.CQRS.Query import cqrs_query_execute
from proj_struc.CQRS.command import  cqrs_command_execute
from proj_struc.EntitySchemaConfiguration import entity_schema_configuration_execute
from proj_struc.repository import repository_execute

def create_cqrs_command_files():
    arrName= [
       "PatchTemplateFile"
    ]
    cqrs_command_execute(arrName,"TemplateFile")

def create_cqrs_query_files():
    arrName= [
        "Get"+"ParentsIncidents",
    ]
    cqrs_query_execute(arrName,"Incident")

def create_repository_files():
    arrName= [
       "IncidentClassificationCategory",
        "IncidentClassificationSubcategory",
        "IncidentWage",
        "IncidentSubClass",
        "IncidentPriority",
    ]
    repository_execute(arrName)
    

def entity_schema_configuration_execute_files():
    arrName= [
        "FilePermissionType",
        "FilePermissionRole",
        "VendorFilePermissionAccess",
        "VendorFilePermissionAccessEnterprise",
        "VendorFile",
    ]
    entity_schema_configuration_execute(arrName)

if __name__ == "__main__":
    print("----------------------------------Choose an operation:-----------------------------------")
    print("1. Command")
    print("2. Query")
    print("3. Repository")
    print("4. Schema Configuration")

    user_choice = input("Enter the number of the operation (1-4): ")

    if user_choice == "1":
        create_cqrs_command_files()
    elif user_choice == "2":
        create_cqrs_query_files()
    elif user_choice == "3":
        create_repository_files()
    elif user_choice == "4":
        entity_schema_configuration_execute_files()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")