# KubernetesK8sApplicationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_limit** | **float** |  | [optional] 
**cpu_request** | **float** |  | [optional] 
**memory_limit** | **int** |  | [optional] 
**memory_request** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_application_resource import KubernetesK8sApplicationResource

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sApplicationResource from a JSON string
kubernetes_k8s_application_resource_instance = KubernetesK8sApplicationResource.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sApplicationResource.to_json())

# convert the object into a dict
kubernetes_k8s_application_resource_dict = kubernetes_k8s_application_resource_instance.to_dict()
# create an instance of KubernetesK8sApplicationResource from a dict
kubernetes_k8s_application_resource_from_dict = KubernetesK8sApplicationResource.from_dict(kubernetes_k8s_application_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


