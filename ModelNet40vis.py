from matplotlib import pyplot as plt
path = "/home/wangwei83/point-transformer-old/data/modelnet40_normal_resampled/airplane/airplane_0001.txt"
data = open(path,"r")
x,y,z = [],[],[]

for line in data:
    tx,ty,tz,nx,ny,nz=line.split(",")
    x.append(eval(tx))
    y.append(eval(ty))
    z.append(eval(tz))

x=x[:1024]
y=y[:1024]
z=z[:1024]

fig=plt.figure()
ax=plt.axes(projection="3d")
ax.scatter3D(x,y,z,c="b",s=10,alpha=0.8,marker=".")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.pause(50)