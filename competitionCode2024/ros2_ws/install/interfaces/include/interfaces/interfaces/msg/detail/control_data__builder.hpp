// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/ControlData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__CONTROL_DATA__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__CONTROL_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/control_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_ControlData_depth
{
public:
  explicit Init_ControlData_depth(::interfaces::msg::ControlData & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::ControlData depth(::interfaces::msg::ControlData::_depth_type arg)
  {
    msg_.depth = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::ControlData msg_;
};

class Init_ControlData_imu_data
{
public:
  Init_ControlData_imu_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlData_depth imu_data(::interfaces::msg::ControlData::_imu_data_type arg)
  {
    msg_.imu_data = std::move(arg);
    return Init_ControlData_depth(msg_);
  }

private:
  ::interfaces::msg::ControlData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::ControlData>()
{
  return interfaces::msg::builder::Init_ControlData_imu_data();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__CONTROL_DATA__BUILDER_HPP_
