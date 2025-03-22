#Desafio: Analisador de Pedidos em XML
#Você tem um arquivo XML que contém informações sobre pedidos de uma loja. Seu objetivo é:
#
#Ler e processar os dados do arquivo XML.
#Calcular o valor total dos pedidos de cada cliente.
#Gerar um resumo exibindo os clientes e seus totais de compras.

#primeiro obtenho a arvore(tree) do xml usando o ET.parse(função da biblioteca), apos isso obenho a raiz
# Usei procure tudo ( findall) find(procure) all(tudo), para percorrer a raiz do xml

import xml.etree.ElementTree as ET

tree = ET.parse('desafioPython\desafio_xml\pedidos_xml\pedidos_2.xml')
root = tree.getroot()

clientes = list()
valores = list()

for usuario in root.findall('pedido'):
    cliente = str(usuario.findtext("cliente"))
    valor = usuario.find("valor").text#posso pedir que procure dentro chave um text, dessa forma o valor ja vem convertido
    valor = float(valor)
    if cliente in clientes:
       indice = clientes.index(cliente)
       valores[indice] += valor
    else:
        clientes.append(cliente)
        valores.append(valor)


for char, valor in zip(clientes, valores):
    print(f'Cliente: {char}, valor total: {valor}')

    