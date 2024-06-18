// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/ControlData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__CONTROL_DATA__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__CONTROL_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/srv/detail/control_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const ControlData_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ControlData_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ControlData_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::srv::ControlData_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::ControlData_Request & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::ControlData_Request>()
{
  return "interfaces::srv::ControlData_Request";
}

template<>
inline const char * name<interfaces::srv::ControlData_Request>()
{
  return "interfaces/srv/ControlData_Request";
}

template<>
struct has_fixed_size<interfaces::srv::ControlData_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::ControlData_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::ControlData_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'imu_data'
#include "sensor_msgs/msg/detail/imu__traits.hpp"

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const ControlData_Response & msg,
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
  const ControlData_Response & msg,
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

inline std::string to_yaml(const ControlData_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::srv::ControlData_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::ControlData_Response & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::ControlData_Response>()
{
  return "interfaces::srv::ControlData_Response";
}

template<>
inline const char * name<interfaces::srv::ControlData_Response>()
{
  return "interfaces/srv/ControlData_Response";
}

template<>
struct has_fixed_size<interfaces::srv::ControlData_Response>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::Imu>::value> {};

template<>
struct has_bounded_size<interfaces::srv::ControlData_Response>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::Imu>::value> {};

template<>
struct is_message<interfaces::srv::ControlData_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::ControlData>()
{
  return "interfaces::srv::ControlData";
}

template<>
inline const char * name<interfaces::srv::ControlData>()
{
  return "interfaces/srv/ControlData";
}

template<>
struct has_fixed_size<interfaces::srv::ControlData>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::ControlData_Request>::value &&
    has_fixed_size<interfaces::srv::ControlData_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::ControlData>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::ControlData_Request>::value &&
    has_bounded_size<interfaces::srv::ControlData_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::ControlData>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::ControlData_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::ControlData_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__CONTROL_DATA__TRAITS_HPP_
