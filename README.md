# permify-async
Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.2.3
- Package version: 1.0.0
- Generator version: 7.11.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/Permify/permify/issues](https://github.com/Permify/permify/issues)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/mmx86/python-async-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mmx86/python-async-python.git`)

Then import the package:
```python
import permify_async
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import permify_async
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import permify_async
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
    api_instance = permify_async.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.BundleDeleteBody() # BundleDeleteBody | 

    try:
        # delete bundle
        api_response = await api_instance.bundle_delete(tenant_id, body)
        print("The response of BundleApi->bundle_delete:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BundleApi->bundle_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BundleApi* | [**bundle_delete**](docs/BundleApi.md#bundle_delete) | **POST** /v1/tenants/{tenant_id}/bundle/delete | delete bundle
*BundleApi* | [**bundle_read**](docs/BundleApi.md#bundle_read) | **POST** /v1/tenants/{tenant_id}/bundle/read | read bundle
*BundleApi* | [**bundle_write**](docs/BundleApi.md#bundle_write) | **POST** /v1/tenants/{tenant_id}/bundle/write | write bundle
*DataApi* | [**bundle_run**](docs/DataApi.md#bundle_run) | **POST** /v1/tenants/{tenant_id}/data/run-bundle | run bundle
*DataApi* | [**data_attributes_read**](docs/DataApi.md#data_attributes_read) | **POST** /v1/tenants/{tenant_id}/data/attributes/read | read attributes
*DataApi* | [**data_delete**](docs/DataApi.md#data_delete) | **POST** /v1/tenants/{tenant_id}/data/delete | delete data
*DataApi* | [**data_relationships_read**](docs/DataApi.md#data_relationships_read) | **POST** /v1/tenants/{tenant_id}/data/relationships/read | read relationships
*DataApi* | [**data_write**](docs/DataApi.md#data_write) | **POST** /v1/tenants/{tenant_id}/data/write | write data
*DataApi* | [**relationships_delete**](docs/DataApi.md#relationships_delete) | **POST** /v1/tenants/{tenant_id}/relationships/delete | delete relationships
*DataApi* | [**relationships_write**](docs/DataApi.md#relationships_write) | **POST** /v1/tenants/{tenant_id}/relationships/write | write relationships
*PermissionApi* | [**permissions_check**](docs/PermissionApi.md#permissions_check) | **POST** /v1/tenants/{tenant_id}/permissions/check | check api
*PermissionApi* | [**permissions_expand**](docs/PermissionApi.md#permissions_expand) | **POST** /v1/tenants/{tenant_id}/permissions/expand | expand api
*PermissionApi* | [**permissions_lookup_entity**](docs/PermissionApi.md#permissions_lookup_entity) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-entity | lookup entity
*PermissionApi* | [**permissions_lookup_entity_stream**](docs/PermissionApi.md#permissions_lookup_entity_stream) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-entity-stream | lookup entity stream
*PermissionApi* | [**permissions_lookup_subject**](docs/PermissionApi.md#permissions_lookup_subject) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-subject | lookup-subject
*PermissionApi* | [**permissions_subject_permission**](docs/PermissionApi.md#permissions_subject_permission) | **POST** /v1/tenants/{tenant_id}/permissions/subject-permission | subject permission
*SchemaApi* | [**schemas_list**](docs/SchemaApi.md#schemas_list) | **POST** /v1/tenants/{tenant_id}/schemas/list | list schema
*SchemaApi* | [**schemas_partial_write**](docs/SchemaApi.md#schemas_partial_write) | **PATCH** /v1/tenants/{tenant_id}/schemas/partial-write | partially update your authorization model
*SchemaApi* | [**schemas_read**](docs/SchemaApi.md#schemas_read) | **POST** /v1/tenants/{tenant_id}/schemas/read | read schema
*SchemaApi* | [**schemas_write**](docs/SchemaApi.md#schemas_write) | **POST** /v1/tenants/{tenant_id}/schemas/write | write schema
*TenancyApi* | [**tenants_create**](docs/TenancyApi.md#tenants_create) | **POST** /v1/tenants/create | create tenant
*TenancyApi* | [**tenants_delete**](docs/TenancyApi.md#tenants_delete) | **DELETE** /v1/tenants/{id} | delete tenant
*TenancyApi* | [**tenants_list**](docs/TenancyApi.md#tenants_list) | **POST** /v1/tenants/list | list tenants
*WatchApi* | [**watch_watch**](docs/WatchApi.md#watch_watch) | **POST** /v1/tenants/{tenant_id}/watch | watch changes


## Documentation For Models

 - [AbstractType](docs/AbstractType.md)
 - [Any](docs/Any.md)
 - [Argument](docs/Argument.md)
 - [Attribute](docs/Attribute.md)
 - [AttributeDefinition](docs/AttributeDefinition.md)
 - [AttributeFilter](docs/AttributeFilter.md)
 - [AttributeReadRequestMetadata](docs/AttributeReadRequestMetadata.md)
 - [AttributeReadResponse](docs/AttributeReadResponse.md)
 - [AttributeType](docs/AttributeType.md)
 - [BundleDeleteBody](docs/BundleDeleteBody.md)
 - [BundleDeleteResponse](docs/BundleDeleteResponse.md)
 - [BundleReadBody](docs/BundleReadBody.md)
 - [BundleReadResponse](docs/BundleReadResponse.md)
 - [BundleRunResponse](docs/BundleRunResponse.md)
 - [BundleWriteBody](docs/BundleWriteBody.md)
 - [BundleWriteResponse](docs/BundleWriteResponse.md)
 - [CheckBody](docs/CheckBody.md)
 - [CheckResult](docs/CheckResult.md)
 - [CheckedExpr](docs/CheckedExpr.md)
 - [Child](docs/Child.md)
 - [Comprehension](docs/Comprehension.md)
 - [ComputedAttribute](docs/ComputedAttribute.md)
 - [ComputedUserSet](docs/ComputedUserSet.md)
 - [Constant](docs/Constant.md)
 - [Context](docs/Context.md)
 - [CreateList](docs/CreateList.md)
 - [CreateStruct](docs/CreateStruct.md)
 - [DataBundle](docs/DataBundle.md)
 - [DataChange](docs/DataChange.md)
 - [DataChangeOperation](docs/DataChangeOperation.md)
 - [DataChanges](docs/DataChanges.md)
 - [DataDeleteBody](docs/DataDeleteBody.md)
 - [DataDeleteResponse](docs/DataDeleteResponse.md)
 - [DataWriteBody](docs/DataWriteBody.md)
 - [DataWriteRequestMetadata](docs/DataWriteRequestMetadata.md)
 - [DataWriteResponse](docs/DataWriteResponse.md)
 - [DeleteRelationshipsBody](docs/DeleteRelationshipsBody.md)
 - [Entity](docs/Entity.md)
 - [EntityDefinition](docs/EntityDefinition.md)
 - [EntityDefinitionReference](docs/EntityDefinitionReference.md)
 - [EntityFilter](docs/EntityFilter.md)
 - [Entry](docs/Entry.md)
 - [ExpandLeaf](docs/ExpandLeaf.md)
 - [ExpandTreeNode](docs/ExpandTreeNode.md)
 - [ExpandTreeNodeOperation](docs/ExpandTreeNodeOperation.md)
 - [Expr](docs/Expr.md)
 - [ExprCall](docs/ExprCall.md)
 - [FunctionType](docs/FunctionType.md)
 - [Ident](docs/Ident.md)
 - [Leaf](docs/Leaf.md)
 - [ListType](docs/ListType.md)
 - [LookupEntityBody](docs/LookupEntityBody.md)
 - [LookupEntityStreamBody](docs/LookupEntityStreamBody.md)
 - [LookupSubjectBody](docs/LookupSubjectBody.md)
 - [MapType](docs/MapType.md)
 - [NullValue](docs/NullValue.md)
 - [PartialWriteBody](docs/PartialWriteBody.md)
 - [Partials](docs/Partials.md)
 - [PermissionCheckRequestMetadata](docs/PermissionCheckRequestMetadata.md)
 - [PermissionCheckResponse](docs/PermissionCheckResponse.md)
 - [PermissionCheckResponseMetadata](docs/PermissionCheckResponseMetadata.md)
 - [PermissionDefinition](docs/PermissionDefinition.md)
 - [PermissionExpandBody](docs/PermissionExpandBody.md)
 - [PermissionExpandRequestMetadata](docs/PermissionExpandRequestMetadata.md)
 - [PermissionExpandResponse](docs/PermissionExpandResponse.md)
 - [PermissionLookupEntityRequestMetadata](docs/PermissionLookupEntityRequestMetadata.md)
 - [PermissionLookupEntityResponse](docs/PermissionLookupEntityResponse.md)
 - [PermissionLookupEntityStreamResponse](docs/PermissionLookupEntityStreamResponse.md)
 - [PermissionLookupSubjectRequestMetadata](docs/PermissionLookupSubjectRequestMetadata.md)
 - [PermissionLookupSubjectResponse](docs/PermissionLookupSubjectResponse.md)
 - [PermissionSubjectPermissionRequestMetadata](docs/PermissionSubjectPermissionRequestMetadata.md)
 - [PermissionSubjectPermissionResponse](docs/PermissionSubjectPermissionResponse.md)
 - [PrimitiveType](docs/PrimitiveType.md)
 - [ReadAttributesBody](docs/ReadAttributesBody.md)
 - [ReadRelationshipsBody](docs/ReadRelationshipsBody.md)
 - [RelationDefinition](docs/RelationDefinition.md)
 - [RelationReference](docs/RelationReference.md)
 - [RelationshipDeleteResponse](docs/RelationshipDeleteResponse.md)
 - [RelationshipReadRequestMetadata](docs/RelationshipReadRequestMetadata.md)
 - [RelationshipReadResponse](docs/RelationshipReadResponse.md)
 - [RelationshipWriteRequestMetadata](docs/RelationshipWriteRequestMetadata.md)
 - [RelationshipWriteResponse](docs/RelationshipWriteResponse.md)
 - [Rewrite](docs/Rewrite.md)
 - [RewriteOperation](docs/RewriteOperation.md)
 - [RuleDefinition](docs/RuleDefinition.md)
 - [RunBundleBody](docs/RunBundleBody.md)
 - [SchemaDefinition](docs/SchemaDefinition.md)
 - [SchemaDefinitionReference](docs/SchemaDefinitionReference.md)
 - [SchemaList](docs/SchemaList.md)
 - [SchemaListBody](docs/SchemaListBody.md)
 - [SchemaListResponse](docs/SchemaListResponse.md)
 - [SchemaPartialWriteRequestMetadata](docs/SchemaPartialWriteRequestMetadata.md)
 - [SchemaPartialWriteResponse](docs/SchemaPartialWriteResponse.md)
 - [SchemaReadBody](docs/SchemaReadBody.md)
 - [SchemaReadRequestMetadata](docs/SchemaReadRequestMetadata.md)
 - [SchemaReadResponse](docs/SchemaReadResponse.md)
 - [SchemaWriteBody](docs/SchemaWriteBody.md)
 - [SchemaWriteResponse](docs/SchemaWriteResponse.md)
 - [Select](docs/Select.md)
 - [SourceInfo](docs/SourceInfo.md)
 - [Status](docs/Status.md)
 - [StreamResultOfPermissionLookupEntityStreamResponse](docs/StreamResultOfPermissionLookupEntityStreamResponse.md)
 - [StreamResultOfWatchResponse](docs/StreamResultOfWatchResponse.md)
 - [StringArrayValue](docs/StringArrayValue.md)
 - [Subject](docs/Subject.md)
 - [SubjectFilter](docs/SubjectFilter.md)
 - [SubjectPermissionBody](docs/SubjectPermissionBody.md)
 - [Subjects](docs/Subjects.md)
 - [Tenant](docs/Tenant.md)
 - [TenantCreateRequest](docs/TenantCreateRequest.md)
 - [TenantCreateResponse](docs/TenantCreateResponse.md)
 - [TenantDeleteResponse](docs/TenantDeleteResponse.md)
 - [TenantListRequest](docs/TenantListRequest.md)
 - [TenantListResponse](docs/TenantListResponse.md)
 - [Tuple](docs/Tuple.md)
 - [TupleFilter](docs/TupleFilter.md)
 - [TupleSet](docs/TupleSet.md)
 - [TupleToUserSet](docs/TupleToUserSet.md)
 - [V1Call](docs/V1Call.md)
 - [V1Expand](docs/V1Expand.md)
 - [V1Operation](docs/V1Operation.md)
 - [V1alpha1Reference](docs/V1alpha1Reference.md)
 - [V1alpha1Type](docs/V1alpha1Type.md)
 - [Values](docs/Values.md)
 - [WatchBody](docs/WatchBody.md)
 - [WatchResponse](docs/WatchResponse.md)
 - [WellKnownType](docs/WellKnownType.md)
 - [WriteRelationshipsBody](docs/WriteRelationshipsBody.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@permify.co


