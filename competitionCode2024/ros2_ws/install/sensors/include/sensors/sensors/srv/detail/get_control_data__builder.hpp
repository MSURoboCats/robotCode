// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sensors:srv/GetControlData.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_CONTROL_DATA__BUILDER_HPP_
#define SENSORS__SRV__DETAIL__GET_CONTROL_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sensors/srv/detail/get_control_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sensors
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sensors::srv::GetControlData_Request>()
{
  return ::sensors::srv::GetControlData_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace sensors


namespace sensors
{

namespace srv
{

namespace builder
{

class Init_GetControlData_Response_data
{
public:
  Init_GetControlData_Response_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sensors::srv::GetControlData_Response data(::sensors::srv::GetControlData_Response::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sensors::srv::GetControlData_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sensors::srv::GetControlData_Response>()
{
  return sensors::srv::builder::Init_GetControlData_Response_data();
}

}  // namespace sensors

#endif  // SENSORS__SRV__DETAIL__GET_CONTROL_DATA__BUILDER_HPP_