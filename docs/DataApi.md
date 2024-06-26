# permify_async.DataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_run**](DataApi.md#bundle_run) | **POST** /v1/tenants/{tenant_id}/data/run-bundle | run bundle
[**data_attributes_read**](DataApi.md#data_attributes_read) | **POST** /v1/tenants/{tenant_id}/data/attributes/read | read attributes
[**data_delete**](DataApi.md#data_delete) | **POST** /v1/tenants/{tenant_id}/data/delete | delete data
[**data_relationships_read**](DataApi.md#data_relationships_read) | **POST** /v1/tenants/{tenant_id}/data/relationships/read | read relationships
[**data_write**](DataApi.md#data_write) | **POST** /v1/tenants/{tenant_id}/data/write | write data
[**relationships_delete**](DataApi.md#relationships_delete) | **POST** /v1/tenants/{tenant_id}/relationships/delete | delete relationships
[**relationships_write**](DataApi.md#relationships_write) | **POST** /v1/tenants/{tenant_id}/relationships/write | write relationships


# **bundle_run**
> BundleRunResponse bundle_run(tenant_id, body)

run bundle

### Example


```python
import permify_async
from permify_async.models.bundle_run_request import BundleRunRequest
from permify_async.models.bundle_run_response import BundleRunResponse
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.BundleRunRequest() # BundleRunRequest | 

    try:
        # run bundle
        api_response = await api_instance.bundle_run(tenant_id, body)
        print("The response of DataApi->bundle_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->bundle_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**BundleRunRequest**](BundleRunRequest.md)|  | 

### Return type

[**BundleRunResponse**](BundleRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_attributes_read**
> AttributeReadResponse data_attributes_read(tenant_id, body)

read attributes

### Example


```python
import permify_async
from permify_async.models.attribute_read_response import AttributeReadResponse
from permify_async.models.data_attributes_read_request import DataAttributesReadRequest
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.DataAttributesReadRequest() # DataAttributesReadRequest | 

    try:
        # read attributes
        api_response = await api_instance.data_attributes_read(tenant_id, body)
        print("The response of DataApi->data_attributes_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_attributes_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**DataAttributesReadRequest**](DataAttributesReadRequest.md)|  | 

### Return type

[**AttributeReadResponse**](AttributeReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_delete**
> DataDeleteResponse data_delete(tenant_id, body)

delete data

### Example


```python
import permify_async
from permify_async.models.data_delete_request import DataDeleteRequest
from permify_async.models.data_delete_response import DataDeleteResponse
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.DataDeleteRequest() # DataDeleteRequest | 

    try:
        # delete data
        api_response = await api_instance.data_delete(tenant_id, body)
        print("The response of DataApi->data_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**DataDeleteRequest**](DataDeleteRequest.md)|  | 

### Return type

[**DataDeleteResponse**](DataDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_relationships_read**
> RelationshipReadResponse data_relationships_read(tenant_id, body)

read relationships

### Example


```python
import permify_async
from permify_async.models.data_relationships_read_request import DataRelationshipsReadRequest
from permify_async.models.relationship_read_response import RelationshipReadResponse
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.DataRelationshipsReadRequest() # DataRelationshipsReadRequest | 

    try:
        # read relationships
        api_response = await api_instance.data_relationships_read(tenant_id, body)
        print("The response of DataApi->data_relationships_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_relationships_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**DataRelationshipsReadRequest**](DataRelationshipsReadRequest.md)|  | 

### Return type

[**RelationshipReadResponse**](RelationshipReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_write**
> DataWriteResponse data_write(tenant_id, body)

write data

### Example


```python
import permify_async
from permify_async.models.data_write_request import DataWriteRequest
from permify_async.models.data_write_response import DataWriteResponse
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.DataWriteRequest() # DataWriteRequest | 

    try:
        # write data
        api_response = await api_instance.data_write(tenant_id, body)
        print("The response of DataApi->data_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**DataWriteRequest**](DataWriteRequest.md)|  | 

### Return type

[**DataWriteResponse**](DataWriteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relationships_delete**
> RelationshipDeleteResponse relationships_delete(tenant_id, body)

delete relationships

### Example


```python
import permify_async
from permify_async.models.relationship_delete_request import RelationshipDeleteRequest
from permify_async.models.relationship_delete_response import RelationshipDeleteResponse
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.RelationshipDeleteRequest() # RelationshipDeleteRequest | 

    try:
        # delete relationships
        api_response = await api_instance.relationships_delete(tenant_id, body)
        print("The response of DataApi->relationships_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->relationships_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**RelationshipDeleteRequest**](RelationshipDeleteRequest.md)|  | 

### Return type

[**RelationshipDeleteResponse**](RelationshipDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relationships_write**
> RelationshipWriteResponse relationships_write(tenant_id, body)

write relationships

### Example


```python
import permify_async
from permify_async.models.relationship_write_response import RelationshipWriteResponse
from permify_async.models.relationships_write_request import RelationshipsWriteRequest
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.RelationshipsWriteRequest() # RelationshipsWriteRequest | 

    try:
        # write relationships
        api_response = await api_instance.relationships_write(tenant_id, body)
        print("The response of DataApi->relationships_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->relationships_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**RelationshipsWriteRequest**](RelationshipsWriteRequest.md)|  | 

### Return type

[**RelationshipWriteResponse**](RelationshipWriteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

