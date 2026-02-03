# PortainerOpenAMTConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_file_content** | **str** |  | [optional] 
**cert_file_name** | **str** |  | [optional] 
**cert_file_password** | **str** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**mps_password** | **str** |  | [optional] 
**mps_server** | **str** |  | [optional] 
**mps_token** | **str** | retrieved from API | [optional] 
**mps_user** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_open_amt_configuration import PortainerOpenAMTConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerOpenAMTConfiguration from a JSON string
portainer_open_amt_configuration_instance = PortainerOpenAMTConfiguration.from_json(json)
# print the JSON string representation of the object
print(PortainerOpenAMTConfiguration.to_json())

# convert the object into a dict
portainer_open_amt_configuration_dict = portainer_open_amt_configuration_instance.to_dict()
# create an instance of PortainerOpenAMTConfiguration from a dict
portainer_open_amt_configuration_from_dict = PortainerOpenAMTConfiguration.from_dict(portainer_open_amt_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


