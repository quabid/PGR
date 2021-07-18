from .StatusMessenger import custom, success, warning, error
from .NumberPatternManager import float_pattern, integer_pattern
from .DialogMessinger import MESSINGER_SWITCH


# Number converters


def to_hex(arg):
    if float_pattern.search(arg):
        return float.hex(float(arg))
    else:
        num = int(arg.strip())
        return hex(num).lstrip("0x").rstrip("L")


def to_octal(arg):
    num = 0
    if float_pattern.search(arg):
        debug(arg)

        try:
            num = int(arg)
            return oct(num)
        except ValueError as e:
            message = "Error casting {} to an integer".format(arg)

            function = MESSAGE_SWITCH["error"]
            function("casting error".title(), message)

            raise ValueError("Error casting {} to an integer".format(arg),
                             "Cause: {} is a floating point number".format(
                                 arg),
                             "Unable to cast {} to an integer".format(arg))

    else:
        num = int(arg)
        return oct(num).lstrip("0o").rstrip("L")


def to_binary(arg):
    num = 0
    if float_pattern.search(arg):
        debug(arg)

        try:
            num = int(arg)
            return "{0:b}".format(num)
        except ValueError as e:
            message = "Error casting {} to an integer".format(arg)

            function = MESSAGE_SWITCH["error"]
            function("casting error".title(), message)

            raise ValueError("Error casting {} to an integer".format(arg),
                             "Cause: {} is a floating point number".format(
                                 arg),
                             "Unable to cast {} to an integer".format(arg))

    else:
        num = int(arg)
        return "{0:b}".format(num)


def debug(arg):
    message = warning("Warning: {} is a floating point number\n\tConverting {} to an integer, so the precision will be lost\n".format(
        arg, arg))
    print("\t{}\n".format(message))
