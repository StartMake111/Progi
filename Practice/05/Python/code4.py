print ('Vvedi skorost, vremya, x')
x0, v0, t = map(float, input().split())
g = 9.8
xt = x0+ v0*t - ((g*t*t)/2)
print (abs(xt-x0))

