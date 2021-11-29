# System packages/modules
import sys

# IDAPython
import ida_kernwin


def is_python_version_supported() -> bool:
    """
    Checks if the Python version number is higher or
      equal to 3.8
    @return: sys.version_info >= 3.8
    """
    minimum_major = 3
    minimum_minor = 8
    return sys.version_info >= (minimum_major, minimum_minor)


def is_ida_version_supported() -> bool:
    """
    Checks if the IDA kernel version is higher or
      equal to 7.5
    @return: ida_kernel_version >= 7.5
    """
    minimum_major = 7
    minimum_minor = 5

    ida_kernel_version = tuple(map(int, ida_kernwin.get_kernel_version().split(".")))
    return ida_kernel_version >= (minimum_major, minimum_minor)