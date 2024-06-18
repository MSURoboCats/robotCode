// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/EnvironmentData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'temperature'
#include "sensor_msgs/msg/detail/temperature__struct.hpp"
// Member 'pressure'
#include "sensor_msgs/msg/detail/fluid_pressure__struct.hpp"
// Member 'humidity'
#include "sensor_msgs/msg/detail/relative_humidity__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__msg__EnvironmentData __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__EnvironmentData __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct EnvironmentData_
{
  using Type = EnvironmentData_<ContainerAllocator>;

  explicit EnvironmentData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : temperature(_init),
    pressure(_init),
    humidity(_init)
  {
    (void)_init;
  }

  explicit EnvironmentData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : temperature(_alloc, _init),
    pressure(_alloc, _init),
    humidity(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _temperature_type =
    sensor_msgs::msg::Temperature_<ContainerAllocator>;
  _temperature_type temperature;
  using _pressure_type =
    sensor_msgs::msg::FluidPressure_<ContainerAllocator>;
  _pressure_type pressure;
  using _humidity_type =
    sensor_msgs::msg::RelativeHumidity_<ContainerAllocator>;
  _humidity_type humidity;

  // setters for named parameter idiom
  Type & set__temperature(
    const sensor_msgs::msg::Temperature_<ContainerAllocator> & _arg)
  {
    this->temperature = _arg;
    return *this;
  }
  Type & set__pressure(
    const sensor_msgs::msg::FluidPressure_<ContainerAllocator> & _arg)
  {
    this->pressure = _arg;
    return *this;
  }
  Type & set__humidity(
    const sensor_msgs::msg::RelativeHumidity_<ContainerAllocator> & _arg)
  {
    this->humidity = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::EnvironmentData_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::EnvironmentData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::EnvironmentData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::EnvironmentData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::EnvironmentData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::EnvironmentData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::EnvironmentData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::EnvironmentData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::EnvironmentData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::EnvironmentData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__EnvironmentData
    std::shared_ptr<interfaces::msg::EnvironmentData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__EnvironmentData
    std::shared_ptr<interfaces::msg::EnvironmentData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EnvironmentData_ & other) const
  {
    if (this->temperature != other.temperature) {
      return false;
    }
    if (this->pressure != other.pressure) {
      return false;
    }
    if (this->humidity != other.humidity) {
      return false;
    }
    return true;
  }
  bool operator!=(const EnvironmentData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EnvironmentData_

// alias to use template instance with default allocator
using EnvironmentData =
  interfaces::msg::EnvironmentData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__ENVIRONMENT_DATA__STRUCT_HPP_
