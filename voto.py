def verificar_voto(idade):


    if idade < 16:
        return "Negado"
    elif 16 <= idade <= 17 or idade > 65:
        return "Facultativo"
    else:
        return "Obrigatório"
    
idade_usuario = int(input("Digite sua idade: "))
tipo_voto = verificar_voto(idade_usuario) 
print(f"Para a idade {idade_usuario}, o voto é: {tipo_voto}")


