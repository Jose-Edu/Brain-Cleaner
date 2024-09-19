# Brain-Cleaner

* Compilador que gera um código BF baseado em um script de Brain Cleaner
* Versão Mais recente:  INDEV-0.1.0-0
* Ultima versão estável: INDEV-0.1.0-0

## O que é o Brain Cleaner?

Brain Cleaner é uma linguagem de programação que pode ter o seu código compilado para a famosa linguagem esotérica BF.

O Brain Cleaner busca ser um meio de facilitar a geração de código BF, permitindo complementar com facilidades o desenvolvimento de códigos BF e, indo além, até permitir desenvolver com uma linguagem de médio/alto nível, buscando o limite do BF

## Como usar o compilador?

Para desenvolver com Brain Cleaner, Escreva o seu código no arquivo "code.bc"; após isso, execute o "main.py", isso resultará na atualização do arquivo "main.bf", localizado na pasta "output". Não mova ou remova o arquivo "main.bf", caso queira usá-lo em outro lugar, o copie e cole no destino.

## Sintaxe da linguagem

* Todos os blocos em Brain Cleaner possuem a seguinte base:
  * |nome do comando|: ( |parâmetro 1|, |parâmetro 2|, ...) {|bloco de código|};
  * Exemplo: repeat:(5){Write:("Hello World!")};
* Em Brain Cleaner, todos os espaços em branco e quebras de linhas são ignorados (quando fora de uma string);
* Todos os segmentos devem ser encerados com ponto e vírgula (;);
* Para escrever comentários, usamos /**/. Exemplo:
  * Write:("Text"); /* Escrevendo "Text" na tela */

## Comandos da linguagem

A linguagem Brain Cleaner está no início do seu desenvolvimento, portanto, ainda possui pouca estrutura, possuindo apenas 3 comandos, sendo eles:

* bf:
  * Bloco especial de código, lhe permite escrever diretamente em BF;
  * Permite o uso de macros de repetição no meio do código como: (+5) = +++++ ou (<3) = <<<
  * Exemplo: bf:{(+20)>(+61)<.>.};
* repeat(num):
  * Cria um laço que se repete x vezes.
  * Exemplo: repeat:(5) {Write("Escrevendo 5 vezes... ")};
* Write(string):
  * Escreve um texto na tela;
  * Exemplo: Write:("Hello World!");
