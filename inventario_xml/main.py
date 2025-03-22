from classes import manipulacaoXml as Mxml

inventario = Mxml()

inventario.readXml('inventario_xml\inventario_3.xml')
print('-'*85)
inventario.productList()
print('-'*85)