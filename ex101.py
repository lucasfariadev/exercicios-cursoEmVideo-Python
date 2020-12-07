def voto(ano):
    from datetime import date
    atual = date.today().year - ano
    if atual < 16:
        return f'Com {atual} anos: Não Vota'
    elif 16 <= atual < 18 or atual > 65:
        return f'Com {atual} anos: Voto Opicional'
    else:
        return f'Com {atual} anos: Voto Obrigatório'

print(voto(int(input('Em que ano você nasceu? '))))
