# PortainerEndpointPostInitMigrations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrate_gpus** | **bool** |  | [optional] 
**migrate_ingresses** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_endpoint_post_init_migrations import PortainerEndpointPostInitMigrations

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEndpointPostInitMigrations from a JSON string
portainer_endpoint_post_init_migrations_instance = PortainerEndpointPostInitMigrations.from_json(json)
# print the JSON string representation of the object
print(PortainerEndpointPostInitMigrations.to_json())

# convert the object into a dict
portainer_endpoint_post_init_migrations_dict = portainer_endpoint_post_init_migrations_instance.to_dict()
# create an instance of PortainerEndpointPostInitMigrations from a dict
portainer_endpoint_post_init_migrations_from_dict = PortainerEndpointPostInitMigrations.from_dict(portainer_endpoint_post_init_migrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


