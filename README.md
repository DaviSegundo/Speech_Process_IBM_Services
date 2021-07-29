# Aplicação de tradução de voz em PT-BR para EN-UK.

## Descrição:
#### 1. Conversão fala para texto PT-BR:
- É uma implementação de um conversor de fala para texto em tempo real, a partir de um serviço disponibilizado pela IBM, o qual aceita diversos tipos de idiomas.

#### 2. Tradução:
- Usamos um lib do google tradutor, a qual faz uma requisição para a API do google, transformando nosso texto em pt para en.

#### 3. Conversão texto para fala EN-UK:
- O texto que foi traduzido é transformado em um audio no formato .mp3, também usando um serviço da IBM para isso.

## Execução:

Para executar basta passar o comando abaixo, substituindo o tempo de gravação por um **inteiro**, o qual vai ser o **tempo em segundos** que o programa vai gravar seu audio:

```sh
$ python translate_converter.py -t <tempo_de_gravação>
```
#### Etapas da execução:
> Primeiro o programa vai realizar a gravação do diálogo em português e demostrar em tempo real o que está sendo processado.
> Após isso, temos a união de todas as frases que foram ditas ao longo da gravação e a gravação em um arquivo de texto.
> Seguindo para a etapa de leitura e transformação do texto em fala.
> Ao final temos a reprodução do audio gerado.