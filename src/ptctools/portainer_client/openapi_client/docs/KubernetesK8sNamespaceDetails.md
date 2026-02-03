# KubernetesK8sNamespaceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**resource_quota** | [**KubernetesK8sResourceQuota**](KubernetesK8sResourceQuota.md) |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_namespace_details import KubernetesK8sNamespaceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sNamespaceDetails from a JSON string
kubernetes_k8s_namespace_details_instance = KubernetesK8sNamespaceDetails.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sNamespaceDetails.to_json())

# convert the object into a dict
kubernetes_k8s_namespace_details_dict = kubernetes_k8s_namespace_details_instance.to_dict()
# create an instance of KubernetesK8sNamespaceDetails from a dict
kubernetes_k8s_namespace_details_from_dict = KubernetesK8sNamespaceDetails.from_dict(kubernetes_k8s_namespace_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


