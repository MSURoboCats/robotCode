// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Yolov8Detection.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/yolov8_detection__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Yolov8Detection_dimensions
{
public:
  explicit Init_Yolov8Detection_dimensions(::interfaces::msg::Yolov8Detection & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::Yolov8Detection dimensions(::interfaces::msg::Yolov8Detection::_dimensions_type arg)
  {
    msg_.dimensions = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Yolov8Detection msg_;
};

class Init_Yolov8Detection_center
{
public:
  explicit Init_Yolov8Detection_center(::interfaces::msg::Yolov8Detection & msg)
  : msg_(msg)
  {}
  Init_Yolov8Detection_dimensions center(::interfaces::msg::Yolov8Detection::_center_type arg)
  {
    msg_.center = std::move(arg);
    return Init_Yolov8Detection_dimensions(msg_);
  }

private:
  ::interfaces::msg::Yolov8Detection msg_;
};

class Init_Yolov8Detection_confidence
{
public:
  explicit Init_Yolov8Detection_confidence(::interfaces::msg::Yolov8Detection & msg)
  : msg_(msg)
  {}
  Init_Yolov8Detection_center confidence(::interfaces::msg::Yolov8Detection::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_Yolov8Detection_center(msg_);
  }

private:
  ::interfaces::msg::Yolov8Detection msg_;
};

class Init_Yolov8Detection_tracking_id
{
public:
  explicit Init_Yolov8Detection_tracking_id(::interfaces::msg::Yolov8Detection & msg)
  : msg_(msg)
  {}
  Init_Yolov8Detection_confidence tracking_id(::interfaces::msg::Yolov8Detection::_tracking_id_type arg)
  {
    msg_.tracking_id = std::move(arg);
    return Init_Yolov8Detection_confidence(msg_);
  }

private:
  ::interfaces::msg::Yolov8Detection msg_;
};

class Init_Yolov8Detection_name
{
public:
  Init_Yolov8Detection_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Yolov8Detection_tracking_id name(::interfaces::msg::Yolov8Detection::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_Yolov8Detection_tracking_id(msg_);
  }

private:
  ::interfaces::msg::Yolov8Detection msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Yolov8Detection>()
{
  return interfaces::msg::builder::Init_Yolov8Detection_name();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__BUILDER_HPP_
