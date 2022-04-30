from __core.ExecuterModule import executor
from __core.Utilities import *
from sett import sett

print(__name__)


def _CreateHandlerTemp(baseName):
    className = baseName + "Handler"
    OutPutPath ='\\'+className+".cs"
    paramDic = {
        "cl": baseName,
        "ns": baseName
    }
    executor(OutPutPath,
            sett.cqrs_command.handler_template_path,
            sett.cqrs_command.commands_folder_path+r"\\"+ baseName,
            paramDic)

def _CreateCommandTemp(baseName):
    className = baseName + "Command"
    OutPutPath ='\\'+className+".cs"
    paramDic = {
        "cl":baseName,
        "ns":baseName
    }
    executor(OutPutPath,
            sett.cqrs_command.command_template_path,
            sett.cqrs_command.commands_folder_path+r"\\"+ baseName,
            paramDic)


def cqrs_command_execute(arrName):
    for baseName in arrName:
        _CreateHandlerTemp(baseName)
        _CreateCommandTemp(baseName)
    print("---------Finish----------")


   