// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:msg/HullData.idl
// generated code does not contain a copyright notice
#include "interfaces/msg/detail/hull_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `temperature`
#include "sensor_msgs/msg/detail/temperature__functions.h"
// Member `pressure`
#include "sensor_msgs/msg/detail/fluid_pressure__functions.h"
// Member `humidity`
#include "sensor_msgs/msg/detail/relative_humidity__functions.h"

bool
interfaces__msg__HullData__init(interfaces__msg__HullData * msg)
{
  if (!msg) {
    return false;
  }
  // temperature
  if (!sensor_msgs__msg__Temperature__init(&msg->temperature)) {
    interfaces__msg__HullData__fini(msg);
    return false;
  }
  // pressure
  if (!sensor_msgs__msg__FluidPressure__init(&msg->pressure)) {
    interfaces__msg__HullData__fini(msg);
    return false;
  }
  // humidity
  if (!sensor_msgs__msg__RelativeHumidity__init(&msg->humidity)) {
    interfaces__msg__HullData__fini(msg);
    return false;
  }
  return true;
}

void
interfaces__msg__HullData__fini(interfaces__msg__HullData * msg)
{
  if (!msg) {
    return;
  }
  // temperature
  sensor_msgs__msg__Temperature__fini(&msg->temperature);
  // pressure
  sensor_msgs__msg__FluidPressure__fini(&msg->pressure);
  // humidity
  sensor_msgs__msg__RelativeHumidity__fini(&msg->humidity);
}

bool
interfaces__msg__HullData__are_equal(const interfaces__msg__HullData * lhs, const interfaces__msg__HullData * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // temperature
  if (!sensor_msgs__msg__Temperature__are_equal(
      &(lhs->temperature), &(rhs->temperature)))
  {
    return false;
  }
  // pressure
  if (!sensor_msgs__msg__FluidPressure__are_equal(
      &(lhs->pressure), &(rhs->pressure)))
  {
    return false;
  }
  // humidity
  if (!sensor_msgs__msg__RelativeHumidity__are_equal(
      &(lhs->humidity), &(rhs->humidity)))
  {
    return false;
  }
  return true;
}

bool
interfaces__msg__HullData__copy(
  const interfaces__msg__HullData * input,
  interfaces__msg__HullData * output)
{
  if (!input || !output) {
    return false;
  }
  // temperature
  if (!sensor_msgs__msg__Temperature__copy(
      &(input->temperature), &(output->temperature)))
  {
    return false;
  }
  // pressure
  if (!sensor_msgs__msg__FluidPressure__copy(
      &(input->pressure), &(output->pressure)))
  {
    return false;
  }
  // humidity
  if (!sensor_msgs__msg__RelativeHumidity__copy(
      &(input->humidity), &(output->humidity)))
  {
    return false;
  }
  return true;
}

interfaces__msg__HullData *
interfaces__msg__HullData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__HullData * msg = (interfaces__msg__HullData *)allocator.allocate(sizeof(interfaces__msg__HullData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__msg__HullData));
  bool success = interfaces__msg__HullData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interfaces__msg__HullData__destroy(interfaces__msg__HullData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interfaces__msg__HullData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interfaces__msg__HullData__Sequence__init(interfaces__msg__HullData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__HullData * data = NULL;

  if (size) {
    data = (interfaces__msg__HullData *)allocator.zero_allocate(size, sizeof(interfaces__msg__HullData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__msg__HullData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__msg__HullData__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__msg__HullData__Sequence__fini(interfaces__msg__HullData__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__msg__HullData__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__msg__HullData__Sequence *
interfaces__msg__HullData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__HullData__Sequence * array = (interfaces__msg__HullData__Sequence *)allocator.allocate(sizeof(interfaces__msg__HullData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interfaces__msg__HullData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interfaces__msg__HullData__Sequence__destroy(interfaces__msg__HullData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interfaces__msg__HullData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interfaces__msg__HullData__Sequence__are_equal(const interfaces__msg__HullData__Sequence * lhs, const interfaces__msg__HullData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__msg__HullData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__msg__HullData__Sequence__copy(
  const interfaces__msg__HullData__Sequence * input,
  interfaces__msg__HullData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__msg__HullData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    interfaces__msg__HullData * data =
      (interfaces__msg__HullData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__msg__HullData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          interfaces__msg__HullData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__msg__HullData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
