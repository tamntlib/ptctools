# KubernetesK8sClusterRoleBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **str** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**role_ref** | [**V1RoleRef**](V1RoleRef.md) |  | [optional] 
**subjects** | [**List[K8sIoApiRbacV1Subject]**](K8sIoApiRbacV1Subject.md) |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_cluster_role_binding import KubernetesK8sClusterRoleBinding

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sClusterRoleBinding from a JSON string
kubernetes_k8s_cluster_role_binding_instance = KubernetesK8sClusterRoleBinding.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sClusterRoleBinding.to_json())

# convert the object into a dict
kubernetes_k8s_cluster_role_binding_dict = kubernetes_k8s_cluster_role_binding_instance.to_dict()
# create an instance of KubernetesK8sClusterRoleBinding from a dict
kubernetes_k8s_cluster_role_binding_from_dict = KubernetesK8sClusterRoleBinding.from_dict(kubernetes_k8s_cluster_role_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


