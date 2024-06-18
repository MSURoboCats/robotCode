// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/MotorPowers.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MOTOR_POWERS__STRUCT_H_
#define INTERFACES__SRV__DETAIL__MOTOR_POWERS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/MotorPowers in the package interfaces.
typedef struct interfaces__srv__MotorPowers_Request
{
  double motor1;
  double motor2;
  double motor3;
  double motor4;
  double motor5;
  double motor6;
  double motor7;
  double motor8;
} interfaces__srv__MotorPowers_Request;

// Struct for a sequence of interfaces__srv__MotorPowers_Request.
typedef struct interfaces__srv__MotorPowers_Request__Sequence
{
  interfaces__srv__MotorPowers_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__MotorPowers_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/MotorPowers in the package interfaces.
typedef struct interfaces__srv__MotorPowers_Response
{
  uint8_t structure_needs_at_least_one_member;
} interfaces__srv__MotorPowers_Response;

// Struct for a sequence of interfaces__srv__MotorPowers_Response.
typedef struct interfaces__srv__MotorPowers_Response__Sequence
{
  interfaces__srv__MotorPowers_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__MotorPowers_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__MOTOR_POWERS__STRUCT_H_
