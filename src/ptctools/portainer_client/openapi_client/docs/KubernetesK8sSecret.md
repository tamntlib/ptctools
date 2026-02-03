# KubernetesK8sSecret


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
**secret_type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_secret import KubernetesK8sSecret

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sSecret from a JSON string
kubernetes_k8s_secret_instance = KubernetesK8sSecret.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sSecret.to_json())

# convert the object into a dict
kubernetes_k8s_secret_dict = kubernetes_k8s_secret_instance.to_dict()
# create an instance of KubernetesK8sSecret from a dict
kubernetes_k8s_secret_from_dict = KubernetesK8sSecret.from_dict(kubernetes_k8s_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


