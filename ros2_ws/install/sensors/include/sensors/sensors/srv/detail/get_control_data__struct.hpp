// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sensors:srv/GetControlData.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_CONTROL_DATA__STRUCT_HPP_
#define SENSORS__SRV__DETAIL__GET_CONTROL_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sensors__srv__GetControlData_Request __attribute__((deprecated))
#else
# define DEPRECATED__sensors__srv__GetControlData_Request __declspec(deprecated)
#endif

namespace sensors
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetControlData_Request_
{
  using Type = GetControlData_Request_<ContainerAllocator>;

  explicit GetControlData_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit GetControlData_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    sensors::srv::GetControlData_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const sensors::srv::GetControlData_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sensors::srv::GetControlData_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sensors::srv::GetControlData_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sensors::srv::GetControlData_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sensors::srv::GetControlData_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sensors::srv::GetControlData_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sensors::srv::GetControlData_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sensors::srv::GetControlData_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sensors::srv::GetControlData_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sensors__srv__GetControlData_Request
    std::shared_ptr<sensors::srv::GetControlData_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sensors__srv__GetControlData_Request
    std::shared_ptr<sensors::srv::GetControlData_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetControlData_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetControlData_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetControlData_Request_

// alias to use template instance with default allocator
using GetControlData_Request =
  sensors::srv::GetControlData_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sensors


// Include directives for member types
// Member 'data'
#include "sensors/msg/detail/control_data__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__sensors__srv__GetControlData_Response __attribute__((deprecated))
#else
# define DEPRECATED__sensors__srv__GetControlData_Response __declspec(deprecated)
#endif

namespace sensors
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetControlData_Response_
{
  using Type = GetControlData_Response_<ContainerAllocator>;

  explicit GetControlData_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : data(_init)
  {
    (void)_init;
  }

  explicit GetControlData_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : data(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _data_type =
    sensors::msg::ControlData_<ContainerAllocator>;
  _data_type data;

  // setters for named parameter idiom
  Type & set__data(
    const sensors::msg::ControlData_<ContainerAllocator> & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sensors::srv::GetControlData_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const sensors::srv::GetControlData_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sensors::srv::GetControlData_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sensors::srv::GetControlData_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sensors::srv::GetControlData_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sensors::srv::GetControlData_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sensors::srv::GetControlData_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sensors::srv::GetControlData_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sensors::srv::GetControlData_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sensors::srv::GetControlData_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sensors__srv__GetControlData_Response
    std::shared_ptr<sensors::srv::GetControlData_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sensors__srv__GetControlData_Response
    std::shared_ptr<sensors::srv::GetControlData_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetControlData_Response_ & other) const
  {
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetControlData_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetControlData_Response_

// alias to use template instance with default allocator
using GetControlData_Response =
  sensors::srv::GetControlData_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sensors

namespace sensors
{

namespace srv
{

struct GetControlData
{
  using Request = sensors::srv::GetControlData_Request;
  using Response = sensors::srv::GetControlData_Response;
};

}  // namespace srv

}  // namespace sensors

#endif  // SENSORS__SRV__DETAIL__GET_CONTROL_DATA__STRUCT_HPP_
