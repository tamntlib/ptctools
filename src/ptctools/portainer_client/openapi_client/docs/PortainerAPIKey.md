# PortainerAPIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **int** | Unix timestamp (UTC) when the API key was created | [optional] 
**description** | **str** |  | [optional] 
**digest** | **str** | Digest represents SHA256 hash of the raw API key | [optional] 
**id** | **int** |  | [optional] 
**last_used** | **int** | Unix timestamp (UTC) when the API key was last used | [optional] 
**prefix** | **str** | API key identifier (7 char prefix) | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_api_key import PortainerAPIKey

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerAPIKey from a JSON string
portainer_api_key_instance = PortainerAPIKey.from_json(json)
# print the JSON string representation of the object
print(PortainerAPIKey.to_json())

# convert the object into a dict
portainer_api_key_dict = portainer_api_key_instance.to_dict()
# create an instance of PortainerAPIKey from a dict
portainer_api_key_from_dict = PortainerAPIKey.from_dict(portainer_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


