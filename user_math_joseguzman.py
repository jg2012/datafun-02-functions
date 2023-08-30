import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def get_area_of_a_livingroom(height, width):
    """
    Return area of a circle given the radius.

    @param radius: the radius of the circle
    @return: the area of the circle
    @raise Exception: if radius is not a number

    """

    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_area_of_a_livingroom({height, width})")

    try: 
        area = height * width
        logger.info(f"The circle area is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
def get_bmi(weight, height_b):

    logger.info(f"Calling get_bmi({weight, height_b})")
    
    try:
        bmi = (weight / (height_b ** 2)) * 703
        logger.info(f"The patients BMI is {bmi}")
        return bmi
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
def get_f_from_c(degrees_c):

    logger.info(f"Calling get_f_from_c({degrees_c})")

    try:
        degrees_f = (degrees_c * (9/5)) + 32 
        logger.info(f"The patients temp is {degrees_f}")
        return degrees_f
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None

def get_avg_weight(weight):

    logger.info(f"Calling get_avg_weight({weight})")

    try:
        avg_weight = math.fsum(weight)/ len(weight)
        logger.info(f"The patients average weight is {avg_weight}")
        return avg_weight
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None

if __name__ == "__main__":
 
    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(6,2) = {math.comb(6,2)}")
    logger.info(f"math.perm(6,2) = {math.perm(6,2)}")
    logger.info("")

    logger.info("TRY: Call get_area_of_a_livingroom() function with a different values.")
    get_area_of_a_livingroom(11, 7)
    get_area_of_a_livingroom(10, 8)
    get_area_of_a_livingroom(12, 6)
    logger.info("")

    ## Weight is in lbs and Height is in inches
    logger.info("TRY: Call get_bmi() with different values ")
    get_bmi(160, 67)
    logger.info("")

    ##Temp in Celcius 
    logger.info("TRY: Call get_f_from_c() with different values ")
    get_f_from_c(37)
    get_f_from_c(39)
    logger.info("")
    
    ##Weight in Lbs
    logger.info("TRY: Call get_avg_weight() function with a list of patients weight")
    weight_list = [160, 163, 162.5, 162, 161, 162]
    get_avg_weight(weight_list)
    logger.info("")
  




    
