// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/MotorPowers.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MOTOR_POWERS__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__MOTOR_POWERS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/srv/detail/motor_powers__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const MotorPowers_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: motor1
  {
    out << "motor1: ";
    rosidl_generator_traits::value_to_yaml(msg.motor1, out);
    out << ", ";
  }

  // member: motor2
  {
    out << "motor2: ";
    rosidl_generator_traits::value_to_yaml(msg.motor2, out);
    out << ", ";
  }

  // member: motor3
  {
    out << "motor3: ";
    rosidl_generator_traits::value_to_yaml(msg.motor3, out);
    out << ", ";
  }

  // member: motor4
  {
    out << "motor4: ";
    rosidl_generator_traits::value_to_yaml(msg.motor4, out);
    out << ", ";
  }

  // member: motor5
  {
    out << "motor5: ";
    rosidl_generator_traits::value_to_yaml(msg.motor5, out);
    out << ", ";
  }

  // member: motor6
  {
    out << "motor6: ";
    rosidl_generator_traits::value_to_yaml(msg.motor6, out);
    out << ", ";
  }

  // member: motor7
  {
    out << "motor7: ";
    rosidl_generator_traits::value_to_yaml(msg.motor7, out);
    out << ", ";
  }

  // member: motor8
  {
    out << "motor8: ";
    rosidl_generator_traits::value_to_yaml(msg.motor8, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MotorPowers_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: motor1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor1: ";
    rosidl_generator_traits::value_to_yaml(msg.motor1, out);
    out << "\n";
  }

  // member: motor2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor2: ";
    rosidl_generator_traits::value_to_yaml(msg.motor2, out);
    out << "\n";
  }

  // member: motor3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor3: ";
    rosidl_generator_traits::value_to_yaml(msg.motor3, out);
    out << "\n";
  }

  // member: motor4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor4: ";
    rosidl_generator_traits::value_to_yaml(msg.motor4, out);
    out << "\n";
  }

  // member: motor5
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor5: ";
    rosidl_generator_traits::value_to_yaml(msg.motor5, out);
    out << "\n";
  }

  // member: motor6
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor6: ";
    rosidl_generator_traits::value_to_yaml(msg.motor6, out);
    out << "\n";
  }

  // member: motor7
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor7: ";
    rosidl_generator_traits::value_to_yaml(msg.motor7, out);
    out << "\n";
  }

  // member: motor8
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor8: ";
    rosidl_generator_traits::value_to_yaml(msg.motor8, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MotorPowers_Request & msg, bool use_flow_style = false)
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
  const interfaces::srv::MotorPowers_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::MotorPowers_Request & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::MotorPowers_Request>()
{
  return "interfaces::srv::MotorPowers_Request";
}

template<>
inline const char * name<interfaces::srv::MotorPowers_Request>()
{
  return "interfaces/srv/MotorPowers_Request";
}

template<>
struct has_fixed_size<interfaces::srv::MotorPowers_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::MotorPowers_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::MotorPowers_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const MotorPowers_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MotorPowers_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MotorPowers_Response & msg, bool use_flow_style = false)
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
  const interfaces::srv::MotorPowers_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::MotorPowers_Response & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::MotorPowers_Response>()
{
  return "interfaces::srv::MotorPowers_Response";
}

template<>
inline const char * name<interfaces::srv::MotorPowers_Response>()
{
  return "interfaces/srv/MotorPowers_Response";
}

template<>
struct has_fixed_size<interfaces::srv::MotorPowers_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::MotorPowers_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::MotorPowers_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::MotorPowers>()
{
  return "interfaces::srv::MotorPowers";
}

template<>
inline const char * name<interfaces::srv::MotorPowers>()
{
  return "interfaces/srv/MotorPowers";
}

template<>
struct has_fixed_size<interfaces::srv::MotorPowers>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::MotorPowers_Request>::value &&
    has_fixed_size<interfaces::srv::MotorPowers_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::MotorPowers>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::MotorPowers_Request>::value &&
    has_bounded_size<interfaces::srv::MotorPowers_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::MotorPowers>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::MotorPowers_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::MotorPowers_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__MOTOR_POWERS__TRAITS_HPP_
