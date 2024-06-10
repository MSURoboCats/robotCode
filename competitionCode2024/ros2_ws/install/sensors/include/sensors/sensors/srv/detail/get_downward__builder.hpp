// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sensors:srv/GetDownward.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_DOWNWARD__BUILDER_HPP_
#define SENSORS__SRV__DETAIL__GET_DOWNWARD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sensors/srv/detail/get_downward__struct.hpp"
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
auto build<::sensors::srv::GetDownward_Request>()
{
  return ::sensors::srv::GetDownward_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace sensors


namespace sensors
{

namespace srv
{

namespace builder
{

class Init_GetDownward_Response_downward_frame
{
public:
  Init_GetDownward_Response_downward_frame()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sensors::srv::GetDownward_Response downward_frame(::sensors::srv::GetDownward_Response::_downward_frame_type arg)
  {
    msg_.downward_frame = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sensors::srv::GetDownward_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sensors::srv::GetDownward_Response>()
{
  return sensors::srv::builder::Init_GetDownward_Response_downward_frame();
}

}  // namespace sensors

#endif  // SENSORS__SRV__DETAIL__GET_DOWNWARD__BUILDER_HPP_
