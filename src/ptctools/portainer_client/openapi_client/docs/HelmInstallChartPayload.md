# HelmInstallChartPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atomic** | **bool** |  | [optional] 
**chart** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**repo** | **str** |  | [optional] 
**values** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.helm_install_chart_payload import HelmInstallChartPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HelmInstallChartPayload from a JSON string
helm_install_chart_payload_instance = HelmInstallChartPayload.from_json(json)
# print the JSON string representation of the object
print(HelmInstallChartPayload.to_json())

# convert the object into a dict
helm_install_chart_payload_dict = helm_install_chart_payload_instance.to_dict()
# create an instance of HelmInstallChartPayload from a dict
helm_install_chart_payload_from_dict = HelmInstallChartPayload.from_dict(helm_install_chart_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


