# UsersAccessTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**PortainerAPIKey**](PortainerAPIKey.md) |  | [optional] 
**raw_api_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.users_access_token_response import UsersAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAccessTokenResponse from a JSON string
users_access_token_response_instance = UsersAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(UsersAccessTokenResponse.to_json())

# convert the object into a dict
users_access_token_response_dict = users_access_token_response_instance.to_dict()
# create an instance of UsersAccessTokenResponse from a dict
users_access_token_response_from_dict = UsersAccessTokenResponse.from_dict(users_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


