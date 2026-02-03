# PortainerK8sNamespaceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**creation_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace_owner** | **str** |  | [optional] 
**resource_quota** | [**V1ResourceQuota**](V1ResourceQuota.md) |  | [optional] 
**status** | [**V1NamespaceStatus**](V1NamespaceStatus.md) |  | [optional] 
**unhealthy_event_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_k8s_namespace_info import PortainerK8sNamespaceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerK8sNamespaceInfo from a JSON string
portainer_k8s_namespace_info_instance = PortainerK8sNamespaceInfo.from_json(json)
# print the JSON string representation of the object
print(PortainerK8sNamespaceInfo.to_json())

# convert the object into a dict
portainer_k8s_namespace_info_dict = portainer_k8s_namespace_info_instance.to_dict()
# create an instance of PortainerK8sNamespaceInfo from a dict
portainer_k8s_namespace_info_from_dict = PortainerK8sNamespaceInfo.from_dict(portainer_k8s_namespace_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


