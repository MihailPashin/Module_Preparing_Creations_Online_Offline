from dependency_injector import containers, providers
from Topics.ECB_control_themes import Group,GroupInterface,GroupControl
from Topics.topics_themes import dict_for_razmetka

class Topic_Container(containers.DeclarativeContainer):
    
    topics_data = providers.Object(dict_for_razmetka)
    group_control = providers.Factory(GroupControl, data=topics_data)
    group_boundary = providers.Factory(GroupInterface, control=group_control)
