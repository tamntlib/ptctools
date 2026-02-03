# PortainerHelmUserRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Membership Identifier | [optional] 
**url** | **str** | Helm repository URL | [optional] 
**user_id** | **int** | User identifier | [optional] 

## Example

```python
from openapi_client.models.portainer_helm_user_repository import PortainerHelmUserRepository

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerHelmUserRepository from a JSON string
portainer_helm_user_repository_instance = PortainerHelmUserRepository.from_json(json)
# print the JSON string representation of the object
print(PortainerHelmUserRepository.to_json())

# convert the object into a dict
portainer_helm_user_repository_dict = portainer_helm_user_repository_instance.to_dict()
# create an instance of PortainerHelmUserRepository from a dict
portainer_helm_user_repository_from_dict = PortainerHelmUserRepository.from_dict(portainer_helm_user_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


