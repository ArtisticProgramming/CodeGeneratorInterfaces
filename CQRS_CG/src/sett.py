
from configuration.setting import EntitySchemaConfiguration, IRepository, _base_setting, cqrs_command,cqrs_query,repository

print(__name__)

class sett:
    base = _base_setting
    cqrs_command = cqrs_command
    cqrs_query = cqrs_query
    repository = repository
    repository_interfae = IRepository
    entitySchemaConfiguration=EntitySchemaConfiguration

