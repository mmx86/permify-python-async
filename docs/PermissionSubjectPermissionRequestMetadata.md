# PermissionSubjectPermissionRequestMetadata

PermissionSubjectPermissionRequestMetadata is the metadata associated with a PermissionSubjectPermissionRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | Version of the schema. | [optional] 
**snap_token** | **str** | Token associated with the snap. | [optional] 
**only_permission** | **bool** | Whether to only check permissions. | [optional] 
**depth** | **int** | Depth of the check, must be greater than or equal to 3. | [optional] 

## Example

```python
from permify_async.models.permission_subject_permission_request_metadata import PermissionSubjectPermissionRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionSubjectPermissionRequestMetadata from a JSON string
permission_subject_permission_request_metadata_instance = PermissionSubjectPermissionRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(PermissionSubjectPermissionRequestMetadata.to_json())

# convert the object into a dict
permission_subject_permission_request_metadata_dict = permission_subject_permission_request_metadata_instance.to_dict()
# create an instance of PermissionSubjectPermissionRequestMetadata from a dict
permission_subject_permission_request_metadata_from_dict = PermissionSubjectPermissionRequestMetadata.from_dict(permission_subject_permission_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

