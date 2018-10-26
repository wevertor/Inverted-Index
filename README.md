[![GitHub stars](https://img.shields.io/github/stars/wevertor/Inverted-Index.svg)](https://github.com/wevertor/Inverted-Index/stargazers)
# Inverted Index

Uma estrutura de dados muito utilizada em motores de busca de texto. É capaz de armazenar as ocorrências de cada palavra em múltiplos arquivos e retornar o arquivo mais relevante dada uma busca feita por n palavras.

Por exemplo, dada a seguinte lista de documentos:
  ~~~
  1: "Sei que sou"
  2: "Sou o que sei"
  3: "Sou uma banana"
  ~~~
Obtemos a seguinte lista invertida:
  ~~~
  "sei" : {1, 2}
  "que" : {1, 2}
  "sou" : {1, 2, 3}
  "o" : {2}
  "uma" : {3}
  "banana" : {3}
  ~~~
