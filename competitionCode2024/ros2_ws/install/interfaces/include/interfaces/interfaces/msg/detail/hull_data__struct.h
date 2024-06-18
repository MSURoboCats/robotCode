// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/HullData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__HULL_DATA__STRUCT_H_
#define INTERFACES__MSG__DETAIL__HULL_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'temperature'
#include "sensor_msgs/msg/detail/temperature__struct.h"
// Member 'pressure'
#include "sensor_msgs/msg/detail/fluid_pressure__struct.h"
// Member 'humidity'
#include "sensor_msgs/msg/detail/relative_humidity__struct.h"

/// Struct defined in msg/HullData in the package interfaces.
typedef struct interfaces__msg__HullData
{
  sensor_msgs__msg__Temperature temperature;
  sensor_msgs__msg__FluidPressure pressure;
  sensor_msgs__msg__RelativeHumidity humidity;
} interfaces__msg__HullData;

// Struct for a sequence of interfaces__msg__HullData.
typedef struct interfaces__msg__HullData__Sequence
{
  interfaces__msg__HullData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__HullData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__HULL_DATA__STRUCT_H_
