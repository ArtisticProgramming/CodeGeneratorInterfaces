from proj_struc.CQRS.Query import cqrs_query_execute
from proj_struc.CQRS.command import  cqrs_command_execute

def create_cqrs_command_files():
    arrName= [
        "AddVendor",
    ]
    cqrs_command_execute(arrName,"vendor")

def create_cqrs_query_files():
    arrName= [
        "HasAtomicPermission",
    ]
    cqrs_query_execute(arrName,"AtomicPermission")


if (__name__ == "__main__"):
    # create_cqrs_command_files()
    create_cqrs_query_files()
