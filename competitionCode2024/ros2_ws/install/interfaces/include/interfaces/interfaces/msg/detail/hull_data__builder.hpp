// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/HullData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__HULL_DATA__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__HULL_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/hull_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_HullData_humidity
{
public:
  explicit Init_HullData_humidity(::interfaces::msg::HullData & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::HullData humidity(::interfaces::msg::HullData::_humidity_type arg)
  {
    msg_.humidity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::HullData msg_;
};

class Init_HullData_pressure
{
public:
  explicit Init_HullData_pressure(::interfaces::msg::HullData & msg)
  : msg_(msg)
  {}
  Init_HullData_humidity pressure(::interfaces::msg::HullData::_pressure_type arg)
  {
    msg_.pressure = std::move(arg);
    return Init_HullData_humidity(msg_);
  }

private:
  ::interfaces::msg::HullData msg_;
};

class Init_HullData_temperature
{
public:
  Init_HullData_temperature()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HullData_pressure temperature(::interfaces::msg::HullData::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_HullData_pressure(msg_);
  }

private:
  ::interfaces::msg::HullData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::HullData>()
{
  return interfaces::msg::builder::Init_HullData_temperature();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__HULL_DATA__BUILDER_HPP_
