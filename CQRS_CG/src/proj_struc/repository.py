from __core.ExecuterModule import CreateFileName, executor
from __core.Utilities import *
from sett import sett

print(__name__)


def _Create(baseName):
    className = baseName + "Repository"

    paramDic = {"cl":baseName}

    executor(CreateFileName(className),
            sett.repository.template_path,
            sett.repository.folder_path,
            paramDic)

def _CreateInterface(baseName):
    className = "I"+baseName + "Repository"

    paramDic = {"cl":baseName}

    executor(CreateFileName(className),
            sett.repository_interfae.template_path,
            sett.repository_interfae.folder_path,
            paramDic)


def repository_execute(arrName):
    for baseName in arrName:
        _Create(baseName)
        _CreateInterface(baseName)
    print("---------Finish----------")
    print("------------------------Add This To DI InfrastructureServiceRegistration class-----------------------")
    for baseName in arrName:
       print("services.AddScoped<I"+baseName+"Repository, "+baseName+"Repository>();")
       print("private readonly I"+baseName+"Repository _"+baseName+"Repository;")


   