// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sensors:srv/GetVoltage.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_VOLTAGE__BUILDER_HPP_
#define SENSORS__SRV__DETAIL__GET_VOLTAGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sensors/srv/detail/get_voltage__struct.hpp"
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
auto build<::sensors::srv::GetVoltage_Request>()
{
  return ::sensors::srv::GetVoltage_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace sensors


namespace sensors
{

namespace srv
{

namespace builder
{

class Init_GetVoltage_Response_voltage
{
public:
  Init_GetVoltage_Response_voltage()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sensors::srv::GetVoltage_Response voltage(::sensors::srv::GetVoltage_Response::_voltage_type arg)
  {
    msg_.voltage = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sensors::srv::GetVoltage_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sensors::srv::GetVoltage_Response>()
{
  return sensors::srv::builder::Init_GetVoltage_Response_voltage();
}

}  // namespace sensors

#endif  // SENSORS__SRV__DETAIL__GET_VOLTAGE__BUILDER_HPP_
