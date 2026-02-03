# KubernetesConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_owner** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**kind** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_configuration import KubernetesConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesConfiguration from a JSON string
kubernetes_configuration_instance = KubernetesConfiguration.from_json(json)
# print the JSON string representation of the object
print(KubernetesConfiguration.to_json())

# convert the object into a dict
kubernetes_configuration_dict = kubernetes_configuration_instance.to_dict()
# create an instance of KubernetesConfiguration from a dict
kubernetes_configuration_from_dict = KubernetesConfiguration.from_dict(kubernetes_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


