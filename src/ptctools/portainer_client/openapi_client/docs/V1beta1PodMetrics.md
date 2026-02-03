# V1beta1PodMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources +optional | [optional] 
**containers** | [**List[V1beta1ContainerMetrics]**](V1beta1ContainerMetrics.md) | Metrics for all containers are collected within the same time window. +listType&#x3D;atomic | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds +optional | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata +optional | [optional] 
**timestamp** | **str** | The following fields define time interval from which metrics were collected from the interval [Timestamp-Window, Timestamp]. | [optional] 
**window** | [**V1Duration**](V1Duration.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1beta1_pod_metrics import V1beta1PodMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PodMetrics from a JSON string
v1beta1_pod_metrics_instance = V1beta1PodMetrics.from_json(json)
# print the JSON string representation of the object
print(V1beta1PodMetrics.to_json())

# convert the object into a dict
v1beta1_pod_metrics_dict = v1beta1_pod_metrics_instance.to_dict()
# create an instance of V1beta1PodMetrics from a dict
v1beta1_pod_metrics_from_dict = V1beta1PodMetrics.from_dict(v1beta1_pod_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


