// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sensors:srv/GetVoltage.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_VOLTAGE__TRAITS_HPP_
#define SENSORS__SRV__DETAIL__GET_VOLTAGE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sensors/srv/detail/get_voltage__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sensors
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetVoltage_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetVoltage_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetVoltage_Request & msg, bool use_flow_style = false)
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
  const sensors::srv::GetVoltage_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  sensors::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sensors::srv::to_yaml() instead")]]
inline std::string to_yaml(const sensors::srv::GetVoltage_Request & msg)
{
  return sensors::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sensors::srv::GetVoltage_Request>()
{
  return "sensors::srv::GetVoltage_Request";
}

template<>
inline const char * name<sensors::srv::GetVoltage_Request>()
{
  return "sensors/srv/GetVoltage_Request";
}

template<>
struct has_fixed_size<sensors::srv::GetVoltage_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sensors::srv::GetVoltage_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sensors::srv::GetVoltage_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'voltage'
#include "sensor_msgs/msg/detail/battery_state__traits.hpp"

namespace sensors
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetVoltage_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: voltage
  {
    out << "voltage: ";
    to_flow_style_yaml(msg.voltage, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetVoltage_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: voltage
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "voltage:\n";
    to_block_style_yaml(msg.voltage, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetVoltage_Response & msg, bool use_flow_style = false)
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
  const sensors::srv::GetVoltage_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  sensors::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sensors::srv::to_yaml() instead")]]
inline std::string to_yaml(const sensors::srv::GetVoltage_Response & msg)
{
  return sensors::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sensors::srv::GetVoltage_Response>()
{
  return "sensors::srv::GetVoltage_Response";
}

template<>
inline const char * name<sensors::srv::GetVoltage_Response>()
{
  return "sensors/srv/GetVoltage_Response";
}

template<>
struct has_fixed_size<sensors::srv::GetVoltage_Response>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::BatteryState>::value> {};

template<>
struct has_bounded_size<sensors::srv::GetVoltage_Response>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::BatteryState>::value> {};

template<>
struct is_message<sensors::srv::GetVoltage_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sensors::srv::GetVoltage>()
{
  return "sensors::srv::GetVoltage";
}

template<>
inline const char * name<sensors::srv::GetVoltage>()
{
  return "sensors/srv/GetVoltage";
}

template<>
struct has_fixed_size<sensors::srv::GetVoltage>
  : std::integral_constant<
    bool,
    has_fixed_size<sensors::srv::GetVoltage_Request>::value &&
    has_fixed_size<sensors::srv::GetVoltage_Response>::value
  >
{
};

template<>
struct has_bounded_size<sensors::srv::GetVoltage>
  : std::integral_constant<
    bool,
    has_bounded_size<sensors::srv::GetVoltage_Request>::value &&
    has_bounded_size<sensors::srv::GetVoltage_Response>::value
  >
{
};

template<>
struct is_service<sensors::srv::GetVoltage>
  : std::true_type
{
};

template<>
struct is_service_request<sensors::srv::GetVoltage_Request>
  : std::true_type
{
};

template<>
struct is_service_response<sensors::srv::GetVoltage_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SENSORS__SRV__DETAIL__GET_VOLTAGE__TRAITS_HPP_
