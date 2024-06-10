// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sensors:srv/GetControlData.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_CONTROL_DATA__TRAITS_HPP_
#define SENSORS__SRV__DETAIL__GET_CONTROL_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sensors/srv/detail/get_control_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sensors
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetControlData_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetControlData_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetControlData_Request & msg, bool use_flow_style = false)
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

}  // namespace sensors

namespace rosidl_generator_traits
{

[[deprecated("use sensors::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sensors::srv::GetControlData_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  sensors::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sensors::srv::to_yaml() instead")]]
inline std::string to_yaml(const sensors::srv::GetControlData_Request & msg)
{
  return sensors::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sensors::srv::GetControlData_Request>()
{
  return "sensors::srv::GetControlData_Request";
}

template<>
inline const char * name<sensors::srv::GetControlData_Request>()
{
  return "sensors/srv/GetControlData_Request";
}

template<>
struct has_fixed_size<sensors::srv::GetControlData_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sensors::srv::GetControlData_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sensors::srv::GetControlData_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'data'
#include "sensors/msg/detail/control_data__traits.hpp"

namespace sensors
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetControlData_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: data
  {
    out << "data: ";
    to_flow_style_yaml(msg.data, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetControlData_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "data:\n";
    to_block_style_yaml(msg.data, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetControlData_Response & msg, bool use_flow_style = false)
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

}  // namespace sensors

namespace rosidl_generator_traits
{

[[deprecated("use sensors::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sensors::srv::GetControlData_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  sensors::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sensors::srv::to_yaml() instead")]]
inline std::string to_yaml(const sensors::srv::GetControlData_Response & msg)
{
  return sensors::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sensors::srv::GetControlData_Response>()
{
  return "sensors::srv::GetControlData_Response";
}

template<>
inline const char * name<sensors::srv::GetControlData_Response>()
{
  return "sensors/srv/GetControlData_Response";
}

template<>
struct has_fixed_size<sensors::srv::GetControlData_Response>
  : std::integral_constant<bool, has_fixed_size<sensors::msg::ControlData>::value> {};

template<>
struct has_bounded_size<sensors::srv::GetControlData_Response>
  : std::integral_constant<bool, has_bounded_size<sensors::msg::ControlData>::value> {};

template<>
struct is_message<sensors::srv::GetControlData_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sensors::srv::GetControlData>()
{
  return "sensors::srv::GetControlData";
}

template<>
inline const char * name<sensors::srv::GetControlData>()
{
  return "sensors/srv/GetControlData";
}

template<>
struct has_fixed_size<sensors::srv::GetControlData>
  : std::integral_constant<
    bool,
    has_fixed_size<sensors::srv::GetControlData_Request>::value &&
    has_fixed_size<sensors::srv::GetControlData_Response>::value
  >
{
};

template<>
struct has_bounded_size<sensors::srv::GetControlData>
  : std::integral_constant<
    bool,
    has_bounded_size<sensors::srv::GetControlData_Request>::value &&
    has_bounded_size<sensors::srv::GetControlData_Response>::value
  >
{
};

template<>
struct is_service<sensors::srv::GetControlData>
  : std::true_type
{
};

template<>
struct is_service_request<sensors::srv::GetControlData_Request>
  : std::true_type
{
};

template<>
struct is_service_response<sensors::srv::GetControlData_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SENSORS__SRV__DETAIL__GET_CONTROL_DATA__TRAITS_HPP_
