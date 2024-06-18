// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/BatHealth.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__BAT_HEALTH__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__BAT_HEALTH__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/bat_health__struct.hpp"
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
auto build<::interfaces::srv::BatHealth_Request>()
{
  return ::interfaces::srv::BatHealth_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_BatHealth_Response_voltage
{
public:
  Init_BatHealth_Response_voltage()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::BatHealth_Response voltage(::interfaces::srv::BatHealth_Response::_voltage_type arg)
  {
    msg_.voltage = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::BatHealth_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::BatHealth_Response>()
{
  return interfaces::srv::builder::Init_BatHealth_Response_voltage();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__BAT_HEALTH__BUILDER_HPP_
