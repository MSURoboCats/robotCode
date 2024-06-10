// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sensors:msg/ControlData.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__MSG__DETAIL__CONTROL_DATA__BUILDER_HPP_
#define SENSORS__MSG__DETAIL__CONTROL_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sensors/msg/detail/control_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sensors
{

namespace msg
{

namespace builder
{

class Init_ControlData_depth
{
public:
  explicit Init_ControlData_depth(::sensors::msg::ControlData & msg)
  : msg_(msg)
  {}
  ::sensors::msg::ControlData depth(::sensors::msg::ControlData::_depth_type arg)
  {
    msg_.depth = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sensors::msg::ControlData msg_;
};

class Init_ControlData_imu_data
{
public:
  Init_ControlData_imu_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlData_depth imu_data(::sensors::msg::ControlData::_imu_data_type arg)
  {
    msg_.imu_data = std::move(arg);
    return Init_ControlData_depth(msg_);
  }

private:
  ::sensors::msg::ControlData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sensors::msg::ControlData>()
{
  return sensors::msg::builder::Init_ControlData_imu_data();
}

}  // namespace sensors

#endif  // SENSORS__MSG__DETAIL__CONTROL_DATA__BUILDER_HPP_
