# programa para conferir a HbA1c com base na média da glicose informada pelo usuário
# a fórmula para determinar a Hba1c é = (MPG + 46,7) / 28,7
# A1C corresponde a média da glicose informada pelo usuário
glicose=int (input ('diga a média da sua glicose:'))
media=glicose + 46.7
divisao= 28.7
resultado = media/divisao
print ("sua hba1c é {:.1f}" .format (resultado))
if resultado <= 5.6:
    print ("sua glicose encontra-se dentro da normalidade")
else:
    print ("você precisa controlar sua glicose")