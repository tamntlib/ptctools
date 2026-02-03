# KubernetesK8sRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **str** |  | [optional] 
**is_system** | **bool** | isSystem is true if prefixed with \&quot;system:\&quot; or exists in the kube-system namespace or is one of the portainer roles | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_role import KubernetesK8sRole

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sRole from a JSON string
kubernetes_k8s_role_instance = KubernetesK8sRole.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sRole.to_json())

# convert the object into a dict
kubernetes_k8s_role_dict = kubernetes_k8s_role_instance.to_dict()
# create an instance of KubernetesK8sRole from a dict
kubernetes_k8s_role_from_dict = KubernetesK8sRole.from_dict(kubernetes_k8s_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


