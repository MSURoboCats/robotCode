// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/BatHealth.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__BAT_HEALTH__STRUCT_H_
#define INTERFACES__SRV__DETAIL__BAT_HEALTH__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/BatHealth in the package interfaces.
typedef struct interfaces__srv__BatHealth_Request
{
  uint8_t structure_needs_at_least_one_member;
} interfaces__srv__BatHealth_Request;

// Struct for a sequence of interfaces__srv__BatHealth_Request.
typedef struct interfaces__srv__BatHealth_Request__Sequence
{
  interfaces__srv__BatHealth_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__BatHealth_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'voltage'
#include "sensor_msgs/msg/detail/battery_state__struct.h"

/// Struct defined in srv/BatHealth in the package interfaces.
typedef struct interfaces__srv__BatHealth_Response
{
  sensor_msgs__msg__BatteryState voltage;
} interfaces__srv__BatHealth_Response;

// Struct for a sequence of interfaces__srv__BatHealth_Response.
typedef struct interfaces__srv__BatHealth_Response__Sequence
{
  interfaces__srv__BatHealth_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__BatHealth_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__BAT_HEALTH__STRUCT_H_
