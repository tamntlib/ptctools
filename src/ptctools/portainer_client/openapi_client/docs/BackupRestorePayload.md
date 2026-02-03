# BackupRestorePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_content** | **List[int]** |  | [optional] 
**file_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.backup_restore_payload import BackupRestorePayload

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRestorePayload from a JSON string
backup_restore_payload_instance = BackupRestorePayload.from_json(json)
# print the JSON string representation of the object
print(BackupRestorePayload.to_json())

# convert the object into a dict
backup_restore_payload_dict = backup_restore_payload_instance.to_dict()
# create an instance of BackupRestorePayload from a dict
backup_restore_payload_from_dict = BackupRestorePayload.from_dict(backup_restore_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


