# MotdMotdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_layout** | **Dict[str, str]** |  | [optional] 
**hash** | **List[int]** |  | [optional] 
**message** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.motd_motd_response import MotdMotdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MotdMotdResponse from a JSON string
motd_motd_response_instance = MotdMotdResponse.from_json(json)
# print the JSON string representation of the object
print(MotdMotdResponse.to_json())

# convert the object into a dict
motd_motd_response_dict = motd_motd_response_instance.to_dict()
# create an instance of MotdMotdResponse from a dict
motd_motd_response_from_dict = MotdMotdResponse.from_dict(motd_motd_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


