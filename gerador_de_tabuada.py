contador = 0
limite = int(input('multiplicar quantas vezes:')) + 1 # +1 por causa do range, pois ele se inicia no 0 e assim por diiante, experimente sem o +1 
multiplicador = int(input('multiplicador:'))


# tabuada de qualquer número quantas vezes quiser 
if contador <= limite:
    for contador in range(1,limite):# range(1,limite) - '1' é o start onde começa e 'limite' é o stop onde vai parar
        print( str(multiplicador),'x', contador, '=', contador*multiplicador)





  


