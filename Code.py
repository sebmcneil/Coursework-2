

# Chodeos is a pedo


#Angular velocity (rad s-1)

Rw = [3.0, 6.5, 1.0]

#Wheel diameter (meters)

Wd = [0.15, 0.10, 0.30]


#Wheel radius (meters)

Wr = []
for x in Wd:
    Wr.append(x/2)
    
#Linear velocity (ms -1)

Lv = []
for value1, value2 in zip(Rw, Wr):
    Lv.append(value1 * value2)

#Defining the robots linear speed
Robot1_lv = Lv[0]
Robot2_lv = Lv[1]
Robot3_lv = Lv[2]

   
#Finding the distance away from the original point for all the robots
print("For Robot 1:")
def D_Caluclator(Robot1_lv):
    time = 0
    for i in range (0, 601):
        time += 1
        if time == 120 :
            print("In 2 minutes the Robot travelled", Robot1_lv*time, "meters")
            continue
        if time == 240 :
            print("In 4 minutes the Robot travelled", Robot1_lv*time, "meters")
            continue
        if time == 360 :
            print("In 6 minutes the Robot travelled", Robot1_lv*time, "meters")
            continue
        if time == 480 :
            print("In 8 minutes the Robot travelled", Robot1_lv*time, "meters")
            continue
        if time == 600 :
            print("In 10 minutes the Robot travelled", Robot1_lv*time, 
                  "meters")
            return Robot1_lv
       
D_Caluclator(Robot1_lv)
print("For Robot 2:")
D_Caluclator(Robot2_lv)
print("For Robot 3:") 
D_Caluclator(Robot3_lv)

#Distance after 10 minutes
Robot1_d = Robot1_lv * 600
Robot2_d = Robot2_lv * 600
Robot3_d = Robot3_lv * 600


#Finding the robot that travlled the largest distance
if Robot1_d > Robot2_d and Robot1_d > Robot3_d:
    L_d_t = "Robot 1"
elif Robot2_d > Robot1_d and Robot2_d > Robot3_d:
    L_d_t = "Robot 2"
elif Robot3_d > Robot1_d and Robot3_d > Robot2_d:
    L_d_t = "Robot 3"

print("The Robot that travelled the largest distance was", L_d_t)

#Finding the robot that travlled the smallest distance
if Robot1_d < Robot2_d and Robot1_d < Robot3_d:
    S_d_t = "Robot 1"
elif Robot2_d < Robot1_d and Robot2_d < Robot3_d:
    S_d_t = "Robot 2"
elif Robot3_d < Robot1_d and Robot3_d < Robot2_d:
    S_d_t = "Robot 3"

print("The Robot that travelled the smallest distance was", S_d_t)

#Working out the largest distance made by a robot
if L_d_t == "Robot 1":
    Largest_distance = float(Robot1_d)
if L_d_t == "Robot 2":
    Largest_distance = float(Robot2_d)
if L_d_t == "Robot 3":
    Largest_distance = float(Robot3_d)
    
#Working out the smallest distance made by a robot
if S_d_t == "Robot 1":
    Smallest_distance = float(Robot1_d)
if S_d_t == "Robot 2":
    Smallest_distance = float(Robot2_d)
if S_d_t == "Robot 3":
    Smallest_distance = float(Robot3_d)
    

#Finding the greatest difference in distance travelled
print("The greatest difference in distance travelled by any two "
      "of the three robots at the end of the 10 mins was", L_d_t, "-", S_d_t, 
      "which is equal to", Largest_distance - Smallest_distance, "meters")









