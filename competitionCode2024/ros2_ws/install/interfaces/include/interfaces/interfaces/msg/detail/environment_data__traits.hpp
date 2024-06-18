// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/EnvironmentData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/msg/detail/environment_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'temperature'
#include "sensor_msgs/msg/detail/temperature__traits.hpp"
// Member 'pressure'
#include "sensor_msgs/msg/detail/fluid_pressure__traits.hpp"
// Member 'humidity'
#include "sensor_msgs/msg/detail/relative_humidity__traits.hpp"

namespace interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const EnvironmentData & msg,
  std::ostream & out)
{
  out << "{";
  // member: temperature
  {
    out << "temperature: ";
    to_flow_style_yaml(msg.temperature, out);
    out << ", ";
  }

  // member: pressure
  {
    out << "pressure: ";
    to_flow_style_yaml(msg.pressure, out);
    out << ", ";
  }

  // member: humidity
  {
    out << "humidity: ";
    to_flow_style_yaml(msg.humidity, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const EnvironmentData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: temperature
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature:\n";
    to_block_style_yaml(msg.temperature, out, indentation + 2);
  }

  // member: pressure
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pressure:\n";
    to_block_style_yaml(msg.pressure, out, indentation + 2);
  }

  // member: humidity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "humidity:\n";
    to_block_style_yaml(msg.humidity, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const EnvironmentData & msg, bool use_flow_style = false)
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
  const interfaces::msg::EnvironmentData & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::msg::EnvironmentData & msg)
{
  return interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::msg::EnvironmentData>()
{
  return "interfaces::msg::EnvironmentData";
}

template<>
inline const char * name<interfaces::msg::EnvironmentData>()
{
  return "interfaces/msg/EnvironmentData";
}

template<>
struct has_fixed_size<interfaces::msg::EnvironmentData>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::FluidPressure>::value && has_fixed_size<sensor_msgs::msg::RelativeHumidity>::value && has_fixed_size<sensor_msgs::msg::Temperature>::value> {};

template<>
struct has_bounded_size<interfaces::msg::EnvironmentData>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::FluidPressure>::value && has_bounded_size<sensor_msgs::msg::RelativeHumidity>::value && has_bounded_size<sensor_msgs::msg::Temperature>::value> {};

template<>
struct is_message<interfaces::msg::EnvironmentData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__TRAITS_HPP_
