# PortainerTeamMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Membership Identifier | [optional] 
**role** | [**PortainerMembershipRole**](PortainerMembershipRole.md) | Team role (1 for team leader and 2 for team member) | [optional] 
**team_id** | **int** | Team identifier | [optional] 
**user_id** | **int** | User identifier | [optional] 

## Example

```python
from openapi_client.models.portainer_team_membership import PortainerTeamMembership

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTeamMembership from a JSON string
portainer_team_membership_instance = PortainerTeamMembership.from_json(json)
# print the JSON string representation of the object
print(PortainerTeamMembership.to_json())

# convert the object into a dict
portainer_team_membership_dict = portainer_team_membership_instance.to_dict()
# create an instance of PortainerTeamMembership from a dict
portainer_team_membership_from_dict = PortainerTeamMembership.from_dict(portainer_team_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


