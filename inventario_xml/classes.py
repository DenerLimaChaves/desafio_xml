import xml.etree.ElementTree as ET


class manipulacaoXml:
    def __init__(self):
        pass
    def readXml(self, pathxml):
        tree = ET.parse(pathxml)
        self.root = tree.getroot()

    def itensInventary (self):
        #print(self.root[0])
        totalProdutoEstoque = int()
        totalValorInventario = float()
        for child in self.root:
            #print(child.findtext('nome'), child.findtext('quantidade'),  child.findtext('preco'))
            totalProdutoEstoque += int(child.findtext('quantidade'))
            totalValorInventario += float(child.findtext('preco')) * float(child.findtext('quantidade'))
            #print(child.findtext("preco"))
        print(f'Total de produtos em estoque: {totalProdutoEstoque} \nValor total de inventario: {totalValorInventario}')
        
    
    def maxEndMin(self):
        valores = list()
        produtoMaisCaro = dict()
        produtobarato = dict()
        for child in self.root:
            valores.append(float(child.findtext('preco')))
            if max(valores) == float(child.findtext('preco')):
                produtoMaisCaro['nome'] = child.findtext('nome')
                produtoMaisCaro['preco'] = child.findtext('preco')
            if min(valores) == float(child.findtext('preco')):
                produtobarato['nome'] = child.findtext('nome')
                produtobarato['preco'] = child.findtext('preco')
        produtoMaisCaro = f'Produto mais caro: {produtoMaisCaro["nome"]}, valor ({produtoMaisCaro["preco"]})'
        produtobarato = f'Produto mais barato: {produtobarato["nome"]}, valor ({produtobarato["preco"]})'
        return f'{produtoMaisCaro} \n{produtobarato}'
    
    def report(self):
        #Gerar um relatório detalhado com os produtos, quantidade em estoque, preço unitário e valor total por produto.
        itens = dict()
        produtos = list()
        for son in self.root:
            x = 0
            decoration = f"{'-'*15}"
            itens['nome'] = son.findtext('nome')
            itens['quantidade'] = int(son.findtext('quantidade'))
            itens['preco'] = float(son.findtext('preco'))
            produtos.append(itens)
            decoration
            print(decoration)
            print(f"Nome: {produtos[x]['nome']}, Quantidade: {produtos[x]['quantidade']}, Preco: {produtos[x]['preco']}")

        return 

    def productList(self):
        for child in self.root:
            produto = str()
            quantidade = int()
            preco = float()
            total = float()

            produto = child.findtext('nome')
            quantidade = int(child.findtext('quantidade'))
            preco = float(child.findtext('preco'))
            total = quantidade*preco
            print(f"Produto, {produto} - quantidade ({quantidade}) - preco ({preco}) - total ({total}) ")


