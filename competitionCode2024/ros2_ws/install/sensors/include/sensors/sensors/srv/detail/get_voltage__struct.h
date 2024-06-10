// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sensors:srv/GetVoltage.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_VOLTAGE__STRUCT_H_
#define SENSORS__SRV__DETAIL__GET_VOLTAGE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetVoltage in the package sensors.
typedef struct sensors__srv__GetVoltage_Request
{
  uint8_t structure_needs_at_least_one_member;
} sensors__srv__GetVoltage_Request;

// Struct for a sequence of sensors__srv__GetVoltage_Request.
typedef struct sensors__srv__GetVoltage_Request__Sequence
{
  sensors__srv__GetVoltage_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sensors__srv__GetVoltage_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'voltage'
#include "sensor_msgs/msg/detail/battery_state__struct.h"

/// Struct defined in srv/GetVoltage in the package sensors.
typedef struct sensors__srv__GetVoltage_Response
{
  sensor_msgs__msg__BatteryState voltage;
} sensors__srv__GetVoltage_Response;

// Struct for a sequence of sensors__srv__GetVoltage_Response.
typedef struct sensors__srv__GetVoltage_Response__Sequence
{
  sensors__srv__GetVoltage_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sensors__srv__GetVoltage_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SENSORS__SRV__DETAIL__GET_VOLTAGE__STRUCT_H_
