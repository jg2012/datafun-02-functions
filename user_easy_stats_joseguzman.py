# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

xtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


logger.info("xtimes = " + str(xtimes))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(xtimes)
median = statistics.median(xtimes)
mode = statistics.mode(xtimes)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(xtimes)
stdev = statistics.stdev(xtimes)
lowest = min(xtimes)
highest = max(xtimes)

# TODO: change to f-strings and display 2 decimal places (like we did above)
logger.info(f"var    = {var:.2f}")
logger.info(f"stdev  = {stdev:.2f}")
logger.info(f"lowest = {lowest:.2f}")
logger.info(f"highest= {highest:.2f}")

yvalues = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]


logger.info("yvalues = " + str(yvalues))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(yvalues)
median = statistics.median(yvalues)
mode = statistics.mode(yvalues)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(yvalues)
stdev = statistics.stdev(yvalues)
lowest = min(yvalues)
highest = max(yvalues)

# TODO: change to f-strings and display 2 decimal places (like we did above)
logger.info(f"var    = {var:.2f}")
logger.info(f"stdev  = {stdev:.2f}")
logger.info(f"lowest = {lowest:.2f}")
logger.info(f"highest= {highest:.2f}")