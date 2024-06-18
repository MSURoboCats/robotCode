// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/ControlData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__CONTROL_DATA__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__CONTROL_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/control_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::ControlData_Request>()
{
  return ::interfaces::srv::ControlData_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_ControlData_Response_depth
{
public:
  explicit Init_ControlData_Response_depth(::interfaces::srv::ControlData_Response & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::ControlData_Response depth(::interfaces::srv::ControlData_Response::_depth_type arg)
  {
    msg_.depth = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::ControlData_Response msg_;
};

class Init_ControlData_Response_imu_data
{
public:
  Init_ControlData_Response_imu_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlData_Response_depth imu_data(::interfaces::srv::ControlData_Response::_imu_data_type arg)
  {
    msg_.imu_data = std::move(arg);
    return Init_ControlData_Response_depth(msg_);
  }

private:
  ::interfaces::srv::ControlData_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::ControlData_Response>()
{
  return interfaces::srv::builder::Init_ControlData_Response_imu_data();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__CONTROL_DATA__BUILDER_HPP_
