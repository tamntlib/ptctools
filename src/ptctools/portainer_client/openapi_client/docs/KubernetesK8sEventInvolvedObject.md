# KubernetesK8sEventInvolvedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_event_involved_object import KubernetesK8sEventInvolvedObject

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sEventInvolvedObject from a JSON string
kubernetes_k8s_event_involved_object_instance = KubernetesK8sEventInvolvedObject.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sEventInvolvedObject.to_json())

# convert the object into a dict
kubernetes_k8s_event_involved_object_dict = kubernetes_k8s_event_involved_object_instance.to_dict()
# create an instance of KubernetesK8sEventInvolvedObject from a dict
kubernetes_k8s_event_involved_object_from_dict = KubernetesK8sEventInvolvedObject.from_dict(kubernetes_k8s_event_involved_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


