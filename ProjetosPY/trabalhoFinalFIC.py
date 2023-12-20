cliente = input('Digite seu nome: ')
quantidade = int(input('Quantos aparelhos serão instalados em sua residencia?'))
quant = 1
n = 1  
for i in range(quantidade):
    #cliente = input('Digite seu nome: ')
    marca = input(f'Qual o modelo do seu {n}° aparelho de ar condicionado: ')
    n = n + quant
    BTU = int(input('Quantidade em BTU do aparelho citado? 8000 a 45000mil BTU'))
    if BTU >=8000 and BTU <=12000:
        modelo1 = int('110')
        valor = int('600')
    elif BTU >=15000 and BTU <=18000:
        modelo1 = int('180')
        valor = int('800')
    elif BTU >=19000 and BTU <=45000:
        modelo1 = int('240')
        valor = int('1200')
    else:
        print('opção invalida!!')   
    metros = input('O condensadora sera instalada atras da evaporadora? [S][N]').upper()
    if metros == 'S':
        print(f'Ok... nenhum acrescimo no valor, teremos uma instalação simples! na maquina {marca} ')
        print(f'Seu ar condicionado do modelo: {marca}, será cobrado o valor de instalação o total \n de: {valor}Reais')
    elif metros == 'N':
        qMetros = float(input('A condensadora ficará a quantos metros de distancia da evaporadora?'))
        print(f'Seu ar condicionado do modelo: {marca}, será cobrado o valor de instalação o total \n de: {(qMetros * modelo1) + valor}Reais, levando em consideração que foi cobrado o valor de {valor} \n pela instalação e o total de: {modelo1} por metros adicionais do cobre')

    else:
        print('opção invalida')
    #O para uso do banco de dedos tire as aspas!
    '''import mysql.connector

    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password='',
        database='Orcamentos'
    )
    mycursor = mydb.cursor()

    sql = 'INSERT INTO clientes (cliente, marca, BTU, valor)VALUES (%s,%s,%s,%s)'
    val = (cliente, marca, BTU, valor)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,'record inserted')'''