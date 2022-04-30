import ExecuterModule as exe
import Utilities as util

def execute():
    print(__name__)

    BaseName = input("Enter Base Name: ") 
    print(BaseName)
    OutPutBasePath=  exe.GlobalOption.OutPutBasePath

    TemplatePath = exe.GlobalOption.TemplatePath+"GetActionData.txt"
    OutPutPath =util.GeneratetCurrentDateTime()+'\\'+"Get"+BaseName+"Data.cs"

    paramArray =[]
    paramArray.append(exe.MakeParam("Get"+BaseName+"Data" ,"1"))  
    paramArray.append(exe.MakeParam("IGet"+BaseName+"Query" ,"2"))
    paramArray.append(exe.MakeParam(BaseName+"QueryParam" ,"3"))
    Param =  exe.sep.join(paramArray)

    exe.executor(OutPutPath,TemplatePath,OutPutBasePath,Param)

#exe.OpenFolder(OutPutBasePath+OutPutPath)
