# KubernetesNamespacesToggleSystemPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system** | **bool** | Toggle the system state of this namespace to true or false | [optional] 

## Example

```python
from openapi_client.models.kubernetes_namespaces_toggle_system_payload import KubernetesNamespacesToggleSystemPayload

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNamespacesToggleSystemPayload from a JSON string
kubernetes_namespaces_toggle_system_payload_instance = KubernetesNamespacesToggleSystemPayload.from_json(json)
# print the JSON string representation of the object
print(KubernetesNamespacesToggleSystemPayload.to_json())

# convert the object into a dict
kubernetes_namespaces_toggle_system_payload_dict = kubernetes_namespaces_toggle_system_payload_instance.to_dict()
# create an instance of KubernetesNamespacesToggleSystemPayload from a dict
kubernetes_namespaces_toggle_system_payload_from_dict = KubernetesNamespacesToggleSystemPayload.from_dict(kubernetes_namespaces_toggle_system_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


