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


def repository_execute(arrName):
    for baseName in arrName:
        _Create(baseName)
    print("---------Finish----------")


   