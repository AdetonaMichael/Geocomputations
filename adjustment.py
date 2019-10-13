#importation of class math to be used in the program
import math
#Welcome messages and instructions
def welcome():
    print("")
    print("Welcome to Surveying computation")
    print("")
    print("1. Bowditch Adjustment")
    print("2. Transit Adjustment")
    print("3. Adjustment By least square")
    print("4. Convert form GCS to UTM")
    print("5. Convert co-ordinate to bearing and distance")
    print("")
    
# this function sums up measured distances
def distances():
  no_dist = int(input("Enter no of distances to compute"))
  result = 0
  distance = 0
  for i in range(no_dist):
      distance = float(input("Enter Distance: "))
      result = result + distance
  return result

# this function sums up measured angles 
# def angles():
#     no_angles = int(input("Enter no of angles to compute"))
#     result = 0
#     angle = 0
#     for i in range(no_angles):
#         angle = float(input("Enter Angle: "))
#         result = result + angle
#     return result

#-----------------the following code converts decimal degree to deg,min and sec---------------------#
def dd2dms(longitude, latitude):

    # math.modf() splits whole number and decimal into tuple
    # eg 53.3478 becomes (0.3478, 53)
    split_degx = math.modf(longitude)
    
    # the whole number [index 1] is the degrees
    degrees_x = int(split_degx[1])

    # multiply the decimal part by 60: 0.3478 * 60 = 20.868
    # split the whole number part of the total as the minutes: 20
    # abs() absoulte value - no negative
    minutes_x = abs(int(math.modf(split_degx[0] * 60)[1]))

    # multiply the decimal part of the split above by 60 to get the seconds
    # 0.868 x 60 = 52.08, round excess decimal places to 2 places
    # abs() absoulte value - no negative
    seconds_x = abs(round(math.modf(split_degx[0] * 60)[0] * 60,2))

    # repeat for latitude
    split_degy = math.modf(latitude)
    degrees_y = int(split_degy[1])
    minutes_y = abs(int(math.modf(split_degy[0] * 60)[1]))
    seconds_y = abs(round(math.modf(split_degy[0] * 60)[0] * 60,2))

    # account for E/W & N/S
    if degrees_x < 0:
        EorW = "W"
    else:
        EorW = "E"

    if degrees_y < 0:
        NorS = "S"
    else:
        NorS = "N"

    # abs() remove negative from degrees, was only needed for if-else above
    print "\t" + str(abs(degrees_x)) + u"\u00b0 " + str(minutes_x) + "' " + str(seconds_x) + "\" " + EorW
    print "\t" + str(abs(degrees_y)) + u"\u00b0 " + str(minutes_y) + "' " + str(seconds_y) + "\" " + NorS

# some coords of cities
# coords = [["Dublin", -6.2597, 53.3478],["Paris", 2.3508, 48.8567],["Sydney", 151.2094, -33.8650]]

# # test dd2dms() 
# for city,x,y in coords:
#     print city + ":"
#     dd2dms(x, y)

#-----------------the following code converts decimal degree to deg,min and sec---------------------#
#this document consist of method, object and classes for performing different types of surveying computation
def main():
    welcome()
    print("The Co-ordinate of Nigeria is: ", dd2dms(-6.2597, 53.3478)

  
#the following line tells if the computer should execute the line of code as a program and not as a library
if __name__=="__main__":
    main()

    