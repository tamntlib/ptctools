# V1ScopedResourceSelectorRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**V1ScopeSelectorOperator**](V1ScopeSelectorOperator.md) | Represents a scope&#39;s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. | [optional] 
**scope_name** | [**V1ResourceQuotaScope**](V1ResourceQuotaScope.md) | The name of the scope that the selector applies to. | [optional] 
**values** | **List[str]** | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. +optional +listType&#x3D;atomic | [optional] 

## Example

```python
from openapi_client.models.v1_scoped_resource_selector_requirement import V1ScopedResourceSelectorRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of V1ScopedResourceSelectorRequirement from a JSON string
v1_scoped_resource_selector_requirement_instance = V1ScopedResourceSelectorRequirement.from_json(json)
# print the JSON string representation of the object
print(V1ScopedResourceSelectorRequirement.to_json())

# convert the object into a dict
v1_scoped_resource_selector_requirement_dict = v1_scoped_resource_selector_requirement_instance.to_dict()
# create an instance of V1ScopedResourceSelectorRequirement from a dict
v1_scoped_resource_selector_requirement_from_dict = V1ScopedResourceSelectorRequirement.from_dict(v1_scoped_resource_selector_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


