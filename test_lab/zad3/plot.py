import matplotlib

x_val = []
y_val = []
with open("gen.txt", 'r') as f:
    for line in f:
        ch = line.split(' ')
        x_val.append(ch[0])
        y_val.expand(ch[1:])
matplotlib.plot(x_val, y_val)
plt.show()
