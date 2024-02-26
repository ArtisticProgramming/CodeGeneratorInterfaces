import os
currentPath=os.path.abspath(os.getcwd())

class _base_setting:
     #Project Paths
     # -----------VendorHub------------
     #application_project_base_path= r"C:\Users\jafar\source\repos\VendorHUB\src\BcmLogicONE.VendorHUB.Application";
     #infrastructure_project_base_path= r"C:\Users\jafar\source\repos\VendorHUB\src\BcmLogicONE.VendorHUB.Infrastructure";
     # -----------Incident Service------------
     application_project_base_path= r"C:\Users\tree\source\repos\BCMLogicONEServices\src\BCMLogicONE.Services\IncidentSvc\BcmLogicONE.IncidentService.Application";
     infrastructure_project_base_path= r"C:\Users\tree\source\repos\BCMLogicONEServices\src\BCMLogicONE.Services\IncidentSvc\BcmLogicONE.IncidentService.Infrastructure";
     
     #Template Paths
     tempate_base_path= currentPath+r"\configuration\Template"

class cqrs_command:
     _base_template_path = _base_setting.tempate_base_path + r"\CQRS"
     #templates
     handler_template_path =  _base_template_path + r"\command_handler.txt"
     command_template_path =  _base_template_path + r"\command.txt"
     #Project Paths
     commands_folder_path = _base_setting.application_project_base_path+r"\Commands"

class cqrs_query:
     _base_template_path = _base_setting.tempate_base_path + r"\CQRS"
     #templates
     handler_template_path =  _base_template_path + r"\query_handler.txt"
     queries_template_path =  _base_template_path + r"\query.txt"
     #Project Paths
     queries_folder_path = _base_setting.application_project_base_path+r"\Queries"

class repository:
     _base_template_path = _base_setting.tempate_base_path + r"\Repository"
     #templates
     template_path =  _base_template_path + r"\Repository.txt"
     #Project Paths
     folder_path = _base_setting.infrastructure_project_base_path+r"\Repositories"
    


class IRepository:
     _base_template_path = _base_setting.tempate_base_path + r"\Repository"
     #templates
     template_path =  _base_template_path + r"\IRepository.txt"
     #Project Paths
     folder_path = _base_setting.infrastructure_project_base_path+ r"\Contracts\Repository"
    


class EntitySchemaConfiguration:
     #templates
     template_path =  _base_setting.tempate_base_path + r"\Schema\EntitySchemaConfiguration.txt"
     #Project Paths
     folder_path = _base_setting.infrastructure_project_base_path+r"\SchemaDefinitions"
  