from __core.ExecuterModule import CreateFileName, executor
from __core.Utilities import *
from sett import sett

print(__name__)


def _Create(baseName):
    className = baseName + "EntitySchemaConfiguration"

    paramDic = {"cl":baseName}

    executor(CreateFileName(className),
            sett.entitySchemaConfiguration.template_path,
            sett.entitySchemaConfiguration.folder_path,
            paramDic)



def entity_schema_configuration_execute(arrName):
    for baseName in arrName:
        _Create(baseName)
      
    print("---------Add this line to VendorHUBContext class OnModelCreating method-----------")
    for baseName in arrName:
         print("modelBuilder.ApplyConfiguration(new "+baseName+"EntitySchemaConfiguration());")
         print("public DbSet<"+baseName+">? "+baseName+" { get; set; }")
    print("")
    print("----------------------------------Finish-------------------------------------------")


   