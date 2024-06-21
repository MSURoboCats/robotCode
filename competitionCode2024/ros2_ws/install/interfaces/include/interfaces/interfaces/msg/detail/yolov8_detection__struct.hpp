// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/Yolov8Detection.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'center'
// Member 'dimensions'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__msg__Yolov8Detection __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__Yolov8Detection __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Yolov8Detection_
{
  using Type = Yolov8Detection_<ContainerAllocator>;

  explicit Yolov8Detection_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : center(_init),
    dimensions(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->name = "";
      this->tracking_id = 0ll;
      this->confidence = 0.0;
    }
  }

  explicit Yolov8Detection_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : name(_alloc),
    center(_alloc, _init),
    dimensions(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->name = "";
      this->tracking_id = 0ll;
      this->confidence = 0.0;
    }
  }

  // field types and members
  using _name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _name_type name;
  using _tracking_id_type =
    int64_t;
  _tracking_id_type tracking_id;
  using _confidence_type =
    double;
  _confidence_type confidence;
  using _center_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _center_type center;
  using _dimensions_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _dimensions_type dimensions;

  // setters for named parameter idiom
  Type & set__name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->name = _arg;
    return *this;
  }
  Type & set__tracking_id(
    const int64_t & _arg)
  {
    this->tracking_id = _arg;
    return *this;
  }
  Type & set__confidence(
    const double & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__center(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->center = _arg;
    return *this;
  }
  Type & set__dimensions(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->dimensions = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::Yolov8Detection_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::Yolov8Detection_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::Yolov8Detection_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::Yolov8Detection_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Yolov8Detection_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Yolov8Detection_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Yolov8Detection_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Yolov8Detection_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::Yolov8Detection_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::Yolov8Detection_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__Yolov8Detection
    std::shared_ptr<interfaces::msg::Yolov8Detection_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__Yolov8Detection
    std::shared_ptr<interfaces::msg::Yolov8Detection_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Yolov8Detection_ & other) const
  {
    if (this->name != other.name) {
      return false;
    }
    if (this->tracking_id != other.tracking_id) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->center != other.center) {
      return false;
    }
    if (this->dimensions != other.dimensions) {
      return false;
    }
    return true;
  }
  bool operator!=(const Yolov8Detection_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Yolov8Detection_

// alias to use template instance with default allocator
using Yolov8Detection =
  interfaces::msg::Yolov8Detection_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__YOLOV8_DETECTION__STRUCT_HPP_
