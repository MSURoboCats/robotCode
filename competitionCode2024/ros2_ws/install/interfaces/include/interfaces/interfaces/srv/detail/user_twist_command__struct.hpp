// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/UserTwistCommand.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'twist_command'
#include "geometry_msgs/msg/detail/twist__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__srv__UserTwistCommand_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__UserTwistCommand_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct UserTwistCommand_Request_
{
  using Type = UserTwistCommand_Request_<ContainerAllocator>;

  explicit UserTwistCommand_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : twist_command(_init)
  {
    (void)_init;
  }

  explicit UserTwistCommand_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : twist_command(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _twist_command_type =
    geometry_msgs::msg::Twist_<ContainerAllocator>;
  _twist_command_type twist_command;

  // setters for named parameter idiom
  Type & set__twist_command(
    const geometry_msgs::msg::Twist_<ContainerAllocator> & _arg)
  {
    this->twist_command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::UserTwistCommand_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::UserTwistCommand_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::UserTwistCommand_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::UserTwistCommand_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::UserTwistCommand_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::UserTwistCommand_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::UserTwistCommand_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::UserTwistCommand_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::UserTwistCommand_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::UserTwistCommand_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__UserTwistCommand_Request
    std::shared_ptr<interfaces::srv::UserTwistCommand_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__UserTwistCommand_Request
    std::shared_ptr<interfaces::srv::UserTwistCommand_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const UserTwistCommand_Request_ & other) const
  {
    if (this->twist_command != other.twist_command) {
      return false;
    }
    return true;
  }
  bool operator!=(const UserTwistCommand_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct UserTwistCommand_Request_

// alias to use template instance with default allocator
using UserTwistCommand_Request =
  interfaces::srv::UserTwistCommand_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__UserTwistCommand_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__UserTwistCommand_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct UserTwistCommand_Response_
{
  using Type = UserTwistCommand_Response_<ContainerAllocator>;

  explicit UserTwistCommand_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit UserTwistCommand_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    interfaces::srv::UserTwistCommand_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::UserTwistCommand_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::UserTwistCommand_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::UserTwistCommand_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::UserTwistCommand_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::UserTwistCommand_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::UserTwistCommand_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::UserTwistCommand_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::UserTwistCommand_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::UserTwistCommand_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__UserTwistCommand_Response
    std::shared_ptr<interfaces::srv::UserTwistCommand_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__UserTwistCommand_Response
    std::shared_ptr<interfaces::srv::UserTwistCommand_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const UserTwistCommand_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const UserTwistCommand_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct UserTwistCommand_Response_

// alias to use template instance with default allocator
using UserTwistCommand_Response =
  interfaces::srv::UserTwistCommand_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct UserTwistCommand
{
  using Request = interfaces::srv::UserTwistCommand_Request;
  using Response = interfaces::srv::UserTwistCommand_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__USER_TWIST_COMMAND__STRUCT_HPP_
