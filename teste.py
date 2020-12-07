def voto(nascimento):
    from datetime import date
    # global atual
    atual = date.today().year - ano
    if atual < 18:
        return f'Com {atual} anos de idade: VOTO NEGADO'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))