from proj_struc.CQRS.Query import cqrs_query_execute
from proj_struc.CQRS.command import  cqrs_command_execute
from proj_struc.repository import repository_execute

def create_cqrs_command_files():
    arrName= [
        "AddVendor",
    ]
    cqrs_command_execute(arrName,"vendor")

def create_cqrs_query_files():
    arrName= [
        "GetSectorList",
    ]
    cqrs_query_execute(arrName,"Sector")


def create_repository_files():
    arrName= [
        "Product",
        "Sector",
        "Category"
    ]
    repository_execute(arrName)


if (__name__ == "__main__"):
    # create_cqrs_command_files()
    #create_cqrs_query_files()
    create_repository_files()
