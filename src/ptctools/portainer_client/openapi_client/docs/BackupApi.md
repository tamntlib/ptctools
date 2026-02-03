# openapi_client.BackupApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup**](BackupApi.md#backup) | **POST** /backup | Creates an archive with a system data snapshot that could be used to restore the system.
[**restore**](BackupApi.md#restore) | **POST** /restore | Triggers a system restore using provided backup file


# **backup**
> backup(body=body)

Creates an archive with a system data snapshot that could be used to restore the system.

Creates an archive with a system data snapshot that could be used to restore the system.
**Access policy**: admin

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.backup_backup_payload import BackupBackupPayload
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BackupApi(api_client)
    body = openapi_client.BackupBackupPayload() # BackupBackupPayload | An object contains the password to encrypt the backup with (optional)

    try:
        # Creates an archive with a system data snapshot that could be used to restore the system.
        api_instance.backup(body=body)
    except Exception as e:
        print("Exception when calling BackupApi->backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupBackupPayload**](BackupBackupPayload.md)| An object contains the password to encrypt the backup with | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore**
> restore(restore_payload)

Triggers a system restore using provided backup file

Triggers a system restore using provided backup file
**Access policy**: public

### Example


```python
import openapi_client
from openapi_client.models.backup_restore_payload import BackupRestorePayload
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BackupApi(api_client)
    restore_payload = openapi_client.BackupRestorePayload() # BackupRestorePayload | Restore request payload

    try:
        # Triggers a system restore using provided backup file
        api_instance.restore(restore_payload)
    except Exception as e:
        print("Exception when calling BackupApi->restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_payload** | [**BackupRestorePayload**](BackupRestorePayload.md)| Restore request payload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

