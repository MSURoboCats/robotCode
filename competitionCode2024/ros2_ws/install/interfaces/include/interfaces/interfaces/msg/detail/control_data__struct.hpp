// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/ControlData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__CONTROL_DATA__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__CONTROL_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'imu_data'
#include "sensor_msgs/msg/detail/imu__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__msg__ControlData __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__ControlData __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ControlData_
{
  using Type = ControlData_<ContainerAllocator>;

  explicit ControlData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : imu_data(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->depth = 0.0;
    }
  }

  explicit ControlData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : imu_data(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->depth = 0.0;
    }
  }

  // field types and members
  using _imu_data_type =
    sensor_msgs::msg::Imu_<ContainerAllocator>;
  _imu_data_type imu_data;
  using _depth_type =
    double;
  _depth_type depth;

  // setters for named parameter idiom
  Type & set__imu_data(
    const sensor_msgs::msg::Imu_<ContainerAllocator> & _arg)
  {
    this->imu_data = _arg;
    return *this;
  }
  Type & set__depth(
    const double & _arg)
  {
    this->depth = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::ControlData_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::ControlData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::ControlData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::ControlData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::ControlData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::ControlData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::ControlData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::ControlData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::ControlData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::ControlData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__ControlData
    std::shared_ptr<interfaces::msg::ControlData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__ControlData
    std::shared_ptr<interfaces::msg::ControlData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControlData_ & other) const
  {
    if (this->imu_data != other.imu_data) {
      return false;
    }
    if (this->depth != other.depth) {
      return false;
    }
    return true;
  }
  bool operator!=(const ControlData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControlData_

// alias to use template instance with default allocator
using ControlData =
  interfaces::msg::ControlData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__CONTROL_DATA__STRUCT_HPP_
