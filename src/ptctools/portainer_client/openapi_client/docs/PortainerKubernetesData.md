# PortainerKubernetesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**PortainerKubernetesConfiguration**](PortainerKubernetesConfiguration.md) |  | [optional] 
**flags** | [**PortainerKubernetesFlags**](PortainerKubernetesFlags.md) |  | [optional] 
**snapshots** | [**List[PortainerKubernetesSnapshot]**](PortainerKubernetesSnapshot.md) |  | [optional] 

## Example

```python
from openapi_client.models.portainer_kubernetes_data import PortainerKubernetesData

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerKubernetesData from a JSON string
portainer_kubernetes_data_instance = PortainerKubernetesData.from_json(json)
# print the JSON string representation of the object
print(PortainerKubernetesData.to_json())

# convert the object into a dict
portainer_kubernetes_data_dict = portainer_kubernetes_data_instance.to_dict()
# create an instance of PortainerKubernetesData from a dict
portainer_kubernetes_data_from_dict = PortainerKubernetesData.from_dict(portainer_kubernetes_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


