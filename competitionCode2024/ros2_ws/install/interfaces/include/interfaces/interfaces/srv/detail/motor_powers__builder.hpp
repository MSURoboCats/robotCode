// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/MotorPowers.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MOTOR_POWERS__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__MOTOR_POWERS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/motor_powers__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_MotorPowers_Request_motor8
{
public:
  explicit Init_MotorPowers_Request_motor8(::interfaces::srv::MotorPowers_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::MotorPowers_Request motor8(::interfaces::srv::MotorPowers_Request::_motor8_type arg)
  {
    msg_.motor8 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::MotorPowers_Request msg_;
};

class Init_MotorPowers_Request_motor7
{
public:
  explicit Init_MotorPowers_Request_motor7(::interfaces::srv::MotorPowers_Request & msg)
  : msg_(msg)
  {}
  Init_MotorPowers_Request_motor8 motor7(::interfaces::srv::MotorPowers_Request::_motor7_type arg)
  {
    msg_.motor7 = std::move(arg);
    return Init_MotorPowers_Request_motor8(msg_);
  }

private:
  ::interfaces::srv::MotorPowers_Request msg_;
};

class Init_MotorPowers_Request_motor6
{
public:
  explicit Init_MotorPowers_Request_motor6(::interfaces::srv::MotorPowers_Request & msg)
  : msg_(msg)
  {}
  Init_MotorPowers_Request_motor7 motor6(::interfaces::srv::MotorPowers_Request::_motor6_type arg)
  {
    msg_.motor6 = std::move(arg);
    return Init_MotorPowers_Request_motor7(msg_);
  }

private:
  ::interfaces::srv::MotorPowers_Request msg_;
};

class Init_MotorPowers_Request_motor5
{
public:
  explicit Init_MotorPowers_Request_motor5(::interfaces::srv::MotorPowers_Request & msg)
  : msg_(msg)
  {}
  Init_MotorPowers_Request_motor6 motor5(::interfaces::srv::MotorPowers_Request::_motor5_type arg)
  {
    msg_.motor5 = std::move(arg);
    return Init_MotorPowers_Request_motor6(msg_);
  }

private:
  ::interfaces::srv::MotorPowers_Request msg_;
};

class Init_MotorPowers_Request_motor4
{
public:
  explicit Init_MotorPowers_Request_motor4(::interfaces::srv::MotorPowers_Request & msg)
  : msg_(msg)
  {}
  Init_MotorPowers_Request_motor5 motor4(::interfaces::srv::MotorPowers_Request::_motor4_type arg)
  {
    msg_.motor4 = std::move(arg);
    return Init_MotorPowers_Request_motor5(msg_);
  }

private:
  ::interfaces::srv::MotorPowers_Request msg_;
};

class Init_MotorPowers_Request_motor3
{
public:
  explicit Init_MotorPowers_Request_motor3(::interfaces::srv::MotorPowers_Request & msg)
  : msg_(msg)
  {}
  Init_MotorPowers_Request_motor4 motor3(::interfaces::srv::MotorPowers_Request::_motor3_type arg)
  {
    msg_.motor3 = std::move(arg);
    return Init_MotorPowers_Request_motor4(msg_);
  }

private:
  ::interfaces::srv::MotorPowers_Request msg_;
};

class Init_MotorPowers_Request_motor2
{
public:
  explicit Init_MotorPowers_Request_motor2(::interfaces::srv::MotorPowers_Request & msg)
  : msg_(msg)
  {}
  Init_MotorPowers_Request_motor3 motor2(::interfaces::srv::MotorPowers_Request::_motor2_type arg)
  {
    msg_.motor2 = std::move(arg);
    return Init_MotorPowers_Request_motor3(msg_);
  }

private:
  ::interfaces::srv::MotorPowers_Request msg_;
};

class Init_MotorPowers_Request_motor1
{
public:
  Init_MotorPowers_Request_motor1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorPowers_Request_motor2 motor1(::interfaces::srv::MotorPowers_Request::_motor1_type arg)
  {
    msg_.motor1 = std::move(arg);
    return Init_MotorPowers_Request_motor2(msg_);
  }

private:
  ::interfaces::srv::MotorPowers_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::MotorPowers_Request>()
{
  return interfaces::srv::builder::Init_MotorPowers_Request_motor1();
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
auto build<::interfaces::srv::MotorPowers_Response>()
{
  return ::interfaces::srv::MotorPowers_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__MOTOR_POWERS__BUILDER_HPP_
