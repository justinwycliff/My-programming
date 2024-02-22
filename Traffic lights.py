#Traffic lights

traffic_light = input("Enter traffic color :")

if (traffic_light == "red"):
    print("stop!")

elif(traffic_light == "orange"):
    print("slow_down and prepare to go")

elif(traffic_light == "green") :
    print("go!")

else:
    print("color invalid")
