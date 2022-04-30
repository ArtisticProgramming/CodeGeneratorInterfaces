import ExecuterModule as exe
import Utilities as util

print(__name__)

class GlobalOption:
    # Class attribute
    servicTemplateBasePath = "C:\\home\\CSharpCodeGenerator\\Templates\\"
    outPutBasePath= r"C:\Users\jafar\source\repos\TestCodeGenerator\TestCodeGenerator\Commands"


def createRepositoryClassTemplate(baseName, outPutBasePath):
    templatePath = GlobalOption.servicTemplateBasePath+"repositoryClassTempl.txt"
    className =baseName+"Repository"

    paramDic = {
        "in":"I"+className,
        "cl":className,
        "ns":"CodeNet.Infrastructure.Repositories"   
    }

    OutPutPath ='\\'+className+".cs"
    param = exe.createParamtersString(paramDic)
    exe.executor(OutPutPath,templatePath,outPutBasePath,param)

def createRepositoryInterfaceTemplate(baseName, outPutBasePath):
    templatePath = GlobalOption.servicTemplateBasePath +"repositoryInterfaceTempl.txt"
    className =baseName+"Repository"

    paramDic = {
        "in":"I"+className,
        "ns":"CodeNet.Domain.Repositories"   
    }

    OutPutPath ='\\I'+className+".cs"
    param = exe.createParamtersString(paramDic)
    exe.executor(OutPutPath,templatePath,outPutBasePath,param)

def cgRunner():
    outPutBasePath_repositoryClass =  GlobalOption.outPutBasePath
    outPutBasePath_repositoryInterface =  GlobalOption.outPutBasePath
    arrName= [
        "AddVendor",
    ]
    for baseName in arrName:
        createRepositoryClassTemplate(baseName,outPutBasePath_repositoryClass)
        createRepositoryInterfaceTemplate(baseName,outPutBasePath_repositoryInterface)
    print("---------Finish----------")

if (__name__ == "__main__"):
    cgRunner()
   