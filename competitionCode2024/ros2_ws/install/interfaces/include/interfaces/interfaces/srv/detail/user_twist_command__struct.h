// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/UserTwistCommand.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__STRUCT_H_
#define INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'twist_command'
#include "geometry_msgs/msg/detail/twist__struct.h"

/// Struct defined in srv/UserTwistCommand in the package interfaces.
typedef struct interfaces__srv__UserTwistCommand_Request
{
  geometry_msgs__msg__Twist twist_command;
} interfaces__srv__UserTwistCommand_Request;

// Struct for a sequence of interfaces__srv__UserTwistCommand_Request.
typedef struct interfaces__srv__UserTwistCommand_Request__Sequence
{
  interfaces__srv__UserTwistCommand_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__UserTwistCommand_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/UserTwistCommand in the package interfaces.
typedef struct interfaces__srv__UserTwistCommand_Response
{
  uint8_t structure_needs_at_least_one_member;
} interfaces__srv__UserTwistCommand_Response;

// Struct for a sequence of interfaces__srv__UserTwistCommand_Response.
typedef struct interfaces__srv__UserTwistCommand_Response__Sequence
{
  interfaces__srv__UserTwistCommand_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__UserTwistCommand_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__STRUCT_H_
