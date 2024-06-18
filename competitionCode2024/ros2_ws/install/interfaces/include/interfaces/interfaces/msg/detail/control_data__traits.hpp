// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/ControlData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__CONTROL_DATA__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__CONTROL_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/msg/detail/control_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'imu_data'
#include "sensor_msgs/msg/detail/imu__traits.hpp"

namespace interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const ControlData & msg,
  std::ostream & out)
{
  out << "{";
  // member: imu_data
  {
    out << "imu_data: ";
    to_flow_style_yaml(msg.imu_data, out);
    out << ", ";
  }

  // member: depth
  {
    out << "depth: ";
    rosidl_generator_traits::value_to_yaml(msg.depth, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ControlData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: imu_data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "imu_data:\n";
    to_block_style_yaml(msg.imu_data, out, indentation + 2);
  }

  // member: depth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "depth: ";
    rosidl_generator_traits::value_to_yaml(msg.depth, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ControlData & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::msg::ControlData & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::msg::ControlData & msg)
{
  return interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::msg::ControlData>()
{
  return "interfaces::msg::ControlData";
}

template<>
inline const char * name<interfaces::msg::ControlData>()
{
  return "interfaces/msg/ControlData";
}

template<>
struct has_fixed_size<interfaces::msg::ControlData>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::Imu>::value> {};

template<>
struct has_bounded_size<interfaces::msg::ControlData>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::Imu>::value> {};

template<>
struct is_message<interfaces::msg::ControlData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__CONTROL_DATA__TRAITS_HPP_
