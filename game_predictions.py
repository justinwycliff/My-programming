#initial points
man_cit_points= 88
arsenal_points= 86

#asking the user for match 
man_city_result=input("Enter Manchester City's result (win/draw/lose): ").lower()
arsenal_result =input("Enter Arsenal's resultn(win/draw/lose): ").lower()

# calculating points based on results

if man_city_result == "win":
    man_city_points= 88 + 3

elif man_city_result == "draw":
    man_city_points= 88 + 1

elif man_city_result =="lose":
    man_city_points= 88

else:
    print("inavalid input for Manchester City's results." )


if arsenal_result== "win":
    arsenal_points=86 +3

elif arsenal_result== "draw":
    arsenal_points= 86 + 1

elif arsenal_result == "lose":
    arsenal_points=86

else:
    print("invalid input for arsenals's result.")

#champions
if man_city_points > arsenal_points:
    print("Manchester City will be crowned champions.")

elif arsenal_points > man_cit_points:
    print("Arsenal will be crowned champions.")

else:
    print("Manchester City will be crowned champions") #assuming goaldifference favors city



