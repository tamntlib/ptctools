# PortainerKubernetesStorageClassConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** |  | [optional] 
**allow_volume_expansion** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**provisioner** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_kubernetes_storage_class_config import PortainerKubernetesStorageClassConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerKubernetesStorageClassConfig from a JSON string
portainer_kubernetes_storage_class_config_instance = PortainerKubernetesStorageClassConfig.from_json(json)
# print the JSON string representation of the object
print(PortainerKubernetesStorageClassConfig.to_json())

# convert the object into a dict
portainer_kubernetes_storage_class_config_dict = portainer_kubernetes_storage_class_config_instance.to_dict()
# create an instance of PortainerKubernetesStorageClassConfig from a dict
portainer_kubernetes_storage_class_config_from_dict = PortainerKubernetesStorageClassConfig.from_dict(portainer_kubernetes_storage_class_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


