#2. Duplicação de Elementos
#Um XML pode conter IDs ou chaves duplicadas onde deveriam ser únicas.
#Projeto: Criar um script que detecte elementos duplicados com base em um atributo específico.
import random as rd
import xml.etree.ElementTree as ET


class tree_xml:
    def __init__(self):
        self.lista = list()
        pass

    def read_xml(self, source):
        self.source = source
        self.tree = ET.parse(self.source)
        self.root = self.tree.getroot()
    
    def duplicados(self):
        self.lista = list()
        self.id_duplicado = list()
        for child in self.root:
            if int(child.attrib['id']) in self.lista:
                self.id_duplicado.append(int(child.attrib['id']))
            else:
                self.lista.append(int(child.attrib['id'])) #estava recendo string, agr passa a receber inteiro
        return self.id_duplicado
    
    def alterar_duplicado(self):
        if len(self.lista) == 0:
            self.duplicados() 
         
        while len(self.id_duplicado) >= 1:
            for child in self.root:
                #if child.attrib['id'] in self.id_duplicado:
                while int(child.attrib['id']) in self.id_duplicado:
                    #new_id = int(input('Digite um novo id: ')) #ESTOU RECEBENDO UM STRING 
                    n = max(self.lista)+1
                    new_id = rd.randint(1, n)
                    if new_id not in self.lista:
                        self.id_duplicado.remove(int(child.attrib['id']))
                        child.attrib['id'] = str(new_id)
                        print(f'Id {new_id} inserido com sucesso')
                        #Declarei o parametro source do metodo read_xml como uma variavel de classe para ultilizar novamente no upload do arquivo xml
                        self.tree.write(self.source, encoding='utf-8', xml_declaration=True)
                        
                        self.duplicados()
                        #print("Esse Id, ja existe, escolha outro!")
                    #indice = self.id_duplicado.index(child.attrib['id'])
                        
                    
        else:
            print('Não existem ID iguais')
        for child in self.root:
            print('id livro: ', child.attrib['id'])
        
    def excluir_duplicados(self):
        for c in self.root:
            c.attrib['id'] = '1'
            self.tree.write(self.source, encoding='utf-8', xml_declaration=True)
        pass        
        



teste = tree_xml()
teste.read_xml("Projeto_xml\pedidos2.xml")
teste.alterar_duplicado()

