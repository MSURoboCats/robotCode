// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from sensors:msg/ControlData.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__MSG__DETAIL__CONTROL_DATA__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SENSORS__MSG__DETAIL__CONTROL_DATA__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "sensors/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "sensors/msg/detail/control_data__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace sensors
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sensors
cdr_serialize(
  const sensors::msg::ControlData & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sensors
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  sensors::msg::ControlData & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sensors
get_serialized_size(
  const sensors::msg::ControlData & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sensors
max_serialized_size_ControlData(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace sensors

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sensors
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, sensors, msg, ControlData)();

#ifdef __cplusplus
}
#endif

#endif  // SENSORS__MSG__DETAIL__CONTROL_DATA__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
