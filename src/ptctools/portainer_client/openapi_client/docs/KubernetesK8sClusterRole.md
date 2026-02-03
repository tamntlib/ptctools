# KubernetesK8sClusterRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **str** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_cluster_role import KubernetesK8sClusterRole

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sClusterRole from a JSON string
kubernetes_k8s_cluster_role_instance = KubernetesK8sClusterRole.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sClusterRole.to_json())

# convert the object into a dict
kubernetes_k8s_cluster_role_dict = kubernetes_k8s_cluster_role_instance.to_dict()
# create an instance of KubernetesK8sClusterRole from a dict
kubernetes_k8s_cluster_role_from_dict = KubernetesK8sClusterRole.from_dict(kubernetes_k8s_cluster_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


