// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/UserStringCommand.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__USER_STRING_COMMAND__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__USER_STRING_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/user_string_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_UserStringCommand_Request_string_command
{
public:
  Init_UserStringCommand_Request_string_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::UserStringCommand_Request string_command(::interfaces::srv::UserStringCommand_Request::_string_command_type arg)
  {
    msg_.string_command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::UserStringCommand_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::UserStringCommand_Request>()
{
  return interfaces::srv::builder::Init_UserStringCommand_Request_string_command();
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
auto build<::interfaces::srv::UserStringCommand_Response>()
{
  return ::interfaces::srv::UserStringCommand_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__USER_STRING_COMMAND__BUILDER_HPP_
