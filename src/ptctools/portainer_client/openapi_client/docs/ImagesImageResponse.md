# ImagesImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**node_name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**used** | **bool** | Used is true if the image is used by at least one container supplied only when withUsage is true | [optional] 

## Example

```python
from openapi_client.models.images_image_response import ImagesImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesImageResponse from a JSON string
images_image_response_instance = ImagesImageResponse.from_json(json)
# print the JSON string representation of the object
print(ImagesImageResponse.to_json())

# convert the object into a dict
images_image_response_dict = images_image_response_instance.to_dict()
# create an instance of ImagesImageResponse from a dict
images_image_response_from_dict = ImagesImageResponse.from_dict(images_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


