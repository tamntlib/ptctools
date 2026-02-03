# KubernetesIngressRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**tls** | [**List[KubernetesTLSInfo]**](KubernetesTLSInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_ingress_rule import KubernetesIngressRule

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesIngressRule from a JSON string
kubernetes_ingress_rule_instance = KubernetesIngressRule.from_json(json)
# print the JSON string representation of the object
print(KubernetesIngressRule.to_json())

# convert the object into a dict
kubernetes_ingress_rule_dict = kubernetes_ingress_rule_instance.to_dict()
# create an instance of KubernetesIngressRule from a dict
kubernetes_ingress_rule_from_dict = KubernetesIngressRule.from_dict(kubernetes_ingress_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


