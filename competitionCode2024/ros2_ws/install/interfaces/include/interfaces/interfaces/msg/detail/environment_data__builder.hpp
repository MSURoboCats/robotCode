// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/EnvironmentData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/environment_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_EnvironmentData_humidity
{
public:
  explicit Init_EnvironmentData_humidity(::interfaces::msg::EnvironmentData & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::EnvironmentData humidity(::interfaces::msg::EnvironmentData::_humidity_type arg)
  {
    msg_.humidity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::EnvironmentData msg_;
};

class Init_EnvironmentData_pressure
{
public:
  explicit Init_EnvironmentData_pressure(::interfaces::msg::EnvironmentData & msg)
  : msg_(msg)
  {}
  Init_EnvironmentData_humidity pressure(::interfaces::msg::EnvironmentData::_pressure_type arg)
  {
    msg_.pressure = std::move(arg);
    return Init_EnvironmentData_humidity(msg_);
  }

private:
  ::interfaces::msg::EnvironmentData msg_;
};

class Init_EnvironmentData_temperature
{
public:
  Init_EnvironmentData_temperature()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_EnvironmentData_pressure temperature(::interfaces::msg::EnvironmentData::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_EnvironmentData_pressure(msg_);
  }

private:
  ::interfaces::msg::EnvironmentData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::EnvironmentData>()
{
  return interfaces::msg::builder::Init_EnvironmentData_temperature();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__BUILDER_HPP_
