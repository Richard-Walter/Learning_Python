
import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: Indicates something unexpected happened(e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Note:  Print functions still have their use, but also consider logging


# Default logging level is WARNING and log to console.  Change logging configuration
# Different format codes are available-see python logging docs for various options
# logging.basicConfig(filename='test.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(message)s')
#
#
# def add(x, y):
#     """Add Function"""
#     return x + y
#
#
# def subtract(x, y):
#     """Subtract Function"""
#     return x - y
#
#
# def multiply(x, y):
#     """Multiply Function"""
#     return x * y
#
#
# def divide(x, y):
#     """Divide Function"""
#     return x / y
#
#
# num_1 = 10
# num_2 = 5
#
# add_result = add(num_1, num_2)
# logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
#
# sub_result = subtract(num_1, num_2)
# logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
#
# mul_result = multiply(num_1, num_2)
# logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
#
# div_result = divide(num_1, num_2)
# logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


"""ADVANCED LOGGING-handlers, formatter, exceptions"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
