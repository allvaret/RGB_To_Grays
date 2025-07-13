from PIL import Image #Utilizado apenas para abrir as imagens, e não para a conversão e redução de dimensionalidade direta

def imagem_para_matriz(img):
    largura, altura = img.size
    pixels = img.load()
    matriz = []

    for y in range(altura):
        linha = []
        for x in range(largura):
            linha.append(pixels[x, y])  # (R, G, B)
        matriz.append(linha)

    return matriz

def converter_cinza_manual(matriz, largura, altura):
    matriz_cinza = [[(0, 0, 0) for _ in range(largura)] for _ in range(altura)]
#Aplicada por meio de matrizes 5x5, como em convoluções ou filtros
    for y in range(0, altura, 5):
        for x in range(0, largura, 5):
            for dy in range(5):
                for dx in range(5):
                    if y+dy < altura and x+dx < largura:
                        r, g, b = matriz[y+dy][x+dx]
                        gray = int(0.299*r + 0.587*g + 0.114*b)
                        matriz_cinza[y+dy][x+dx] = (gray, gray, gray)
    return matriz_cinza

def binarizar_manual(matriz_cinza, largura, altura, limiar=128):
    matriz_bin = [[(0, 0, 0) for _ in range(largura)] for _ in range(altura)]
#Aplicado pixel a pixel
    for y in range(altura):
        for x in range(largura):
            gray = matriz_cinza[y][x][0]  # R == G == B
            bin_value = 255 if gray >= limiar else 0
            matriz_bin[y][x] = (bin_value, bin_value, bin_value)

    return matriz_bin

def salvar_matriz_como_imagem(matriz, caminho_saida):
    altura = len(matriz)
    largura = len(matriz[0])
    nova_img = Image.new("RGB", (largura, altura))

    for y in range(altura):
        for x in range(largura):
            nova_img.putpixel((x, y), matriz[y][x])

    nova_img.save(caminho_saida)
    print(f"Imagem salva em: {caminho_saida}")

def processar_imagem_em_blocos(caminho_imagem):
    img = Image.open(caminho_imagem).convert('RGB')
    largura, altura = img.size
    matriz_rgb = imagem_para_matriz(img)

    # Cinza (com varredura 5x5 percorrendo pixel a pixel)
    matriz_cinza = converter_cinza_manual(matriz_rgb, largura, altura)
    salvar_matriz_como_imagem(matriz_cinza, caminho_imagem+"_Cinza.png")

    # Binarização
    matriz_bin = binarizar_manual(matriz_cinza, largura, altura, limiar=128)
    salvar_matriz_como_imagem(matriz_bin, caminho_imagem+"_Binaria.png")

# Executar
processar_imagem_em_blocos("foto.png")  # substitua pelo nome da sua imagem
