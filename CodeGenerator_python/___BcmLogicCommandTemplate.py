from Core.ExecuterModule import createParamtersString, executor
from Core.Utilities import *

print(__name__)

class GlobalOption:
    # Class attribute
    servicTemplateBasePath = "C:\\home\\CSharpCodeGenerator\\Templates\\"
    outPutBasePath= r"C:\Users\jafar\source\repos\TestCodeGenerator\TestCodeGenerator\Commands"


def createRepositoryClassTemplate(baseName, outPutBasePath):
    templatePath = GlobalOption.servicTemplateBasePath+"repositoryClassTempl.txt"
    className =baseName+"Repository"
    OutPutPath ='\\'+className+".cs"
    paramDic = {
        "in":"I"+className,
        "cl":className,
        "ns":"CodeNet.Infrastructure.Repositories"   
    }

    executor(OutPutPath,templatePath,outPutBasePath,paramDic)

def createRepositoryInterfaceTemplate(baseName, outPutBasePath):
    templatePath = GlobalOption.servicTemplateBasePath +"repositoryInterfaceTempl.txt"
    className =baseName+"Repository"
    OutPutPath ='\\I'+className+".cs"
    paramDic = {
        "in":"I"+className,
        "ns":"CodeNet.Domain.Repositories"   
    }
    executor(OutPutPath,templatePath,outPutBasePath,paramDic)

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
   