# TeamsTeamCreatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**team_leaders** | **List[int]** | TeamLeaders | [optional] 

## Example

```python
from openapi_client.models.teams_team_create_payload import TeamsTeamCreatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsTeamCreatePayload from a JSON string
teams_team_create_payload_instance = TeamsTeamCreatePayload.from_json(json)
# print the JSON string representation of the object
print(TeamsTeamCreatePayload.to_json())

# convert the object into a dict
teams_team_create_payload_dict = teams_team_create_payload_instance.to_dict()
# create an instance of TeamsTeamCreatePayload from a dict
teams_team_create_payload_from_dict = TeamsTeamCreatePayload.from_dict(teams_team_create_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


