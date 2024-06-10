// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sensors:srv/GetForward.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_FORWARD__BUILDER_HPP_
#define SENSORS__SRV__DETAIL__GET_FORWARD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sensors/srv/detail/get_forward__struct.hpp"
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
auto build<::sensors::srv::GetForward_Request>()
{
  return ::sensors::srv::GetForward_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace sensors


namespace sensors
{

namespace srv
{

namespace builder
{

class Init_GetForward_Response_forward_frame
{
public:
  Init_GetForward_Response_forward_frame()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sensors::srv::GetForward_Response forward_frame(::sensors::srv::GetForward_Response::_forward_frame_type arg)
  {
    msg_.forward_frame = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sensors::srv::GetForward_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sensors::srv::GetForward_Response>()
{
  return sensors::srv::builder::Init_GetForward_Response_forward_frame();
}

}  // namespace sensors

#endif  // SENSORS__SRV__DETAIL__GET_FORWARD__BUILDER_HPP_
