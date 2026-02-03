# SslSslUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** | SSL Certificates | [optional] 
**httpenabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ssl_ssl_update_payload import SslSslUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of SslSslUpdatePayload from a JSON string
ssl_ssl_update_payload_instance = SslSslUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(SslSslUpdatePayload.to_json())

# convert the object into a dict
ssl_ssl_update_payload_dict = ssl_ssl_update_payload_instance.to_dict()
# create an instance of SslSslUpdatePayload from a dict
ssl_ssl_update_payload_from_dict = SslSslUpdatePayload.from_dict(ssl_ssl_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


