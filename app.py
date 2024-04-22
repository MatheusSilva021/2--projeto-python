from models.restaurant import Restaurant
from models.cardapio.bebida import bebida
from models.cardapio.prato import prato

restaurante1 = Restaurant('Madero','Hambúrguer')
bebida1 = bebida('suco de laranja', 10.00, 'jarra')
prato1 = prato('macarrão', 15.00, 'macarrão ao alho e óleo')
restaurante1.adicionar_itens_cardapio(bebida1)
restaurante1.adicionar_itens_cardapio(prato1)
prato1.aplicar_desconto()


def main():
    restaurante1.exibir_cardapio

if __name__ == "__main__":
    main()