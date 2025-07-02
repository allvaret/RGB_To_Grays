def ler_imagem_ppm(caminho):
    with open(caminho, 'r') as f:
        linhas = f.readlines()

    # Ignora comentários e cabeçalho
    linhas = [linha for linha in linhas if not linha.startswith('#')]

    tipo = linhas[0].strip()
    if tipo != 'P3':
        raise ValueError('Formato não suportado. Use P3 (texto).')

    # Extrai as dimensões da imagem (largura e altura) e o valor máximo da cor (normalmente 255).
    largura, altura = map(int, linhas[1].split())
    max_val = int(linhas[2])

    # Junta todas as linhas restantes (que contêm os valores RGB), separa os números e transforma em inteiros.
    dados = list(map(int, ' '.join(linhas[3:]).split()))
    pixels = []

  # Agrupa os números em trios (R, G, B) e armazena como tuplas numa lista pixels.
    for i in range(0, len(dados), 3):
        r = dados[i]
        g = dados[i+1]
        b = dados[i+2]
        pixels.append((r, g, b))

    return largura, altura, max_val, pixels

def converter_para_cinza(pixels):
    cinza_pixels = []
    for r, g, b in pixels:
        # Fórmula perceptual
        gray = int(0.299*r + 0.587*g + 0.114*b)
        cinza_pixels.append((gray, gray, gray))
    return cinza_pixels


def binarizar_imagem(pixels_cinza, limiar=128):
    imagem_binaria = []
    for r, g, b in pixels_cinza:
        # como R = G = B em imagens em tons de cinza, podemos pegar qualquer um
        valor = r
        binario = 255 if valor >= limiar else 0
        imagem_binaria.append((binario, binario, binario))  # preto ou branco
    return imagem_binaria

def salvar_imagem_ppm(caminho, largura, altura, max_val, pixels):
    with open(caminho, 'w') as f:
        f.write('P3\n')
        f.write(f'{largura} {altura}\n')
        f.write(f'{max_val}\n')
        for r, g, b in pixels:
            f.write(f'{r} {g} {b}\n')

# Caminho da imagem original
entrada = 'imagem.ppm'
saida = 'imagem_cinza.ppm'

largura, altura, max_val, pixels = ler_imagem_ppm(entrada)
pixels_cinza = converter_para_cinza(pixels)
salvar_imagem_ppm(saida, largura, altura, max_val, pixels_cinza)

pixels_binarios = binarizar_imagem(pixels_cinza, limiar=128)
salvar_imagem_ppm(saida_binaria, largura, altura, max_val, pixels_binarios)

print("Imagem convertida para tons de cinza com sucesso.")
