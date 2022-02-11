def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    print(f"{value} = {rightMin + (valueScaled * rightSpan)}")
    return rightMin + (valueScaled * rightSpan)

if __name__ == "__main__":
    translate(1275, 1750, 1250, -100, 100)
