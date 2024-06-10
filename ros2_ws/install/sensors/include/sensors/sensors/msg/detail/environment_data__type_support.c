// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sensors:msg/EnvironmentData.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sensors/msg/detail/environment_data__rosidl_typesupport_introspection_c.h"
#include "sensors/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sensors/msg/detail/environment_data__functions.h"
#include "sensors/msg/detail/environment_data__struct.h"


// Include directives for member types
// Member `temperature`
#include "sensor_msgs/msg/temperature.h"
// Member `temperature`
#include "sensor_msgs/msg/detail/temperature__rosidl_typesupport_introspection_c.h"
// Member `pressure`
#include "sensor_msgs/msg/fluid_pressure.h"
// Member `pressure`
#include "sensor_msgs/msg/detail/fluid_pressure__rosidl_typesupport_introspection_c.h"
// Member `humidity`
#include "sensor_msgs/msg/relative_humidity.h"
// Member `humidity`
#include "sensor_msgs/msg/detail/relative_humidity__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sensors__msg__EnvironmentData__init(message_memory);
}

void sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_fini_function(void * message_memory)
{
  sensors__msg__EnvironmentData__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_member_array[3] = {
  {
    "temperature",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sensors__msg__EnvironmentData, temperature),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pressure",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sensors__msg__EnvironmentData, pressure),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "humidity",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sensors__msg__EnvironmentData, humidity),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_members = {
  "sensors__msg",  // message namespace
  "EnvironmentData",  // message name
  3,  // number of fields
  sizeof(sensors__msg__EnvironmentData),
  sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_member_array,  // message members
  sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_init_function,  // function to initialize message memory (memory has to be allocated)
  sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_type_support_handle = {
  0,
  &sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sensors
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensors, msg, EnvironmentData)() {
  sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, Temperature)();
  sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, FluidPressure)();
  sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, RelativeHumidity)();
  if (!sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_type_support_handle.typesupport_identifier) {
    sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sensors__msg__EnvironmentData__rosidl_typesupport_introspection_c__EnvironmentData_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
