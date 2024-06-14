// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sensors:msg/ControlData.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__MSG__DETAIL__CONTROL_DATA__STRUCT_H_
#define SENSORS__MSG__DETAIL__CONTROL_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'imu_data'
#include "sensor_msgs/msg/detail/imu__struct.h"

/// Struct defined in msg/ControlData in the package sensors.
typedef struct sensors__msg__ControlData
{
  sensor_msgs__msg__Imu imu_data;
  double depth;
} sensors__msg__ControlData;

// Struct for a sequence of sensors__msg__ControlData.
typedef struct sensors__msg__ControlData__Sequence
{
  sensors__msg__ControlData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sensors__msg__ControlData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SENSORS__MSG__DETAIL__CONTROL_DATA__STRUCT_H_
