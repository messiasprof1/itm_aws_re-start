# ler arquivo e limpar os dados

# usar expressoes regulares
# importar o modulo
import re

# funcao de ler arquivos
with open('day-3/preproinsulin-seq.txt') as file:
    insulinFile = file.read()

print('---- DADO ORIGINAL -----')
print(insulinFile)

# funcao para limpeza do dado
def clean_text(string):
    # remover ORIGIN
    string = string.replace("ORIGIN", "")
    # remover numeros
    string = re.sub(r"\d+", "", string)
    # remover o 1
    #string = string.replace("1", "")
    # remover o 61
    #string = string.replace("61", "")
    # remover os espacos em branco
    string = re.sub(r"\s", "", string)
    # string = string.replace(" ", "")
    # remover o //
    string = string.replace("//", "")
    # remover quebra de linha
    #string = string.replace("\n", "")
    string = re.sub(r"\n", "", string)
    
    # retornar a string formatada
    return string

# dado limpo
cleanInsulin = clean_text(insulinFile)

# exibir os dados do arquivo limpo
print('------ DADO LIMPO ------')
print(cleanInsulin)