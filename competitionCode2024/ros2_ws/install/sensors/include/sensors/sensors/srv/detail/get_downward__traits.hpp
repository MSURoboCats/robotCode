// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sensors:srv/GetDownward.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_DOWNWARD__TRAITS_HPP_
#define SENSORS__SRV__DETAIL__GET_DOWNWARD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sensors/srv/detail/get_downward__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sensors
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetDownward_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetDownward_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetDownward_Request & msg, bool use_flow_style = false)
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
  const sensors::srv::GetDownward_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  sensors::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sensors::srv::to_yaml() instead")]]
inline std::string to_yaml(const sensors::srv::GetDownward_Request & msg)
{
  return sensors::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sensors::srv::GetDownward_Request>()
{
  return "sensors::srv::GetDownward_Request";
}

template<>
inline const char * name<sensors::srv::GetDownward_Request>()
{
  return "sensors/srv/GetDownward_Request";
}

template<>
struct has_fixed_size<sensors::srv::GetDownward_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sensors::srv::GetDownward_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sensors::srv::GetDownward_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'downward_frame'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace sensors
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetDownward_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: downward_frame
  {
    out << "downward_frame: ";
    to_flow_style_yaml(msg.downward_frame, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetDownward_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: downward_frame
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "downward_frame:\n";
    to_block_style_yaml(msg.downward_frame, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetDownward_Response & msg, bool use_flow_style = false)
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
  const sensors::srv::GetDownward_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  sensors::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sensors::srv::to_yaml() instead")]]
inline std::string to_yaml(const sensors::srv::GetDownward_Response & msg)
{
  return sensors::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sensors::srv::GetDownward_Response>()
{
  return "sensors::srv::GetDownward_Response";
}

template<>
inline const char * name<sensors::srv::GetDownward_Response>()
{
  return "sensors/srv/GetDownward_Response";
}

template<>
struct has_fixed_size<sensors::srv::GetDownward_Response>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::Image>::value> {};

template<>
struct has_bounded_size<sensors::srv::GetDownward_Response>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::Image>::value> {};

template<>
struct is_message<sensors::srv::GetDownward_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sensors::srv::GetDownward>()
{
  return "sensors::srv::GetDownward";
}

template<>
inline const char * name<sensors::srv::GetDownward>()
{
  return "sensors/srv/GetDownward";
}

template<>
struct has_fixed_size<sensors::srv::GetDownward>
  : std::integral_constant<
    bool,
    has_fixed_size<sensors::srv::GetDownward_Request>::value &&
    has_fixed_size<sensors::srv::GetDownward_Response>::value
  >
{
};

template<>
struct has_bounded_size<sensors::srv::GetDownward>
  : std::integral_constant<
    bool,
    has_bounded_size<sensors::srv::GetDownward_Request>::value &&
    has_bounded_size<sensors::srv::GetDownward_Response>::value
  >
{
};

template<>
struct is_service<sensors::srv::GetDownward>
  : std::true_type
{
};

template<>
struct is_service_request<sensors::srv::GetDownward_Request>
  : std::true_type
{
};

template<>
struct is_service_response<sensors::srv::GetDownward_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SENSORS__SRV__DETAIL__GET_DOWNWARD__TRAITS_HPP_
