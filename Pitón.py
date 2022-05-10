from operator import indexOf
from select import kevent
import runpy



builtin_functions={"cualquier":"any","todo":"all","metodoclase":"classmethod","compilar":"compile","dicc":"dict","elimatr":"delattr","enumerar":"enumerate","ejec":"exec","filtro":"filter","ayuda":"help","entrada":"input","larg":"len","lista":"list","mapa":"map","objecto":"object","revertido":"reversed","redondear":"round","partir":"slice","ordenado":"sorted","metodoestatico":"staticmethod","suma":"sum","tipo":"type","imprimir":"print"}
keywords={"y":"and","o":"or","afirmar":"assert","romper":"break","classe":"class","continuar":"continue","elim":"del","ysi":"elif","si":"if","demas":"else","excepto":"except","Falso":"False","desde":"from","importar":"import","en":"in","es":"is","Nada":"None","no":"not","pasar":"pass","retornar":"return","elevar":"raise","Verdadero":"True","intentar":"try","mientras":"while","con":"with","para":"for"}


def inside_something(item,keyword,charac,charac_close):
    index_open=charac
    index_close = charac_close
    keep_string=item[index_open:index_close+1]
    new_word=item[:index_open].replace(keyword,builtin_functions[keyword])+keep_string+item[index_close+1:].replace(keyword,builtin_functions[keyword])
    return new_word

def kill_comments(sentence):
    if "#" in sentence:
        index_open=sentence.find("'")
        index_close = sentence.rfind("'")
        if sentence.find('#')<index_open or sentence.find('#')>index_close:
            sentence=sentence[:sentence.find('#')]
            

    return sentence

    

        

# Using readlines()
file1 = open('spanish.txt', 'r')
Lines = file1.readlines()
file2 = open('translatedPy.txt', 'w')
file3 = open('translatedPy.txt', 'a')
file2.write("")
 

# Strips the newline character
for line in Lines:
    line=kill_comments(line)
    words=line.split(" ")
    for i in range(len(words)):
        if words[i] in keywords:
            words[i]=keywords[words[i]]
    line=' '.join([str(elem) for elem in words])
    words=line.split(" ")
    for i in range(len(words)):
        
        if "(" in words[i] and ")" in words[i]:
            if "'" in words[i]:
                str_index=words[i].find("'")
                str_index_c=words[i].rfind("'")
                if str_index>words[i].find("("):
                    bltin_func=words[i][:str_index-1]
                    if bltin_func in builtin_functions:
                        words[i]=inside_something(words[i],bltin_func,str_index,str_index_c)
            else:
                str_index=words[i].find("(")
                str_index_c=words[i].find("(")
                bltin_func=words[i][:str_index]
                
                words[i]=inside_something(words[i],bltin_func,str_index,str_index_c)
                if words[i].count("(")>1:
                    str_index=words[i].find("(")
                    str_index_subfunction=words[i].find("(",str_index+1)
                    str_index_subfunction_c=words[i].find(")",str_index_subfunction+1)
                    bltin_func=words[i][str_index+1:str_index_subfunction]
                    words[i]=inside_something(words[i],bltin_func,str_index_subfunction,str_index_subfunction_c)

    
    line=' '.join([str(elem) for elem in words])
    line_list=list(line)
    have_function=False
    for i in reversed(range(len(line_list))):
        if line_list[i]=="(":
            have_function=True
            index_par=i
        if have_function==True:
            if line_list[i]==" ":
                prob_bltin_func=line[i+1:index_par]
                if prob_bltin_func in builtin_functions:
                    str_index_c=line.find(")")
                    line=inside_something(line,prob_bltin_func,index_par,str_index_c)
                break
            elif i==0:
                prob_bltin_func=line[i:index_par]
                if prob_bltin_func in builtin_functions:
                    str_index_c=line.find(")")
                    line=inside_something(line,prob_bltin_func,index_par,str_index_c)
    file2.write(line+"\n")
    
file2.close()
file3.close()
        

                
runpy.run_path(path_name='translatedPy.txt')
        

            
            




        







        


    
    
    
