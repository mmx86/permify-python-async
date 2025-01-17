# LookupSubjectBody

PermissionLookupSubjectRequest is the request message for the LookupSubject method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionLookupSubjectRequestMetadata**](PermissionLookupSubjectRequestMetadata.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**permission** | **str** | Permission to be checked, can be a permission or relation. Required, and must match the pattern \&quot;^([a-zA-Z][a-zA-Z0-9_]{1,62}[a-zA-Z0-9])$\&quot;, max 64 bytes. | [optional] 
**subject_reference** | [**RelationReference**](RelationReference.md) |  | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**arguments** | [**List[Argument]**](Argument.md) | Additional arguments associated with this request. | [optional] 
**page_size** | **int** | page_size is the number of subjects to be returned in the response. The value should be between 1 and 100. | [optional] 
**continuous_token** | **str** | continuous_token is an optional parameter used for pagination. It should be the value received in the previous response. | [optional] 

## Example

```python
from permify_async.models.lookup_subject_body import LookupSubjectBody

# TODO update the JSON string below
json = "{}"
# create an instance of LookupSubjectBody from a JSON string
lookup_subject_body_instance = LookupSubjectBody.from_json(json)
# print the JSON string representation of the object
print(LookupSubjectBody.to_json())

# convert the object into a dict
lookup_subject_body_dict = lookup_subject_body_instance.to_dict()
# create an instance of LookupSubjectBody from a dict
lookup_subject_body_from_dict = LookupSubjectBody.from_dict(lookup_subject_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


