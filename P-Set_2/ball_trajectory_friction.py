S_list = []
dt = 0.01
s = [0,0,0]
S_list.append(s)
v = [10,5,15]
g = 9.78
t = 0
m = 0.43
k = 0.5*1.225*0.47*0.038

t = t+dt
s_new = [0,0,0]
v[0]=v[0]+dt*-k*v[0]/m
v[1]=v[1]+dt*-k*v[1]/m
v[2]=v[2]+dt*-g+dt*-k*v[2]/m

print(S_list)
s_new[0]=s[0]+dt*v[0]
s_new[1]=s[1]+dt*v[1]
s_new[2]=s[2]+dt*v[2]
S_list.append(s_new)
print(S_list)

while s_new[2] > 0:
    t = t+dt
    v[0]=v[0]+dt*-k*v[0]/m
    v[1]=v[1]+dt*-k*v[1]/m
    v[2]=v[2]+dt*-g+dt*-k*v[2]/m
    s_new[0]=S_list[-1][0]+dt*v[0]
    s_new[1]=S_list[-1][1]+dt*v[1]
    s_new[2]=S_list[-1][2]+dt*v[2]
    S_list.append(s_new)
    #print(S_list[-1][2]) # z-position
    print((S_list[-1][1]**2+S_list[-1][1]**2)**0.5) # distance from start
    
