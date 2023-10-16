import matplotlib.pyplot as plt
from randomwalk import RandomWalk
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
#图像的长宽比
    point_numbers=range(rw.num_points)
    # 初始化
    ax.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)

    ax.scatter(0,0,c='green',edgecolor='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)
#终点的时候颜色、
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #xy轴的可见性
    ax.set_aspect('equal')
    # 刻度的间距是相等的
    plt.show()
    keep_running=input("make another walk?(y/n)")
    if keep_running=="n":
        break




