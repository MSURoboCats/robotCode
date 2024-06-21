// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:msg/Yolov8Detection.idl
// generated code does not contain a copyright notice
#include "interfaces/msg/detail/yolov8_detection__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"
// Member `center`
// Member `dimensions`
#include "geometry_msgs/msg/detail/point__functions.h"

bool
interfaces__msg__Yolov8Detection__init(interfaces__msg__Yolov8Detection * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    interfaces__msg__Yolov8Detection__fini(msg);
    return false;
  }
  // tracking_id
  // confidence
  // center
  if (!geometry_msgs__msg__Point__init(&msg->center)) {
    interfaces__msg__Yolov8Detection__fini(msg);
    return false;
  }
  // dimensions
  if (!geometry_msgs__msg__Point__init(&msg->dimensions)) {
    interfaces__msg__Yolov8Detection__fini(msg);
    return false;
  }
  return true;
}

void
interfaces__msg__Yolov8Detection__fini(interfaces__msg__Yolov8Detection * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // tracking_id
  // confidence
  // center
  geometry_msgs__msg__Point__fini(&msg->center);
  // dimensions
  geometry_msgs__msg__Point__fini(&msg->dimensions);
}

bool
interfaces__msg__Yolov8Detection__are_equal(const interfaces__msg__Yolov8Detection * lhs, const interfaces__msg__Yolov8Detection * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // tracking_id
  if (lhs->tracking_id != rhs->tracking_id) {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // center
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->center), &(rhs->center)))
  {
    return false;
  }
  // dimensions
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->dimensions), &(rhs->dimensions)))
  {
    return false;
  }
  return true;
}

bool
interfaces__msg__Yolov8Detection__copy(
  const interfaces__msg__Yolov8Detection * input,
  interfaces__msg__Yolov8Detection * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // tracking_id
  output->tracking_id = input->tracking_id;
  // confidence
  output->confidence = input->confidence;
  // center
  if (!geometry_msgs__msg__Point__copy(
      &(input->center), &(output->center)))
  {
    return false;
  }
  // dimensions
  if (!geometry_msgs__msg__Point__copy(
      &(input->dimensions), &(output->dimensions)))
  {
    return false;
  }
  return true;
}

interfaces__msg__Yolov8Detection *
interfaces__msg__Yolov8Detection__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__Yolov8Detection * msg = (interfaces__msg__Yolov8Detection *)allocator.allocate(sizeof(interfaces__msg__Yolov8Detection), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__msg__Yolov8Detection));
  bool success = interfaces__msg__Yolov8Detection__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interfaces__msg__Yolov8Detection__destroy(interfaces__msg__Yolov8Detection * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interfaces__msg__Yolov8Detection__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interfaces__msg__Yolov8Detection__Sequence__init(interfaces__msg__Yolov8Detection__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__Yolov8Detection * data = NULL;

  if (size) {
    data = (interfaces__msg__Yolov8Detection *)allocator.zero_allocate(size, sizeof(interfaces__msg__Yolov8Detection), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__msg__Yolov8Detection__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__msg__Yolov8Detection__fini(&data[i - 1]);
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
interfaces__msg__Yolov8Detection__Sequence__fini(interfaces__msg__Yolov8Detection__Sequence * array)
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
      interfaces__msg__Yolov8Detection__fini(&array->data[i]);
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

interfaces__msg__Yolov8Detection__Sequence *
interfaces__msg__Yolov8Detection__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces__msg__Yolov8Detection__Sequence * array = (interfaces__msg__Yolov8Detection__Sequence *)allocator.allocate(sizeof(interfaces__msg__Yolov8Detection__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interfaces__msg__Yolov8Detection__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interfaces__msg__Yolov8Detection__Sequence__destroy(interfaces__msg__Yolov8Detection__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interfaces__msg__Yolov8Detection__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interfaces__msg__Yolov8Detection__Sequence__are_equal(const interfaces__msg__Yolov8Detection__Sequence * lhs, const interfaces__msg__Yolov8Detection__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces__msg__Yolov8Detection__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces__msg__Yolov8Detection__Sequence__copy(
  const interfaces__msg__Yolov8Detection__Sequence * input,
  interfaces__msg__Yolov8Detection__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces__msg__Yolov8Detection);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    interfaces__msg__Yolov8Detection * data =
      (interfaces__msg__Yolov8Detection *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces__msg__Yolov8Detection__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          interfaces__msg__Yolov8Detection__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces__msg__Yolov8Detection__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
