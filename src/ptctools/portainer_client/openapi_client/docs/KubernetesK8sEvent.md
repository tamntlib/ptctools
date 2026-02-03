# KubernetesK8sEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**event_time** | **str** |  | [optional] 
**first_timestamp** | **str** |  | [optional] 
**involved_object** | [**KubernetesK8sEventInvolvedObject**](KubernetesK8sEventInvolvedObject.md) |  | [optional] 
**kind** | **str** |  | [optional] 
**last_timestamp** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_event import KubernetesK8sEvent

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sEvent from a JSON string
kubernetes_k8s_event_instance = KubernetesK8sEvent.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sEvent.to_json())

# convert the object into a dict
kubernetes_k8s_event_dict = kubernetes_k8s_event_instance.to_dict()
# create an instance of KubernetesK8sEvent from a dict
kubernetes_k8s_event_from_dict = KubernetesK8sEvent.from_dict(kubernetes_k8s_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


