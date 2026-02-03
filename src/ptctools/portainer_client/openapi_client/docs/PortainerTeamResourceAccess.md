# PortainerTeamResourceAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**PortainerResourceAccessLevel**](PortainerResourceAccessLevel.md) |  | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_team_resource_access import PortainerTeamResourceAccess

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTeamResourceAccess from a JSON string
portainer_team_resource_access_instance = PortainerTeamResourceAccess.from_json(json)
# print the JSON string representation of the object
print(PortainerTeamResourceAccess.to_json())

# convert the object into a dict
portainer_team_resource_access_dict = portainer_team_resource_access_instance.to_dict()
# create an instance of PortainerTeamResourceAccess from a dict
portainer_team_resource_access_from_dict = PortainerTeamResourceAccess.from_dict(portainer_team_resource_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


