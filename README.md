# Brain-Cleaner

* Compilador que gera um código BF baseado em um script de Brain Cleaner

* Última versão estável (main):  INDEV-0.1.3-0

## O que é o Brain Cleaner?

Brain Cleaner é uma linguagem de programação que pode ter o seu código compilado para a famosa linguagem esotérica BF.

O Brain Cleaner busca ser um meio de facilitar a geração de código BF, permitindo complementar com facilidades o desenvolvimento de códigos BF e, indo além, até permitir desenvolver com uma linguagem de médio/alto nível, buscando o limite do BF

## Como usar o compilador?

Para desenvolver com Brain Cleaner, Escreva o seu código no arquivo "code.bc"; após isso, execute o "main.py", isso resultará na atualização do arquivo "main.bf" que será executado pelo [interpretador de BF](https://github.com/Jose-Edu/BF-Interpreter-CS). Não mova ou remova o arquivo "main.bf", caso queira usá-lo em outro lugar, o copie e cole no destino.

## Sintaxe da linguagem

* Todos os blocos em Brain Cleaner possuem a seguinte base:
  * |nome do comando|: ( |parâmetro 1|, |parâmetro 2|, ...) {|bloco de código|};
  * Exemplo: repeat:(5){Write:("Hello World!")};
* Em Brain Cleaner, todos os espaços em branco e quebras de linhas são ignorados (quando fora de uma string);
* Todos os segmentos devem ser encerados com ponto e vírgula (;);
* Para escrever comentários, usamos /**/. Exemplo:
  * Write:("Text"); /* Escrevendo "Text" na tela */

## Comandos da linguagem

A linguagem Brain Cleaner está no início do seu desenvolvimento, portanto, ainda possui pouca estrutura, possuindo apenas 7 comandos, sendo eles:

* bf:{...}
  * Bloco especial de código, lhe permite escrever diretamente em BF;
  * Permite o uso de macros de repetição no meio do código como: (+5) = +++++ ou (<3) = <<<
  * Exemplo: bf:{(+20)>(+61)<.>.};
* repeat:(num){...}
  * Repete um bloco de código x vezes.
  * Exemplo: repeat:(5) {Write("Escrevendo 5 vezes... ")};
* Write:(string, quebrarLinha)
  * Escreve um texto na tela;
  * Exemplo: Write:("Hello World!", true);
* FindNext:(val)
  * Move o ponteiro até a próxima incidência de um valor x na memória;
  * Exemplo: FindNext:(255);
* FindLast:(val)
  * Move o ponteiro até a incidência anterior de um valor x na memória;
  * Exemplo: FindLast:(255);
* Input:(text)
  * Recebe uma string e a armazena no bloco atual de memória;
  * Essa função possui um parâmetro opcional, no qual lhe permite escrever um texto para o input;
  * Exemplo: Input:("Digite um texto: ");
  * Exemplo: Input:();
* MoveBlocks(blocksNum)
  * Se move por x blocos na memória. Use números positivos para avançar na memória e números negativos para voltar;
  * Exemplo: MoveBlocks(3);
  * Exemplo: MoveBlocks(-2);
