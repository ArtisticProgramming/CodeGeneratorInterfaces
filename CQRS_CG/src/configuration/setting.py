import os
currentPath=os.path.abspath(os.getcwd())

class _base_setting:
     #Project Paths
     project_base_path= r"C:\Users\jafar\source\repos\VendorHUB\src\BcmLogicONE.VendorHUB.Application";
     #Template Paths
     tempate_base_path= currentPath+r"\configuration\Template"

class cqrs_command:
     _base_template_path = _base_setting.tempate_base_path + r"\CQRS"
     #templates
     handler_template_path =  _base_template_path + r"\command_handler.txt"
     command_template_path =  _base_template_path + r"\command.txt"
     #Project Paths
     commands_folder_path = _base_setting.project_base_path+r"\Commands"

class cqrs_query:
     _base_template_path = _base_setting.tempate_base_path + r"\CQRS"
     #templates
     handler_template_path =  _base_template_path + r"\query_handler.txt"
     queries_template_path =  _base_template_path + r"\query.txt"
     #Project Paths
     queries_folder_path = _base_setting.project_base_path+r"\Queries"

     

