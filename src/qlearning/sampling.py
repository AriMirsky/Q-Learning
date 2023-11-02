from src.state_pred.bike_sim import get_possible_states, optimize_input_res
import numpy as np
import math
import matplotlib.pyplot as plt

acceleration_power = 1  # m/s/s
braking_power = 1  # m/s/s
max_turning_rate = 30  # deg/s

#potential range of ACC-RES: 0.01 to 5.00
#potential range of TURNING-RES: 0.1 to 100.0

#plot in 2d matrix with arrays of acc and turning
#acc_res, turning_res, density of states that combo results in
acc_res = 0.01
turning_res = 0.1

acc_ult = 0.01
turning_ult = 0.1

high_res = [acc_ult, turning_ult]
#use very high res to get close to 100% of states to be used as the benchmark 
#for checking sampling density
total_samples = get_possible_states(curr, diff, high_res)

sample_size = len(temp)
total_samples_size = len(total_samples)

acc_res_size = 500
turn_res_size = 1000

res_shape = (acc_res_size, turn_res_size) #500 rows for acc_res, 1000 columns for turn_res

res = np.empty(res_shape)

pos_i = 0
pos_j = 0
for i in range(0.1, 100, 0.1):
  if i>0.1:
    pos_i+=1
  for j in range(0.01, 5, 0.01):
    if j>0.01:
      pos_j+=1
    res[pos_i, pos_j] = (i, j)

densities_shape = (acc_res_size*turn_res_size)
densities = np.empty(densities_shape)

densities_pos=0
for x in res:
  temp = (get_possible_states(curr, diff, x))
  sample_size = len(temp)
  sample_density = (sample_size/total_samples_size)*100
  densities[densities_pos] = sample-density
  densities_pos+=1

for i in densities:
  print(i)
#use diff values of res to check the output
#temp = get_possible_states(curr, diff, res)


#sample_density = (sample_size/total_samples_size)*100

# plt.figure()
# ax = plt.axes(projection="3d")
# ax.scatter(acc_res, turning_res, sample_density)

# plt.plot(acc_res, turning_res, sample_density)

# ax.set_xlabel("acceleration res")
# ax.set_ylabel("turning res")
# ax.set_zlabel("sampling density")
# ax.view_init(60,35)
# plt.show()
