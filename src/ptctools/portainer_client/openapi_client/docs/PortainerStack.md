# PortainerStack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_files** | **List[str]** | Only applies when deploying stack with multiple files | [optional] 
**auto_update** | [**PortainerAutoUpdateSettings**](PortainerAutoUpdateSettings.md) | The GitOps update settings of a git stack | [optional] 
**endpoint_id** | **int** | Environment(Endpoint) identifier. Reference the environment(endpoint) that will be used for deployment | [optional] 
**entry_point** | **str** | Path to the Stack file | [optional] 
**env** | [**List[PortainerPair]**](PortainerPair.md) | A list of environment(endpoint) variables used during stack deployment | [optional] 
**id** | **int** | Stack Identifier | [optional] 
**name** | **str** | Stack name | [optional] 
**option** | [**PortainerStackOption**](PortainerStackOption.md) | The stack deployment option | [optional] 
**resource_control** | [**PortainerResourceControl**](PortainerResourceControl.md) |  | [optional] 
**status** | [**PortainerStackStatus**](PortainerStackStatus.md) | Stack status (1 - active, 2 - inactive) | [optional] 
**swarm_id** | **str** | Cluster identifier of the Swarm cluster where the stack is deployed | [optional] 
**type** | [**PortainerStackType**](PortainerStackType.md) | Stack type. 1 for a Swarm stack, 2 for a Compose stack | [optional] 
**created_by** | **str** | The username which created this stack | [optional] 
**creation_date** | **int** | The date in unix time when stack was created | [optional] 
**from_app_template** | **bool** | Whether the stack is from a app template | [optional] 
**git_config** | [**GittypesRepoConfig**](GittypesRepoConfig.md) | The git config of this stack | [optional] 
**namespace** | **str** | Kubernetes namespace if stack is a kube application | [optional] 
**project_path** | **str** | Path on disk to the repository hosting the Stack file | [optional] 
**update_date** | **int** | The date in unix time when stack was last updated | [optional] 
**updated_by** | **str** | The username which last updated this stack | [optional] 

## Example

```python
from openapi_client.models.portainer_stack import PortainerStack

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerStack from a JSON string
portainer_stack_instance = PortainerStack.from_json(json)
# print the JSON string representation of the object
print(PortainerStack.to_json())

# convert the object into a dict
portainer_stack_dict = portainer_stack_instance.to_dict()
# create an instance of PortainerStack from a dict
portainer_stack_from_dict = PortainerStack.from_dict(portainer_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


