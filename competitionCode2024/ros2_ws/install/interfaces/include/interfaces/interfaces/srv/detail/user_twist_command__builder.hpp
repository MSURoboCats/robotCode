// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/UserTwistCommand.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/user_twist_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_UserTwistCommand_Request_twist_command
{
public:
  Init_UserTwistCommand_Request_twist_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::UserTwistCommand_Request twist_command(::interfaces::srv::UserTwistCommand_Request::_twist_command_type arg)
  {
    msg_.twist_command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::UserTwistCommand_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::UserTwistCommand_Request>()
{
  return interfaces::srv::builder::Init_UserTwistCommand_Request_twist_command();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::UserTwistCommand_Response>()
{
  return ::interfaces::srv::UserTwistCommand_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__BUILDER_HPP_
