# AuthOauthPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | OAuth code returned from OAuth Provided | [optional] 

## Example

```python
from openapi_client.models.auth_oauth_payload import AuthOauthPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AuthOauthPayload from a JSON string
auth_oauth_payload_instance = AuthOauthPayload.from_json(json)
# print the JSON string representation of the object
print(AuthOauthPayload.to_json())

# convert the object into a dict
auth_oauth_payload_dict = auth_oauth_payload_instance.to_dict()
# create an instance of AuthOauthPayload from a dict
auth_oauth_payload_from_dict = AuthOauthPayload.from_dict(auth_oauth_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


