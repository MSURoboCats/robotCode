// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sensors:srv/GetVoltage.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sensors/srv/detail/get_voltage__rosidl_typesupport_introspection_c.h"
#include "sensors/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sensors/srv/detail/get_voltage__functions.h"
#include "sensors/srv/detail/get_voltage__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sensors__srv__GetVoltage_Request__init(message_memory);
}

void sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_fini_function(void * message_memory)
{
  sensors__srv__GetVoltage_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sensors__srv__GetVoltage_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_message_members = {
  "sensors__srv",  // message namespace
  "GetVoltage_Request",  // message name
  1,  // number of fields
  sizeof(sensors__srv__GetVoltage_Request),
  sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_message_member_array,  // message members
  sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_message_type_support_handle = {
  0,
  &sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sensors
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensors, srv, GetVoltage_Request)() {
  if (!sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_message_type_support_handle.typesupport_identifier) {
    sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sensors__srv__GetVoltage_Request__rosidl_typesupport_introspection_c__GetVoltage_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "sensors/srv/detail/get_voltage__rosidl_typesupport_introspection_c.h"
// already included above
// #include "sensors/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "sensors/srv/detail/get_voltage__functions.h"
// already included above
// #include "sensors/srv/detail/get_voltage__struct.h"


// Include directives for member types
// Member `voltage`
#include "sensor_msgs/msg/battery_state.h"
// Member `voltage`
#include "sensor_msgs/msg/detail/battery_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sensors__srv__GetVoltage_Response__init(message_memory);
}

void sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_fini_function(void * message_memory)
{
  sensors__srv__GetVoltage_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_member_array[1] = {
  {
    "voltage",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sensors__srv__GetVoltage_Response, voltage),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_members = {
  "sensors__srv",  // message namespace
  "GetVoltage_Response",  // message name
  1,  // number of fields
  sizeof(sensors__srv__GetVoltage_Response),
  sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_member_array,  // message members
  sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_type_support_handle = {
  0,
  &sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sensors
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensors, srv, GetVoltage_Response)() {
  sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, BatteryState)();
  if (!sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_type_support_handle.typesupport_identifier) {
    sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sensors__srv__GetVoltage_Response__rosidl_typesupport_introspection_c__GetVoltage_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "sensors/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "sensors/srv/detail/get_voltage__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_service_members = {
  "sensors__srv",  // service namespace
  "GetVoltage",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_Request_message_type_support_handle,
  NULL  // response message
  // sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_Response_message_type_support_handle
};

static rosidl_service_type_support_t sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_service_type_support_handle = {
  0,
  &sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensors, srv, GetVoltage_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensors, srv, GetVoltage_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sensors
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensors, srv, GetVoltage)() {
  if (!sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_service_type_support_handle.typesupport_identifier) {
    sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensors, srv, GetVoltage_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensors, srv, GetVoltage_Response)()->data;
  }

  return &sensors__srv__detail__get_voltage__rosidl_typesupport_introspection_c__GetVoltage_service_type_support_handle;
}
