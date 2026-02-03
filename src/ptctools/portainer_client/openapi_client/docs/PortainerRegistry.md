# PortainerRegistry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Stores temporary access token | [optional] 
**access_token_expiry** | **int** |  | [optional] 
**authentication** | **bool** | Is authentication against this registry enabled | [optional] 
**authorized_teams** | **List[int]** | Deprecated in DBVersion &#x3D;&#x3D; 18 | [optional] 
**authorized_users** | **List[int]** | Deprecated in DBVersion &#x3D;&#x3D; 18 | [optional] 
**base_url** | **str** | Base URL, introduced for ProGet registry | [optional] 
**ecr** | [**PortainerEcrData**](PortainerEcrData.md) |  | [optional] 
**github** | [**PortainerGithubRegistryData**](PortainerGithubRegistryData.md) |  | [optional] 
**gitlab** | [**PortainerGitlabRegistryData**](PortainerGitlabRegistryData.md) |  | [optional] 
**id** | **int** | Registry Identifier | [optional] 
**management_configuration** | [**PortainerRegistryManagementConfiguration**](PortainerRegistryManagementConfiguration.md) |  | [optional] 
**name** | **str** | Registry Name | [optional] 
**password** | **str** | Password or SecretAccessKey used to authenticate against this registry | [optional] 
**quay** | [**PortainerQuayRegistryData**](PortainerQuayRegistryData.md) |  | [optional] 
**registry_accesses** | [**Dict[str, PortainerRegistryAccessPolicies]**](PortainerRegistryAccessPolicies.md) |  | [optional] 
**team_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) | Deprecated in DBVersion &#x3D;&#x3D; 31 | [optional] 
**type** | [**PortainerRegistryType**](PortainerRegistryType.md) | Registry Type (1 - Quay, 2 - Azure, 3 - Custom, 4 - Gitlab, 5 - ProGet, 6 - DockerHub, 7 - ECR) | [optional] 
**url** | **str** | URL or IP address of the Docker registry | [optional] 
**user_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) | Deprecated fields Deprecated in DBVersion &#x3D;&#x3D; 31 | [optional] 
**username** | **str** | Username or AccessKeyID used to authenticate against this registry | [optional] 

## Example

```python
from openapi_client.models.portainer_registry import PortainerRegistry

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerRegistry from a JSON string
portainer_registry_instance = PortainerRegistry.from_json(json)
# print the JSON string representation of the object
print(PortainerRegistry.to_json())

# convert the object into a dict
portainer_registry_dict = portainer_registry_instance.to_dict()
# create an instance of PortainerRegistry from a dict
portainer_registry_from_dict = PortainerRegistry.from_dict(portainer_registry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


