# TemplatesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[PortainerTemplate]**](PortainerTemplate.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.templates_list_response import TemplatesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesListResponse from a JSON string
templates_list_response_instance = TemplatesListResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatesListResponse.to_json())

# convert the object into a dict
templates_list_response_dict = templates_list_response_instance.to_dict()
# create an instance of TemplatesListResponse from a dict
templates_list_response_from_dict = TemplatesListResponse.from_dict(templates_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


