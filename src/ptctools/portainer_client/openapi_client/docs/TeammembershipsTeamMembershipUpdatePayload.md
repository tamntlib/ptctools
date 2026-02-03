# TeammembershipsTeamMembershipUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **int** | Role for the user inside the team (1 for leader and 2 for regular member) | 
**team_id** | **int** | Team identifier | 
**user_id** | **int** | User identifier | 

## Example

```python
from openapi_client.models.teammemberships_team_membership_update_payload import TeammembershipsTeamMembershipUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of TeammembershipsTeamMembershipUpdatePayload from a JSON string
teammemberships_team_membership_update_payload_instance = TeammembershipsTeamMembershipUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(TeammembershipsTeamMembershipUpdatePayload.to_json())

# convert the object into a dict
teammemberships_team_membership_update_payload_dict = teammemberships_team_membership_update_payload_instance.to_dict()
# create an instance of TeammembershipsTeamMembershipUpdatePayload from a dict
teammemberships_team_membership_update_payload_from_dict = TeammembershipsTeamMembershipUpdatePayload.from_dict(teammemberships_team_membership_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


