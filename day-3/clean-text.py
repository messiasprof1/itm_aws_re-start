preproinsulin = 'malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn'

# contagem dos caracteres
print('---- CONTAGEM DE CARACTERES ------')
print('Quantidade de caracteres: {}'.format(len(preproinsulin)))

# extrair dados especificos
lsInsulin = preproinsulin[0:24]
bInsulin = preproinsulin[25:54]
aInsulin = preproinsulin[55:89]
cInsulin = preproinsulin[90:110]

print('lsInsulin: ', lsInsulin)
print('bInsulin: ', bInsulin)
print('aInsulin: ', aInsulin)
print('cInsulin: ', cInsulin)

# criar os arquivos
# lista
names = ["lsInsulin", "bInsulin", "aInsulin", "cInsulin"]

# estrutura de repeticao
# para ler arquivos: flag 'r'
# para escrever arquivos: flag 'w'
for insulin in names:
    fw = open('day-3/' + str(insulin).upper() + '-seq-clean.txt', 'w')
    fw.write(globals()[insulin])
    fw.close()
