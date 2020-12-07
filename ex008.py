n =float(input('Quantos metros?'))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
c = n * 100
mm = n *1000

print('{}m equivale:'.format(n))
print(' {}km\n {}hm\n {}dam \n {}dm\n {}cm\n {}mm\n'.format(km, hm, dam, dm, c, mm))
