def ler_imagem_ppm(caminho):
    with open(caminho, 'r') as f:
        linhas = f.readlines()

    # Ignora comentários e vazios
    linhas = [linha.strip() for linha in linhas if linha.strip() and not linha.startswith('#')]

    if linhas[0] != 'P3':
        raise ValueError('Formato não suportado. Use P3 (texto).')

    largura, altura = map(int, linhas[1].split())
    max_val = int(linhas[2])

    dados = list(map(int, ' '.join(linhas[3:]).split()))
    pixels = [(dados[i], dados[i+1], dados[i+2]) for i in range(0, len(dados), 3)]

    return largura, altura, max_val, pixels

def converter_para_cinza(pixels):
    cinza_pixels = []
    for r, g, b in pixels:
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        cinza_pixels.append((gray, gray, gray))
    return cinza_pixels

def binarizar_imagem(pixels_cinza, limiar=128):
    binarios = []
    for r, g, b in pixels_cinza:
        bin_value = 255 if r >= limiar else 0
        binarios.append((bin_value, bin_value, bin_value))
    return binarios

def salvar_imagem_ppm(caminho, largura, altura, max_val, pixels):
    with open(caminho, 'w') as f:
        f.write('P3\n')
        f.write(f'{largura} {altura}\n')
        f.write(f'{max_val}\n')
        for r, g, b in pixels:
            f.write(f'{r} {g} {b}\n')

def executar_transformacoes(caminho_entrada):
    largura, altura, max_val, pixels = ler_imagem_ppm(caminho_entrada)

    # Conversão para tons de cinza
    pixels_cinza = converter_para_cinza(pixels)
    salvar_imagem_ppm('imagem_cinza.ppm', largura, altura, max_val, pixels_cinza)

    # Binarização com limiar padrão 128
    pixels_binarios = binarizar_imagem(pixels_cinza, limiar=128)
    salvar_imagem_ppm('imagem_binaria.ppm', largura, altura, max_val, pixels_binarios)

    print("Imagens salvas: imagem_cinza.ppm e imagem_binaria.ppm")

# Exemplo de uso:
# executar_transformacoes('imagem.ppm')
