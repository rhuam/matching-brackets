# -*- coding: utf-8 -*-

#####
# Processor: Essa classe eh responsavel por analisar as entradas e verificar se os parentese, chaves e colchetes
# estao balanceados.
# O metodo principal eh o findErro() que procura apenas pelos erros mais simples, otimizando o desempenho
# caso exista. Caso contrario, o metodo replaceAll() remove de forma interativa todos os pares balanceados,
# se ao final de sua execucao a string nao for vazia, significa que exite uma desbalanceamento.
# Por fim a classe viewText() eh usada apenas para gerar a string de impressao na view, marcando o elemento
# desbalanceado.
#####

class Processor():
    def __init__(self, value):
       self.value = value
       
       
    def viewText(self, i=None):
        if (i == -1):
            return "Balanceado", "<span style='color: green'>" + self.value + "</span>", "Essa entrada atende a todas restri&ccedil;&otilde;es."
        elif(i == len(self.value)):
            return "N&atilde;o Balanceado", "<span style='color: red'>" + self.value + "</span>", "H&aacute; um problema de balanceamento nessa entrada."
        else:
            text = self.value
            text = "N&atilde;o Balanceado", text[:i] + "<span style='color: red'>" + text[i] + "</span>" + text[i+1:], "H&aacute; um problema de balanceamento com o caracter '"+text[i]+"' nessa entrada."
            return text
        
    def replaceAll(self):
        open_close = "()", "[]", "{}"
    
        bValue = self.value
        condition = True
        
        while (condition):
            aValue = bValue
            for oc in open_close:
                bValue = bValue.replace(oc, "")
            condition = not(aValue == bValue)
        if len(bValue) == 0:
            return self.viewText(-1)
        else:
            return self.viewText(len(self.value))
     
    def findErro(self):
        erros = "(]", "(}", "[)", "[}", "{)", "{]", 
        
        for op in ")]}":
            if (self.value[0] == op):
                return self.viewText(0)
        
        for op in "([{":
            if (self.value[-1] == op):
                return self.viewText(len(self.value)-1)
        
        for op in erros:
            f = self.value.find(op)
            if (f != -1):
                return self.viewText(f)
        
        return self.replaceAll()