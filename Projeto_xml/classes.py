

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
        self.tree = ET.parse(source)
        self.root = self.tree.getroot()
    
    def duplicados(self):
        lista = list()
        self.id_duplicado = list()
        for child in self.root:
            if child.attrib['id'] in lista:
                self.id_duplicado.append(int(child.attrib['id']))
            else:
                lista.append(child.attrib['id'])
    
    def alterar_duplicado(self):
        print(len(self.id_duplicado))
        while len(self.id_duplicado) >= 1:
            for child in self.root:
                #if child.attrib['id'] in self.id_duplicado:
                 while int(child.attrib['id']) in self.id_duplicado:
                    new_id = input('Digite um novo id: ')
                    #indice = self.id_duplicado.index(child.attrib['id'])
                    self.id_duplicado.remove(int(child.attrib['id']))
                    child.attrib['id'] = new_id
                    self.duplicados()
                    
        else:
            print('Não é elementos na lista')
        for child in self.root:
            print('id livro: ', child.attrib['id'])

    def excluir_duplicados(self):
        pass        
        print(self.id_duplicado)

           



teste = tree_xml()
teste.read_xml("Projeto_xml\pedidos2.xml")
teste.duplicados()
teste.alterar_duplicado()
