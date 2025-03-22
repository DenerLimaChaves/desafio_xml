

#1. XML Malformado
#Tags não fechadas corretamente - 
#
#Atributos sem aspas
#
#Caracteres especiais não escapados (&, <, > etc.)
#
#Projeto: Criar um validador de XML que identifique erros estruturais e sugira correções.
#
#2. Duplicação de Elementos
#Um XML pode conter IDs ou chaves duplicadas onde deveriam ser únicas.

import xml.etree.ElementTree as ET


class tree_xml:
    def __init__(self):
        pass

    def read_xml(self, source):
        tree = ET.parse(source)
        self.root = tree.getroot()
    
    def duplicados(self):
        lista = list()
        self.id_duplicado = list()
        for child in self.root:
            if child.attrib['id'] in lista:
                self.id_duplicado.append(child.attrib['id'])
            else:
                lista.append(child.attrib['id'])
    
    def alterar_duplicado(self):
        
    
    def excluir_duplicados(self):
        pass        
        print(self.id_duplicado)

           



teste = tree_xml()
teste.read_xml("pedidos2.xml")
teste.duplicados()
