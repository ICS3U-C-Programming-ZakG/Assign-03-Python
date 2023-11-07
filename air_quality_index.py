#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 4, 2023
# This program gets a number from the user and tells them what air quality it is.


def main():
    # introduce program to user
    print(
        "This program gets a number from the user and will tell them what air quality that is."
    )

    # get user input
    air_quality_str = input("Please enter a number from 0-500: ")

    # try casting user input into an integer
    try:
        air_quality_int = int(air_quality_str)

        # check if user input is within the index range
        if (air_quality_int <= 500) and (air_quality_int >= 0):

            # check if input is between 0-50
            if air_quality_int <= 50:
                print(
                    "{} is a good air quality, it ranges between 0-50!\n".format(
                        air_quality_int
                    )
                )

            # check if input is between 51-100
            elif (air_quality_int >= 51) and (air_quality_int <= 100):
                print(
                    "{} is a moderate air quality, it ranges between 51-100.\n".format(
                        air_quality_int
                    )
                )

            # check if input is between 101-150
            elif (air_quality_int >= 101) and (air_quality_int <= 150):
                print(
                    "{} is an unhealthy for sensitive groups air quality, it ranges between 101-150.\n".format(
                        air_quality_int
                    )
                )

            # check if input is between 151-200
            elif (air_quality_int >= 151) and (air_quality_int <= 200):
                print(
                    "{} is an unhealthy air quality, it ranges between 151-200.\n".format(
                        air_quality_int
                    )
                )

            # check if input is between 201-300
            elif (air_quality_int >= 201) and (air_quality_int <= 300):
                print(
                    "{} is a very unhealthy air quality, it ranges between 201-300.\n".format(
                        air_quality_int
                    )
                )

            # else if all false tell user it is hazardous
            else:
                print(
                    "{} is a hazardous air quality, it ranges between 301-500.\n".format(
                        air_quality_int
                    )
                )

        # tell user their number is not within the index
        else:
            print(
                "{} is not a number within the range of the index.\n".format(
                    air_quality_int
                )
            )

    # catch invalid inputs from user
    except Exception:
        print("{} is not a valid number.\n".format(air_quality_str))

if __name__ == "__main__":
    main()
