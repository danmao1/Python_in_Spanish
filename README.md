# Python_in_Spanish
### Description:
The program parses every line of code and changes the built-in function and keywords from spanish to english. After translating the language, you should be able to run the code in spanish. What the code does is that it takes a python script in spanish, read it line by line and changes the keywords and builtin functions to english and writes the translated line into another txt file. After all the lines are translated, the program runs the english scripts in the txt file. You can check the regular python script in translatedPy.txt to check the code that was translated.
### About the grammar:
As the program read the scripts from a txt file. The lines that read are already a string with " in between them and that is why my parser only parses strings between the ' character.


The program should be able to distinguish between a built-in function/keyword and a string that has the same characters as the built-in function/keyword.

For, example: imprimir('imprimir') should translate to only the built-in funciton outside the string -> print('imprimir')


 or 
 
 
 para i en lista('imprimir'): -> for i in list('imprimir'):
 
 
 Another feature is that the program should be able to know if the line has a comment or not to ignore, For example:
 
 
 imprimir('Hello World') #comment, we should ignore the comment but imprimir('#Hello World') we should not ignore it.
 
 
 Moreover, the code should be able to see if there is another built-in function inside of another built-in function. For example,
 
 
 a=3.14
 
 
 imprimir(redondear(a)) -> print(round(a))
 ### Built-in functions:
 cualquier => any

todo => all

metodoclase => classmethod

compilar => compile

dicc => dict

elimatr => delattr

enumerar => enumerate

ejec => exec

filtro => filter

ayuda => help

entrada => input

larg => len

lista => list

mapa => map

objecto => object

revertido => reversed

redondear => round

partir => slice

ordenado => sorted

metodoestatico => staticmethod

suma => sum

tipo => type

imprimir => print

### Keywords:

Falso => False

desde => from

importar => import

en => in

es => is

Mada => None

no => not

pasar => pass

retornar => return

elevar => raise

Verdadero => True

intentar => try

mientras => while

con => with

para => for
 
### How to run the program:
The instructions below assume that python3 and pip3 refer to Python 3.x and Pip 3.x. Depending on how things are configured, you may need to use python and pip commands instead of python3 and pip3.
1. Create a virtual environment: python3 -m venv venv
2. Activate virtual environment:
    Mac or Linux: source venv/bin/activate
    Windows: source venv/Scripts/activate
3. Install dependencies: pip3 install -r requirements.txt
4. export PYTHONPATH=$(pwd)
5. python3 Pitón.py 
// If you want to run your own tests you can paste your spanish python script on the spanish.txt file
