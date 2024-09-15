print ("Bem vindo ao quiz mais grunge de todos.")
print ("Está pronto para testar os seus conhecimentos?")
inic=input ("S/N?   ")
if inic!= "S":
    quit("Quiz encerrado")
pont = 0


## pergunta 1

print ("Começando!!!")
print ("Qual banda conhecida por lançar a música Dirt?\n (A)Pear Jan\n (B)Nirvana\n (C)Alice in Chains\n (D)Soundgarden\n")
resp_1 = input ("Resposta:  ")
if resp_1 == "C":
    print ("Correto")
    pont = pont + 1
else: print ("Errado")
##Pergunta 2
print ("Próxima!!")
print ("Qual o nome do vocalista da banda Soundgarden?\n (A)Chris Cornell\n (B)Eddie Veder\n (C)Kurt Cobain\n (D)Layne Staley\n")
resp_2 =input ("Resposta: ")
pont = pont + 1
if resp_2 == "A":
    print ("Correto, Muito bom!")
else: print ("Errou feio")
##pergunta 3
print ("Em que ano o vocalista da banda Nirvana se matou?\n (A)1987\n (B)1991\n (C)1994\n (D)1998\n")
resp_3=input ("Resposta: ")
if resp_3 == "C":
    print ("Ai sim, você acertou")
    pont = pont + 1
else: print ("Errado") 
##Pergunta 4
print ("Qual banda ficou famosa por criar o álbum superunknown\n (A)Alice in Chains\n (B)Nirvana\n (C)Pear Jan\n (D)Soundgarden\n")
resp_4 = input ("Resposta: ")
if resp_4 == "D":
    print ("Exato")
    pont = pont + 1
else: print ("Errado")
print ("Chegamos ao fim do nosso Quiz Grunge")    
print ("Parabéns em chegar até aqui!")
print ("Vamos para a pontuação....")
print (f"Sua pontuação foi: {pont}/4")



 