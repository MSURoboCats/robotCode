// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sensors:srv/GetDownward.idl
// generated code does not contain a copyright notice
#include "sensors/srv/detail/get_downward__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
sensors__srv__GetDownward_Request__init(sensors__srv__GetDownward_Request * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
sensors__srv__GetDownward_Request__fini(sensors__srv__GetDownward_Request * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
sensors__srv__GetDownward_Request__are_equal(const sensors__srv__GetDownward_Request * lhs, const sensors__srv__GetDownward_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
sensors__srv__GetDownward_Request__copy(
  const sensors__srv__GetDownward_Request * input,
  sensors__srv__GetDownward_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

sensors__srv__GetDownward_Request *
sensors__srv__GetDownward_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sensors__srv__GetDownward_Request * msg = (sensors__srv__GetDownward_Request *)allocator.allocate(sizeof(sensors__srv__GetDownward_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sensors__srv__GetDownward_Request));
  bool success = sensors__srv__GetDownward_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sensors__srv__GetDownward_Request__destroy(sensors__srv__GetDownward_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sensors__srv__GetDownward_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sensors__srv__GetDownward_Request__Sequence__init(sensors__srv__GetDownward_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sensors__srv__GetDownward_Request * data = NULL;

  if (size) {
    data = (sensors__srv__GetDownward_Request *)allocator.zero_allocate(size, sizeof(sensors__srv__GetDownward_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sensors__srv__GetDownward_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sensors__srv__GetDownward_Request__fini(&data[i - 1]);
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
sensors__srv__GetDownward_Request__Sequence__fini(sensors__srv__GetDownward_Request__Sequence * array)
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
      sensors__srv__GetDownward_Request__fini(&array->data[i]);
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

sensors__srv__GetDownward_Request__Sequence *
sensors__srv__GetDownward_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sensors__srv__GetDownward_Request__Sequence * array = (sensors__srv__GetDownward_Request__Sequence *)allocator.allocate(sizeof(sensors__srv__GetDownward_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sensors__srv__GetDownward_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sensors__srv__GetDownward_Request__Sequence__destroy(sensors__srv__GetDownward_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sensors__srv__GetDownward_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sensors__srv__GetDownward_Request__Sequence__are_equal(const sensors__srv__GetDownward_Request__Sequence * lhs, const sensors__srv__GetDownward_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sensors__srv__GetDownward_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sensors__srv__GetDownward_Request__Sequence__copy(
  const sensors__srv__GetDownward_Request__Sequence * input,
  sensors__srv__GetDownward_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sensors__srv__GetDownward_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sensors__srv__GetDownward_Request * data =
      (sensors__srv__GetDownward_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sensors__srv__GetDownward_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sensors__srv__GetDownward_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sensors__srv__GetDownward_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `downward_frame`
#include "sensor_msgs/msg/detail/image__functions.h"

bool
sensors__srv__GetDownward_Response__init(sensors__srv__GetDownward_Response * msg)
{
  if (!msg) {
    return false;
  }
  // downward_frame
  if (!sensor_msgs__msg__Image__init(&msg->downward_frame)) {
    sensors__srv__GetDownward_Response__fini(msg);
    return false;
  }
  return true;
}

void
sensors__srv__GetDownward_Response__fini(sensors__srv__GetDownward_Response * msg)
{
  if (!msg) {
    return;
  }
  // downward_frame
  sensor_msgs__msg__Image__fini(&msg->downward_frame);
}

bool
sensors__srv__GetDownward_Response__are_equal(const sensors__srv__GetDownward_Response * lhs, const sensors__srv__GetDownward_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // downward_frame
  if (!sensor_msgs__msg__Image__are_equal(
      &(lhs->downward_frame), &(rhs->downward_frame)))
  {
    return false;
  }
  return true;
}

bool
sensors__srv__GetDownward_Response__copy(
  const sensors__srv__GetDownward_Response * input,
  sensors__srv__GetDownward_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // downward_frame
  if (!sensor_msgs__msg__Image__copy(
      &(input->downward_frame), &(output->downward_frame)))
  {
    return false;
  }
  return true;
}

sensors__srv__GetDownward_Response *
sensors__srv__GetDownward_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sensors__srv__GetDownward_Response * msg = (sensors__srv__GetDownward_Response *)allocator.allocate(sizeof(sensors__srv__GetDownward_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sensors__srv__GetDownward_Response));
  bool success = sensors__srv__GetDownward_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sensors__srv__GetDownward_Response__destroy(sensors__srv__GetDownward_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sensors__srv__GetDownward_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sensors__srv__GetDownward_Response__Sequence__init(sensors__srv__GetDownward_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sensors__srv__GetDownward_Response * data = NULL;

  if (size) {
    data = (sensors__srv__GetDownward_Response *)allocator.zero_allocate(size, sizeof(sensors__srv__GetDownward_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sensors__srv__GetDownward_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sensors__srv__GetDownward_Response__fini(&data[i - 1]);
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
sensors__srv__GetDownward_Response__Sequence__fini(sensors__srv__GetDownward_Response__Sequence * array)
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
      sensors__srv__GetDownward_Response__fini(&array->data[i]);
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

sensors__srv__GetDownward_Response__Sequence *
sensors__srv__GetDownward_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sensors__srv__GetDownward_Response__Sequence * array = (sensors__srv__GetDownward_Response__Sequence *)allocator.allocate(sizeof(sensors__srv__GetDownward_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sensors__srv__GetDownward_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sensors__srv__GetDownward_Response__Sequence__destroy(sensors__srv__GetDownward_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sensors__srv__GetDownward_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sensors__srv__GetDownward_Response__Sequence__are_equal(const sensors__srv__GetDownward_Response__Sequence * lhs, const sensors__srv__GetDownward_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sensors__srv__GetDownward_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sensors__srv__GetDownward_Response__Sequence__copy(
  const sensors__srv__GetDownward_Response__Sequence * input,
  sensors__srv__GetDownward_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sensors__srv__GetDownward_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sensors__srv__GetDownward_Response * data =
      (sensors__srv__GetDownward_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sensors__srv__GetDownward_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sensors__srv__GetDownward_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sensors__srv__GetDownward_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}