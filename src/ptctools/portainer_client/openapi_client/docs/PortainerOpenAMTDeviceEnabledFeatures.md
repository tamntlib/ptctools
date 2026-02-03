# PortainerOpenAMTDeviceEnabledFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ider** | **bool** |  | [optional] 
**kvm** | **bool** |  | [optional] 
**sol** | **bool** |  | [optional] 
**redirection** | **bool** |  | [optional] 
**user_consent** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_open_amt_device_enabled_features import PortainerOpenAMTDeviceEnabledFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerOpenAMTDeviceEnabledFeatures from a JSON string
portainer_open_amt_device_enabled_features_instance = PortainerOpenAMTDeviceEnabledFeatures.from_json(json)
# print the JSON string representation of the object
print(PortainerOpenAMTDeviceEnabledFeatures.to_json())

# convert the object into a dict
portainer_open_amt_device_enabled_features_dict = portainer_open_amt_device_enabled_features_instance.to_dict()
# create an instance of PortainerOpenAMTDeviceEnabledFeatures from a dict
portainer_open_amt_device_enabled_features_from_dict = PortainerOpenAMTDeviceEnabledFeatures.from_dict(portainer_open_amt_device_enabled_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


