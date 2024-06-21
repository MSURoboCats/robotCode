// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/Yolov8Detection.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__STRUCT_H_
#define INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"
// Member 'center'
// Member 'dimensions'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in msg/Yolov8Detection in the package interfaces.
typedef struct interfaces__msg__Yolov8Detection
{
  rosidl_runtime_c__String name;
  int64_t tracking_id;
  double confidence;
  geometry_msgs__msg__Point center;
  geometry_msgs__msg__Point dimensions;
} interfaces__msg__Yolov8Detection;

// Struct for a sequence of interfaces__msg__Yolov8Detection.
typedef struct interfaces__msg__Yolov8Detection__Sequence
{
  interfaces__msg__Yolov8Detection * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__Yolov8Detection__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__STRUCT_H_
