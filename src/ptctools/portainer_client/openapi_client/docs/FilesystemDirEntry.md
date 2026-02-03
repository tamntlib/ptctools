# FilesystemDirEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**is_file** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | [**OsFileMode**](OsFileMode.md) |  | [optional] 

## Example

```python
from openapi_client.models.filesystem_dir_entry import FilesystemDirEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemDirEntry from a JSON string
filesystem_dir_entry_instance = FilesystemDirEntry.from_json(json)
# print the JSON string representation of the object
print(FilesystemDirEntry.to_json())

# convert the object into a dict
filesystem_dir_entry_dict = filesystem_dir_entry_instance.to_dict()
# create an instance of FilesystemDirEntry from a dict
filesystem_dir_entry_from_dict = FilesystemDirEntry.from_dict(filesystem_dir_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


