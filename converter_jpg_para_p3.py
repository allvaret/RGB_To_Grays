from PIL import Image

def converter_para_ppm_p3(imagem_entrada, imagem_saida):
    img = Image.open(imagem_entrada).convert('RGB')
    largura, altura = img.size

    pixels = list(img.getdata())  # pega todos os pixels como (R, G, B)

    with open(imagem_saida, 'w') as f:
        f.write("P3\n")
        f.write(f"{largura} {altura}\n")
        f.write("255\n")  # valor máximo por canal

        for i in range(altura):
            for j in range(largura):
                r, g, b = pixels[i * largura + j]
                f.write(f"{r} {g} {b} ")
            f.write("\n")  # quebra de linha por linha de pixels

    print(f"Imagem convertida para PPM (P3) com sucesso: {imagem_saida}")

converter_para_ppm_p3("imagem.jpg", "imagem_convertida.ppm")
