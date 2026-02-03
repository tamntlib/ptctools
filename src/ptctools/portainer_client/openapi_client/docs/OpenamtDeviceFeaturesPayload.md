# OpenamtDeviceFeaturesPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**PortainerOpenAMTDeviceEnabledFeatures**](PortainerOpenAMTDeviceEnabledFeatures.md) |  | [optional] 

## Example

```python
from openapi_client.models.openamt_device_features_payload import OpenamtDeviceFeaturesPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OpenamtDeviceFeaturesPayload from a JSON string
openamt_device_features_payload_instance = OpenamtDeviceFeaturesPayload.from_json(json)
# print the JSON string representation of the object
print(OpenamtDeviceFeaturesPayload.to_json())

# convert the object into a dict
openamt_device_features_payload_dict = openamt_device_features_payload_instance.to_dict()
# create an instance of OpenamtDeviceFeaturesPayload from a dict
openamt_device_features_payload_from_dict = OpenamtDeviceFeaturesPayload.from_dict(openamt_device_features_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


