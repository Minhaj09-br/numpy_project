import numpy as np
all_marks = []
rolls=[]
student=int(input("how many student: "))
#input fist roll=1st row all markes(ban,eng,ict)
# input seccond roll=snd row all (ban,eng,ict)
for i in range(student):
    roll=int(input("enter  roll: "))
    rolls.append(roll)   
# student subject
    ban = int(input(f"Bangla{roll}: "))
    eng = int(input(f"English{roll}: "))
    ict = int(input(f"ICT{roll}: "))
    phy=int(input(f"phy{roll}: "))
    che=int(input(f"che{roll}: "))
    bio=int(input(f"bio{roll}: "))
    h_math=int(input(f"h.math{roll}: "))

    all_marks.append([ban, eng, ict, phy, che, bio, h_math])
# markes analiser
arr = np.array(all_marks)
roll_arr=np.array(rolls)
print(arr)
total=np.sum(arr,axis=1)
print(f"total markes of every student:{total}")
average=np.mean(arr,axis=(1))
print(f"avrage markes of every students{average}")
higest=np.max(total)
print(f"the higest markes:{higest}" )
lowest=np.min(total)
print(f"the lowest markes{lowest}")
great=np.where(average>=55,"pass","fail")
print(great)
# mark set
for i in range (student):
    print(f"Roll:{rolls[i]}|Total:{total[i]}|average:{average[i]:.2f}:sf|Result:{great[i]}")


