# KubernetesK8sConfigMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**configuration_owner** | **str** |  | [optional] 
**configuration_owner_id** | **str** |  | [optional] 
**configuration_owners** | [**List[KubernetesK8sConfigurationOwnerResource]**](KubernetesK8sConfigurationOwnerResource.md) |  | [optional] 
**creation_date** | **str** |  | [optional] 
**data** | **Dict[str, str]** |  | [optional] 
**is_used** | **bool** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_config_map import KubernetesK8sConfigMap

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sConfigMap from a JSON string
kubernetes_k8s_config_map_instance = KubernetesK8sConfigMap.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sConfigMap.to_json())

# convert the object into a dict
kubernetes_k8s_config_map_dict = kubernetes_k8s_config_map_instance.to_dict()
# create an instance of KubernetesK8sConfigMap from a dict
kubernetes_k8s_config_map_from_dict = KubernetesK8sConfigMap.from_dict(kubernetes_k8s_config_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


