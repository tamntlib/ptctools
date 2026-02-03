# PortainerDiagnosticsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **Dict[str, str]** |  | [optional] 
**log** | **str** |  | [optional] 
**proxy** | **Dict[str, str]** |  | [optional] 
**telnet** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_diagnostics_data import PortainerDiagnosticsData

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerDiagnosticsData from a JSON string
portainer_diagnostics_data_instance = PortainerDiagnosticsData.from_json(json)
# print the JSON string representation of the object
print(PortainerDiagnosticsData.to_json())

# convert the object into a dict
portainer_diagnostics_data_dict = portainer_diagnostics_data_instance.to_dict()
# create an instance of PortainerDiagnosticsData from a dict
portainer_diagnostics_data_from_dict = PortainerDiagnosticsData.from_dict(portainer_diagnostics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


