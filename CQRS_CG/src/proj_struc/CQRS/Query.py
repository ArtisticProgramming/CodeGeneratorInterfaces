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
            sett.cqrs_query.handler_template_path,
            sett.cqrs_query.queries_folder_path + subForler,
            paramDic)

def _CreateQueryTemp(baseName,subNamespace):
    className = baseName + "Query"
    OutPutPath ='\\'+className+".cs"
    paramDic = {
        "cl":baseName,
        "ns": subNamespace+"."+baseName
    }

    subNamespace = "" if subNamespace is None else "\\"+subNamespace
    subForler= subNamespace+"\\"+ baseName

    executor(OutPutPath,
            sett.cqrs_query.queries_template_path,
            sett.cqrs_query.queries_folder_path+ subForler,
            paramDic)


def cqrs_query_execute(arrName,subNamespace):
    for baseName in arrName:
        _CreateHandlerTemp(baseName,subNamespace)
        _CreateQueryTemp(baseName,subNamespace)
    print("---------Finish----------")


   