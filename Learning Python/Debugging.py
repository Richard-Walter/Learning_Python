import traceback
import logging
import os

# # Creating an exception in your code
# raise Exception('This is the error message')

# # Unhandled exception showing traceback
# def spam():
#     bacon()
# def bacon():
#     raise Exception('This is the error message.')
#
# spam()

# # Logging traceback allowing program to continue
#
# try:
#          raise Exception('This is the error message.')
# except:
#          errorFile = open('errorInfo.txt', 'w')
#          errorFile.write(traceback.format_exc())
#          errorFile.close()
#          print('The traceback info was written to errorInfo.txt.')
#
# # Assertions - raises an AssertionError.  Disabled by passing the -o option running python
# podBayDoorStatus = 'open'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

# # Logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of program')
#
#
# def factorial(n):
#
#     logging.debug('Start of factorial(%s)' % n)
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(%s)' % n)
#     return total
#
#
# print(factorial(5))
# logging.debug('End of program')
# print(os.getcwd())
#
# # Disable logging based on level
# logging.disable(logging.CRITICAL)   # Disable all messages at this level and below
# logging.critical('Critical error! Critical error!')
# logging.error('Error! Error!')

# Logging to a file
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Logging to file')
