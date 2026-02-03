# KubernetesK8sConfigurationOwnerResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**resource_kind** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_configuration_owner_resource import KubernetesK8sConfigurationOwnerResource

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sConfigurationOwnerResource from a JSON string
kubernetes_k8s_configuration_owner_resource_instance = KubernetesK8sConfigurationOwnerResource.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sConfigurationOwnerResource.to_json())

# convert the object into a dict
kubernetes_k8s_configuration_owner_resource_dict = kubernetes_k8s_configuration_owner_resource_instance.to_dict()
# create an instance of KubernetesK8sConfigurationOwnerResource from a dict
kubernetes_k8s_configuration_owner_resource_from_dict = KubernetesK8sConfigurationOwnerResource.from_dict(kubernetes_k8s_configuration_owner_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


