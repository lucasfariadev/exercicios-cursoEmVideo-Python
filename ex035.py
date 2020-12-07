print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('primeiro segmento? '))
r2 = float(input('segundo seguimento? '))
r3 = float(input('terceiro seguimento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os seguimentos acima NÃO PODEM formar triângulo')
