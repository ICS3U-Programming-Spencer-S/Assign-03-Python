#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct. 19, 2022
# This is a program that,
# Takes three values and calculates the average
# While rounding, having a try catch, and looping.


def main():
    # Spacer
    print("")

    # Info to user
    print("Hello, this is a program that find the average of three numbers")

    # Spacer
    print("")

    # Taking three user inputs
    # These are the numbers we find the average for
    numb1_as_string = input("Enter value A: ")

    try:
        numb1_as_float = float(numb1_as_string)

    except:
        print("Invalid input for value A")

    else:
        if numb1_as_float >= 0 and numb1_as_float < 100:
            print("Valid input for Value A")

            numb2_as_string = input("Enter value B: ")

            try:
                numb2_as_float = float(numb2_as_string)

            except:
                print("Invalid input for value B")

            else:
                if numb2_as_float >= 0 and numb2_as_float <= 100:
                    print("Valid input for Value B")

                    numb3_as_string = input("Enter value C: ")

                    try:
                        numb3_as_float = float(numb3_as_string)

                    except:
                        print("Invalid input for value C")

                    else:
                        if numb3_as_float >= 0 and numb3_as_float <= 100:
                            print("Valid input for Value C")
                            aver_num = (
                                numb1_as_float + numb2_as_float + numb3_as_float
                            ) / float(3)
                            print(
                                f"Your numbers: {numb1_as_float}, {numb2_as_float}, and {numb3_as_float}"
                            )
                            print("Have the average of {0:.2f}".format(aver_num))

                        else:
                            wait = input(
                                "Invalid input for C, press any key to retry: "
                            )
                            main()

                else:
                    wait = input("Invalid input for B, press any key to retry: ")
                    main()

        else:
            wait = input("Invalid input for A, press any key to retry: ")
            main()
            aver_num = (numb1_as_float + numb2_as_float + numb3_as_float) / 3


if "__main__" == __name__:
    main()
    answer = input("Would you like to restart? (y/n): ")
    while answer == "y":
        main()
        answer = input("Would you like to restart? (y/n): ")
