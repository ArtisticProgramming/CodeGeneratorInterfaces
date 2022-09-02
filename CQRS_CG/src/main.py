from proj_struc.CQRS.Query import cqrs_query_execute
from proj_struc.CQRS.command import  cqrs_command_execute
from proj_struc.EntitySchemaConfiguration import entity_schema_configuration_execute
from proj_struc.repository import repository_execute

def create_cqrs_command_files():
    arrName= [
       "AssignFilePermission"
    ]
    cqrs_command_execute(arrName,"File")

def create_cqrs_query_files():
    arrName= [
        "Get"+"TenantQuestionSet",
    ]
    cqrs_query_execute(arrName,"Questionnaire")

def create_repository_files():
    arrName= [
        "File",
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

if (__name__ == "__main__"):
    #create_cqrs_command_files()
    #create_cqrs_query_files()
    #create_repository_files()
    entity_schema_configuration_execute_files()
