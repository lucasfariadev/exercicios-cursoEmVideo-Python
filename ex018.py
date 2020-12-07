from math import (sin, cos, tan, radians)
an = float(input('Digite o ângulo que você deseja: '))

sen = sin(radians(an))
co = cos(radians(an))
t = tan(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, t))