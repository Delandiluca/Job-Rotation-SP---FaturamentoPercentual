
def calcularMedia(faturamentos: list):
    for i in range(len(faturamentos)):
        (_, valor) = faturamentos[i]
        soma += valor
    mediaTotal = soma / len(faturamentos)
    return mediaTotal

def calcularPercentual(faturamentos: list, media: int):
    for i in range(len(faturamentos)):
        (estado, valor) = faturamentos[i]
        percentual = abs((valor * 100) / media)
        print(" {:d}".format(estado, percentual))    



def cadastroFaturamentos():
    faturamentos = [("SP", 67.836,43),
             ("RJ", 36.678,66),
             ("MG", 29.229,88),
             ("ES", 27.165,48),
             ("OUTROS", 19.849,53)]
    media = calcularMedia(faturamentos)
    calcularPercentual(faturamentos, media)

if __name__ == "__main__":
    cadastroFaturamentos()