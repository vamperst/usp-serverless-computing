# Aula 02.1 - Lambda


1. No terminal do IDE criado no cloud9 execute o comando `cd ~/environment/usp-serverless-computing/03-Lambda/01-intro` para entrar na pasta que fara este exercicio.
2. Iniciar o repositório de trabalho `sls create --template "aws-python3"`
 
  ![img/slscreate.png](img/slscreate.png)

3. Abra o arquivo serverless.yml no IDE com o comando `c9 open serverless.yml`
4. Altere o arquivo para que fique como na imagem abaixo. Para salvar utilize CTRL+S.
   
   ![](img/yml1.png)

5. No terminal do IDE faça deploy da função criada com o comando `sls deploy --verbose`. Esse comando vai mostrar cada etapa sendo feita em detalhes, bem como o status do cloudformation criado.
 
  ![img/slsdeploy.png](img/slsdeploy.png)

7. Testar remotamente a função `sls invoke -f hello`

  ![img/slsinvoke.png](img/slsinvoke.png)

8. Execute o comando `c9 open handler.py` e altere a versão do retorno da função para 1.1 no arquivo "handler.py" como na imagem e salve com as teclas "CTRL + S"
  ![img/altereversao.png](img/altereversao.png)
9.  Faça um teste local da sua função no terminal com o comando `sls invoke local -f hello` 
  ![img/slsinvokelocal.png](img/slsinvokelocal.png)
10.    Para deletar a função que esta no lambda utilize o comando `sls remove`
  ![img/slsremove.png](img/slsremove.png)
