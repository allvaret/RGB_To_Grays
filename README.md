# Redução de dimensionalidade
## 🖼️ Conversor e Manipulador de Imagens com Python Puro (PPM - P3)

Este repositório contém três implementações didáticas e manuais, feitas em **Python puro**, para manipulação de imagens em baixo nível — **sem uso de bibliotecas externas** como Pillow, OpenCV ou Numpy.

Todos os códigos trabalham com o formato **PPM - P3 (Portable Pixmap - ASCII)**, ideal para fins educacionais por sua estrutura simples e aberta.

---

## 📁 Estrutura do Projeto

- `01_converter_jpg_para_p3.py`  
  Converte uma imagem `.jpg` ou `.png` para o formato `.ppm` (P3), com base em pixels RGB.  
  ⚠️ Usa **Pillow apenas para leitura**, o restante é construído manualmente.

- `02_transformar_por_matriz.py`  
  Varre diretamente qualquer imagem comum (.jpg, .png, etc) usando Pillow, convertendo os pixels em tons de cinza ou binarização por meio de varredura por blocos (ex: 5x5).
✅ Não requer conversão para .ppm.

- `03_converter_para_cinza.py`  
  Converte a imagem `.ppm` para tons de cinza utilizando uma **abordagem vetorial com multiplicação e bias**, simulando o comportamento de neurônios artificiais (uma introdução à ideia de redes neurais).

---

## 📌 Pré-requisitos

- Python 3.6 ou superior
- Biblioteca Pillow apenas para `01_converter_jpg_para_p3.py`

Instale com:

```bash
pip install pillow
```
---

## 🧪 Exemplos de Uso

Aqui estão exemplos práticos de como executar os scripts disponíveis neste repositório:

###  1. Converter imagem .JPG para .PPM (formato texto P3)

```python
from converter_jpg_para_p3 import converter_para_ppm_p3

converter_para_ppm_p3("foto.jpg", "imagem.ppm")
```
### Aplicar transformação por matriz (blocos 5x5)
```python
from transformar_por_matriz import processar_imagem_em_blocos

processar_imagem_em_blocos("foto.jpg")
# Gera: imagem_cinza_bloco.png e imagem_binaria_bloco.png
```
### Converter para cinza com pesos e bias (modo vetorial)

Este código converte uma imagem `.ppm` (P3) para tons de cinza e depois para imagem binária (preto e branco) com limiar.
```python
from converter_para_cinza import executar_transformacoes

executar_transformacoes("imagem.ppm")

```
---

## ✍️ Autor
- Desenvolvido por Alvaro Danko
- Contato: alvarodanko032@gmail.com
- LinkedIn: (https://www.linkedin.com/in/alvaro-danko-119229231/)
