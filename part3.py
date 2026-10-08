def ShouldIEatDroppedFood():

    sticky = input("Was it sticky? (yes/no): ")

    if sticky == "yes":

        raw_steak = input("Is it a raw steak? (yes/no): ")

        if raw_steak == "yes":
            puma = input("Are you a puma? (yes/no): ")

            if puma == "yes":
                print("EAT IT")
            else:
                print("DON'T EAT IT")

        else:
            cat = input("Did the cat lick it? (yes/no): ")

            if cat == "yes":
                healthy = input("Is your cat healthy? (yes/no): ")

                if healthy == "yes":
                    print("EAT IT")
                else:
                    print("YOUR CALL")
            else:
                print("DON'T EAT IT")

    else:
        seen = input("Did anyone see you? (yes/no): ")

        if seen == "no":
            print("EAT IT")

        else:
            boss = input("Was it a boss, lover, or parent? (yes/no): ")

            if boss == "no":
                print("EAT IT")

            else:
                expensive = input("Was it expensive? (yes/no): ")

                if expensive == "yes":
                    cut = input("Can you cut off the part that touched the floor? (yes/no): ")

                    if cut == "yes":
                        print("EAT IT")
                    else:
                        print("YOUR CALL")

                else:
                    bacon = input("Is it bacon? (yes/no): ")

                    if bacon == "yes":
                        print("EAT IT")
                    else:
                        print("DON'T EAT IT")


ShouldIEatDroppedFood()