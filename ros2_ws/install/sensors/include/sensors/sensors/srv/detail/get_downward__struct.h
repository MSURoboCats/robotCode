// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sensors:srv/GetDownward.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_DOWNWARD__STRUCT_H_
#define SENSORS__SRV__DETAIL__GET_DOWNWARD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetDownward in the package sensors.
typedef struct sensors__srv__GetDownward_Request
{
  uint8_t structure_needs_at_least_one_member;
} sensors__srv__GetDownward_Request;

// Struct for a sequence of sensors__srv__GetDownward_Request.
typedef struct sensors__srv__GetDownward_Request__Sequence
{
  sensors__srv__GetDownward_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sensors__srv__GetDownward_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'downward_frame'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in srv/GetDownward in the package sensors.
typedef struct sensors__srv__GetDownward_Response
{
  sensor_msgs__msg__Image downward_frame;
} sensors__srv__GetDownward_Response;

// Struct for a sequence of sensors__srv__GetDownward_Response.
typedef struct sensors__srv__GetDownward_Response__Sequence
{
  sensors__srv__GetDownward_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sensors__srv__GetDownward_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SENSORS__SRV__DETAIL__GET_DOWNWARD__STRUCT_H_
