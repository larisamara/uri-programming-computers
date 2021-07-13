qtd_frango, qtd_carne, qtd_macarrão= input().split()
pedido_frango, pedido_carne, pedido_macarrão = input().split()
falta_frango = 0
falta_carne = 0
falta_macarrão = 0
if(int(pedido_frango) > int(qtd_frango)):
    falta_frango= int(pedido_frango) - int(qtd_frango)
if(int(pedido_carne) > int(qtd_carne)):
    falta_carne= int(pedido_carne) - int(qtd_carne)
if(int(pedido_macarrão) > int(qtd_macarrão)):
    falta_macarrão= int(pedido_macarrão) - int(qtd_macarrão)
falta_total = falta_frango + falta_carne + falta_macarrão    
print(falta_total)