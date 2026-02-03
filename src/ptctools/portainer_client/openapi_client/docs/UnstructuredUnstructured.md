# UnstructuredUnstructured


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **Dict[str, object]** | Object is a JSON compatible map with string, float, int, bool, []interface{}, or map[string]interface{} children. | [optional] 

## Example

```python
from openapi_client.models.unstructured_unstructured import UnstructuredUnstructured

# TODO update the JSON string below
json = "{}"
# create an instance of UnstructuredUnstructured from a JSON string
unstructured_unstructured_instance = UnstructuredUnstructured.from_json(json)
# print the JSON string representation of the object
print(UnstructuredUnstructured.to_json())

# convert the object into a dict
unstructured_unstructured_dict = unstructured_unstructured_instance.to_dict()
# create an instance of UnstructuredUnstructured from a dict
unstructured_unstructured_from_dict = UnstructuredUnstructured.from_dict(unstructured_unstructured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


