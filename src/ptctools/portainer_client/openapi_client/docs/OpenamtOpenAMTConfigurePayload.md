# OpenamtOpenAMTConfigurePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_file_content** | **str** |  | [optional] 
**cert_file_name** | **str** |  | [optional] 
**cert_file_password** | **str** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**mpspassword** | **str** |  | [optional] 
**mpsserver** | **str** |  | [optional] 
**mpsuser** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.openamt_open_amt_configure_payload import OpenamtOpenAMTConfigurePayload

# TODO update the JSON string below
json = "{}"
# create an instance of OpenamtOpenAMTConfigurePayload from a JSON string
openamt_open_amt_configure_payload_instance = OpenamtOpenAMTConfigurePayload.from_json(json)
# print the JSON string representation of the object
print(OpenamtOpenAMTConfigurePayload.to_json())

# convert the object into a dict
openamt_open_amt_configure_payload_dict = openamt_open_amt_configure_payload_instance.to_dict()
# create an instance of OpenamtOpenAMTConfigurePayload from a dict
openamt_open_amt_configure_payload_from_dict = OpenamtOpenAMTConfigurePayload.from_dict(openamt_open_amt_configure_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


