# AuthAuthenticateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | JWT token used to authenticate against the API | [optional] 

## Example

```python
from openapi_client.models.auth_authenticate_response import AuthAuthenticateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAuthenticateResponse from a JSON string
auth_authenticate_response_instance = AuthAuthenticateResponse.from_json(json)
# print the JSON string representation of the object
print(AuthAuthenticateResponse.to_json())

# convert the object into a dict
auth_authenticate_response_dict = auth_authenticate_response_instance.to_dict()
# create an instance of AuthAuthenticateResponse from a dict
auth_authenticate_response_from_dict = AuthAuthenticateResponse.from_dict(auth_authenticate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


