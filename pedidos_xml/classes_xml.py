#Desafio: Analisador de Pedidos em XML
#Você tem um arquivo XML que contém informações sobre pedidos de uma loja. Seu objetivo é:
#
#Ler e processar os dados do arquivo XML.
#Calcular o valor total dos pedidos de cada cliente.
#Gerar um resumo exibindo os clientes e seus totais de compras.
import xml.etree.ElementTree as ET

class TratarXml:
    def __init__(self):
        self.clientes = list()
        self.valores = list()

    def lerXml(self, caminho_Xml):
        self.tree = ET.parse(caminho_Xml)
        self.root = self.tree.getroot()
    
    def CalcularValorTotal (self):
        
        for pedido in self.root.findall('pedido'):
            self.nome = pedido.findtext('cliente')
            self.valor = pedido.findtext('valor')
            self.valor = float(self.valor)

            if self.nome in self.clientes:
                self.indice = self.clientes.index(self.nome)
                self.valores[self.indice] += self.valor
            else:
                self.clientes.append(self.nome)
                self.valores.append(self.valor)

    def mosrtrarValorTotal(self):
        for x in self.clientes:
            print(f'Nome: {x}, valor total: {self.valores[self.clientes.index(x)]}')



