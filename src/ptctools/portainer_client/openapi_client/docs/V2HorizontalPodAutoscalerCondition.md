# V2HorizontalPodAutoscalerCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **str** | lastTransitionTime is the last time the condition transitioned from one status to another +optional | [optional] 
**message** | **str** | message is a human-readable explanation containing details about the transition +optional | [optional] 
**reason** | **str** | reason is the reason for the condition&#39;s last transition. +optional | [optional] 
**status** | [**K8sIoApiCoreV1ConditionStatus**](K8sIoApiCoreV1ConditionStatus.md) | status is the status of the condition (True, False, Unknown) | [optional] 
**type** | [**V2HorizontalPodAutoscalerConditionType**](V2HorizontalPodAutoscalerConditionType.md) | type describes the current condition | [optional] 

## Example

```python
from openapi_client.models.v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V2HorizontalPodAutoscalerCondition from a JSON string
v2_horizontal_pod_autoscaler_condition_instance = V2HorizontalPodAutoscalerCondition.from_json(json)
# print the JSON string representation of the object
print(V2HorizontalPodAutoscalerCondition.to_json())

# convert the object into a dict
v2_horizontal_pod_autoscaler_condition_dict = v2_horizontal_pod_autoscaler_condition_instance.to_dict()
# create an instance of V2HorizontalPodAutoscalerCondition from a dict
v2_horizontal_pod_autoscaler_condition_from_dict = V2HorizontalPodAutoscalerCondition.from_dict(v2_horizontal_pod_autoscaler_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


