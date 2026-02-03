# AuthAuthenticatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password | 
**username** | **str** | Username | 

## Example

```python
from openapi_client.models.auth_authenticate_payload import AuthAuthenticatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAuthenticatePayload from a JSON string
auth_authenticate_payload_instance = AuthAuthenticatePayload.from_json(json)
# print the JSON string representation of the object
print(AuthAuthenticatePayload.to_json())

# convert the object into a dict
auth_authenticate_payload_dict = auth_authenticate_payload_instance.to_dict()
# create an instance of AuthAuthenticatePayload from a dict
auth_authenticate_payload_from_dict = AuthAuthenticatePayload.from_dict(auth_authenticate_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


