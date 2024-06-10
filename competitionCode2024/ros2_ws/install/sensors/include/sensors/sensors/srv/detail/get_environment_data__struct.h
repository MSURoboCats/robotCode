// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sensors:srv/GetEnvironmentData.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_ENVIRONMENT_DATA__STRUCT_H_
#define SENSORS__SRV__DETAIL__GET_ENVIRONMENT_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetEnvironmentData in the package sensors.
typedef struct sensors__srv__GetEnvironmentData_Request
{
  uint8_t structure_needs_at_least_one_member;
} sensors__srv__GetEnvironmentData_Request;

// Struct for a sequence of sensors__srv__GetEnvironmentData_Request.
typedef struct sensors__srv__GetEnvironmentData_Request__Sequence
{
  sensors__srv__GetEnvironmentData_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sensors__srv__GetEnvironmentData_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "sensors/msg/detail/environment_data__struct.h"

/// Struct defined in srv/GetEnvironmentData in the package sensors.
typedef struct sensors__srv__GetEnvironmentData_Response
{
  sensors__msg__EnvironmentData data;
} sensors__srv__GetEnvironmentData_Response;

// Struct for a sequence of sensors__srv__GetEnvironmentData_Response.
typedef struct sensors__srv__GetEnvironmentData_Response__Sequence
{
  sensors__srv__GetEnvironmentData_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sensors__srv__GetEnvironmentData_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SENSORS__SRV__DETAIL__GET_ENVIRONMENT_DATA__STRUCT_H_
