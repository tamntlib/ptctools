# KubernetesK8sRoleBinding


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
from openapi_client.models.kubernetes_k8s_role_binding import KubernetesK8sRoleBinding

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sRoleBinding from a JSON string
kubernetes_k8s_role_binding_instance = KubernetesK8sRoleBinding.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sRoleBinding.to_json())

# convert the object into a dict
kubernetes_k8s_role_binding_dict = kubernetes_k8s_role_binding_instance.to_dict()
# create an instance of KubernetesK8sRoleBinding from a dict
kubernetes_k8s_role_binding_from_dict = KubernetesK8sRoleBinding.from_dict(kubernetes_k8s_role_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


