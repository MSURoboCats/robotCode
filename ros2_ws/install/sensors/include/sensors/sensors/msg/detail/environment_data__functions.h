// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from sensors:msg/EnvironmentData.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__MSG__DETAIL__ENVIRONMENT_DATA__FUNCTIONS_H_
#define SENSORS__MSG__DETAIL__ENVIRONMENT_DATA__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "sensors/msg/rosidl_generator_c__visibility_control.h"

#include "sensors/msg/detail/environment_data__struct.h"

/// Initialize msg/EnvironmentData message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * sensors__msg__EnvironmentData
 * )) before or use
 * sensors__msg__EnvironmentData__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
bool
sensors__msg__EnvironmentData__init(sensors__msg__EnvironmentData * msg);

/// Finalize msg/EnvironmentData message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
void
sensors__msg__EnvironmentData__fini(sensors__msg__EnvironmentData * msg);

/// Create msg/EnvironmentData message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * sensors__msg__EnvironmentData__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
sensors__msg__EnvironmentData *
sensors__msg__EnvironmentData__create();

/// Destroy msg/EnvironmentData message.
/**
 * It calls
 * sensors__msg__EnvironmentData__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
void
sensors__msg__EnvironmentData__destroy(sensors__msg__EnvironmentData * msg);

/// Check for msg/EnvironmentData message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
bool
sensors__msg__EnvironmentData__are_equal(const sensors__msg__EnvironmentData * lhs, const sensors__msg__EnvironmentData * rhs);

/// Copy a msg/EnvironmentData message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
bool
sensors__msg__EnvironmentData__copy(
  const sensors__msg__EnvironmentData * input,
  sensors__msg__EnvironmentData * output);

/// Initialize array of msg/EnvironmentData messages.
/**
 * It allocates the memory for the number of elements and calls
 * sensors__msg__EnvironmentData__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
bool
sensors__msg__EnvironmentData__Sequence__init(sensors__msg__EnvironmentData__Sequence * array, size_t size);

/// Finalize array of msg/EnvironmentData messages.
/**
 * It calls
 * sensors__msg__EnvironmentData__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
void
sensors__msg__EnvironmentData__Sequence__fini(sensors__msg__EnvironmentData__Sequence * array);

/// Create array of msg/EnvironmentData messages.
/**
 * It allocates the memory for the array and calls
 * sensors__msg__EnvironmentData__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
sensors__msg__EnvironmentData__Sequence *
sensors__msg__EnvironmentData__Sequence__create(size_t size);

/// Destroy array of msg/EnvironmentData messages.
/**
 * It calls
 * sensors__msg__EnvironmentData__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
void
sensors__msg__EnvironmentData__Sequence__destroy(sensors__msg__EnvironmentData__Sequence * array);

/// Check for msg/EnvironmentData message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
bool
sensors__msg__EnvironmentData__Sequence__are_equal(const sensors__msg__EnvironmentData__Sequence * lhs, const sensors__msg__EnvironmentData__Sequence * rhs);

/// Copy an array of msg/EnvironmentData messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_sensors
bool
sensors__msg__EnvironmentData__Sequence__copy(
  const sensors__msg__EnvironmentData__Sequence * input,
  sensors__msg__EnvironmentData__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SENSORS__MSG__DETAIL__ENVIRONMENT_DATA__FUNCTIONS_H_
