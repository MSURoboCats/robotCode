// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/Yolov8Detection.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/msg/detail/yolov8_detection__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'center'
// Member 'dimensions'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Yolov8Detection & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: tracking_id
  {
    out << "tracking_id: ";
    rosidl_generator_traits::value_to_yaml(msg.tracking_id, out);
    out << ", ";
  }

  // member: confidence
  {
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << ", ";
  }

  // member: center
  {
    out << "center: ";
    to_flow_style_yaml(msg.center, out);
    out << ", ";
  }

  // member: dimensions
  {
    out << "dimensions: ";
    to_flow_style_yaml(msg.dimensions, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Yolov8Detection & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: tracking_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tracking_id: ";
    rosidl_generator_traits::value_to_yaml(msg.tracking_id, out);
    out << "\n";
  }

  // member: confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << "\n";
  }

  // member: center
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "center:\n";
    to_block_style_yaml(msg.center, out, indentation + 2);
  }

  // member: dimensions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dimensions:\n";
    to_block_style_yaml(msg.dimensions, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Yolov8Detection & msg, bool use_flow_style = false)
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
  const interfaces::msg::Yolov8Detection & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::msg::Yolov8Detection & msg)
{
  return interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::msg::Yolov8Detection>()
{
  return "interfaces::msg::Yolov8Detection";
}

template<>
inline const char * name<interfaces::msg::Yolov8Detection>()
{
  return "interfaces/msg/Yolov8Detection";
}

template<>
struct has_fixed_size<interfaces::msg::Yolov8Detection>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces::msg::Yolov8Detection>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interfaces::msg::Yolov8Detection>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__TRAITS_HPP_
