// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sensors:srv/GetForward.idl
// generated code does not contain a copyright notice

#ifndef SENSORS__SRV__DETAIL__GET_FORWARD__STRUCT_HPP_
#define SENSORS__SRV__DETAIL__GET_FORWARD__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sensors__srv__GetForward_Request __attribute__((deprecated))
#else
# define DEPRECATED__sensors__srv__GetForward_Request __declspec(deprecated)
#endif

namespace sensors
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetForward_Request_
{
  using Type = GetForward_Request_<ContainerAllocator>;

  explicit GetForward_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit GetForward_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    sensors::srv::GetForward_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const sensors::srv::GetForward_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sensors::srv::GetForward_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sensors::srv::GetForward_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sensors::srv::GetForward_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sensors::srv::GetForward_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sensors::srv::GetForward_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sensors::srv::GetForward_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sensors::srv::GetForward_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sensors::srv::GetForward_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sensors__srv__GetForward_Request
    std::shared_ptr<sensors::srv::GetForward_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sensors__srv__GetForward_Request
    std::shared_ptr<sensors::srv::GetForward_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetForward_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetForward_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetForward_Request_

// alias to use template instance with default allocator
using GetForward_Request =
  sensors::srv::GetForward_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sensors


// Include directives for member types
// Member 'forward_frame'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__sensors__srv__GetForward_Response __attribute__((deprecated))
#else
# define DEPRECATED__sensors__srv__GetForward_Response __declspec(deprecated)
#endif

namespace sensors
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetForward_Response_
{
  using Type = GetForward_Response_<ContainerAllocator>;

  explicit GetForward_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : forward_frame(_init)
  {
    (void)_init;
  }

  explicit GetForward_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : forward_frame(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _forward_frame_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _forward_frame_type forward_frame;

  // setters for named parameter idiom
  Type & set__forward_frame(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->forward_frame = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sensors::srv::GetForward_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const sensors::srv::GetForward_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sensors::srv::GetForward_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sensors::srv::GetForward_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sensors::srv::GetForward_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sensors::srv::GetForward_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sensors::srv::GetForward_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sensors::srv::GetForward_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sensors::srv::GetForward_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sensors::srv::GetForward_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sensors__srv__GetForward_Response
    std::shared_ptr<sensors::srv::GetForward_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sensors__srv__GetForward_Response
    std::shared_ptr<sensors::srv::GetForward_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetForward_Response_ & other) const
  {
    if (this->forward_frame != other.forward_frame) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetForward_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetForward_Response_

// alias to use template instance with default allocator
using GetForward_Response =
  sensors::srv::GetForward_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sensors

namespace sensors
{

namespace srv
{

struct GetForward
{
  using Request = sensors::srv::GetForward_Request;
  using Response = sensors::srv::GetForward_Response;
};

}  // namespace srv

}  // namespace sensors

#endif  // SENSORS__SRV__DETAIL__GET_FORWARD__STRUCT_HPP_
