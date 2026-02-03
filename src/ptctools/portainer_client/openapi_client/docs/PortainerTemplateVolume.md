# PortainerTemplateVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind** | **str** | Path on the host | [optional] 
**container** | **str** | Path inside the container | [optional] 
**readonly** | **bool** | Whether the volume used should be readonly | [optional] 

## Example

```python
from openapi_client.models.portainer_template_volume import PortainerTemplateVolume

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTemplateVolume from a JSON string
portainer_template_volume_instance = PortainerTemplateVolume.from_json(json)
# print the JSON string representation of the object
print(PortainerTemplateVolume.to_json())

# convert the object into a dict
portainer_template_volume_dict = portainer_template_volume_instance.to_dict()
# create an instance of PortainerTemplateVolume from a dict
portainer_template_volume_from_dict = PortainerTemplateVolume.from_dict(portainer_template_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


