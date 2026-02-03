# KubernetesPublishedPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingress_rules** | [**List[KubernetesIngressRule]**](KubernetesIngressRule.md) |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_published_port import KubernetesPublishedPort

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesPublishedPort from a JSON string
kubernetes_published_port_instance = KubernetesPublishedPort.from_json(json)
# print the JSON string representation of the object
print(KubernetesPublishedPort.to_json())

# convert the object into a dict
kubernetes_published_port_dict = kubernetes_published_port_instance.to_dict()
# create an instance of KubernetesPublishedPort from a dict
kubernetes_published_port_from_dict = KubernetesPublishedPort.from_dict(kubernetes_published_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


