// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/MotorPowers.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MOTOR_POWERS__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__MOTOR_POWERS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__MotorPowers_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__MotorPowers_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MotorPowers_Request_
{
  using Type = MotorPowers_Request_<ContainerAllocator>;

  explicit MotorPowers_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->motor1 = 0.0;
      this->motor2 = 0.0;
      this->motor3 = 0.0;
      this->motor4 = 0.0;
      this->motor5 = 0.0;
      this->motor6 = 0.0;
      this->motor7 = 0.0;
      this->motor8 = 0.0;
    }
  }

  explicit MotorPowers_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->motor1 = 0.0;
      this->motor2 = 0.0;
      this->motor3 = 0.0;
      this->motor4 = 0.0;
      this->motor5 = 0.0;
      this->motor6 = 0.0;
      this->motor7 = 0.0;
      this->motor8 = 0.0;
    }
  }

  // field types and members
  using _motor1_type =
    double;
  _motor1_type motor1;
  using _motor2_type =
    double;
  _motor2_type motor2;
  using _motor3_type =
    double;
  _motor3_type motor3;
  using _motor4_type =
    double;
  _motor4_type motor4;
  using _motor5_type =
    double;
  _motor5_type motor5;
  using _motor6_type =
    double;
  _motor6_type motor6;
  using _motor7_type =
    double;
  _motor7_type motor7;
  using _motor8_type =
    double;
  _motor8_type motor8;

  // setters for named parameter idiom
  Type & set__motor1(
    const double & _arg)
  {
    this->motor1 = _arg;
    return *this;
  }
  Type & set__motor2(
    const double & _arg)
  {
    this->motor2 = _arg;
    return *this;
  }
  Type & set__motor3(
    const double & _arg)
  {
    this->motor3 = _arg;
    return *this;
  }
  Type & set__motor4(
    const double & _arg)
  {
    this->motor4 = _arg;
    return *this;
  }
  Type & set__motor5(
    const double & _arg)
  {
    this->motor5 = _arg;
    return *this;
  }
  Type & set__motor6(
    const double & _arg)
  {
    this->motor6 = _arg;
    return *this;
  }
  Type & set__motor7(
    const double & _arg)
  {
    this->motor7 = _arg;
    return *this;
  }
  Type & set__motor8(
    const double & _arg)
  {
    this->motor8 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::MotorPowers_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::MotorPowers_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::MotorPowers_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::MotorPowers_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MotorPowers_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MotorPowers_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MotorPowers_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MotorPowers_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::MotorPowers_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::MotorPowers_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__MotorPowers_Request
    std::shared_ptr<interfaces::srv::MotorPowers_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__MotorPowers_Request
    std::shared_ptr<interfaces::srv::MotorPowers_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MotorPowers_Request_ & other) const
  {
    if (this->motor1 != other.motor1) {
      return false;
    }
    if (this->motor2 != other.motor2) {
      return false;
    }
    if (this->motor3 != other.motor3) {
      return false;
    }
    if (this->motor4 != other.motor4) {
      return false;
    }
    if (this->motor5 != other.motor5) {
      return false;
    }
    if (this->motor6 != other.motor6) {
      return false;
    }
    if (this->motor7 != other.motor7) {
      return false;
    }
    if (this->motor8 != other.motor8) {
      return false;
    }
    return true;
  }
  bool operator!=(const MotorPowers_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MotorPowers_Request_

// alias to use template instance with default allocator
using MotorPowers_Request =
  interfaces::srv::MotorPowers_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__MotorPowers_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__MotorPowers_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MotorPowers_Response_
{
  using Type = MotorPowers_Response_<ContainerAllocator>;

  explicit MotorPowers_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit MotorPowers_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::MotorPowers_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::MotorPowers_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::MotorPowers_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::MotorPowers_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MotorPowers_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MotorPowers_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::MotorPowers_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::MotorPowers_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::MotorPowers_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::MotorPowers_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__MotorPowers_Response
    std::shared_ptr<interfaces::srv::MotorPowers_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__MotorPowers_Response
    std::shared_ptr<interfaces::srv::MotorPowers_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MotorPowers_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const MotorPowers_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MotorPowers_Response_

// alias to use template instance with default allocator
using MotorPowers_Response =
  interfaces::srv::MotorPowers_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct MotorPowers
{
  using Request = interfaces::srv::MotorPowers_Request;
  using Response = interfaces::srv::MotorPowers_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__MOTOR_POWERS__STRUCT_HPP_
