from __core.ExecuterModule import executor
from __core.Utilities import *
from sett import sett

print(__name__)


def _CreateHandlerTemp(baseName,subNamespace):
    className = baseName + "Handler"
    OutPutPath ='\\'+className+".cs"
    paramDic = {
        "cl": baseName,
        "ns": subNamespace+"."+baseName
    }

    
    subNamespace = "" if subNamespace is None else "\\"+subNamespace
    subForler= subNamespace+"\\"+ baseName

    executor(OutPutPath,
            sett.cqrs_command.handler_template_path,
            sett.cqrs_command.commands_folder_path+subForler,
            paramDic)

def _CreateCommandTemp(baseName,subNamespace):
    className = baseName + "Command"
    OutPutPath ='\\'+className+".cs"
    paramDic = {
        "cl":baseName,
        "ns":subNamespace+"."+baseName
    }
    subNamespace = "" if subNamespace is None else "\\"+subNamespace
    subForler= subNamespace+"\\"+ baseName
    executor(OutPutPath,
            sett.cqrs_command.command_template_path,
            sett.cqrs_command.commands_folder_path+subForler,
            paramDic)


def cqrs_command_execute(arrName,subNamespace):
    for baseName in arrName:
        _CreateHandlerTemp(baseName,subNamespace)
        _CreateCommandTemp(baseName,subNamespace)
    print("---------Finish----------")


   