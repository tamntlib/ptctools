# PortainerTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Team Identifier | [optional] 
**name** | **str** | Team name | [optional] 

## Example

```python
from openapi_client.models.portainer_team import PortainerTeam

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTeam from a JSON string
portainer_team_instance = PortainerTeam.from_json(json)
# print the JSON string representation of the object
print(PortainerTeam.to_json())

# convert the object into a dict
portainer_team_dict = portainer_team_instance.to_dict()
# create an instance of PortainerTeam from a dict
portainer_team_from_dict = PortainerTeam.from_dict(portainer_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


