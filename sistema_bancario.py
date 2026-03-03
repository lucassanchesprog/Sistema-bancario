print("Bem vindo ao banco Python!")

nome = input("Por gentileza, me informe seu nome: ")

print("Bem vindo ao nosso banco,", nome, "!")

atual = float(input("Qual seu saldo atual? "))

print("Ok, vemos que você tem na sua conta", atual, "reais.")

saldo = float(input("Quanto você quer depositar na sua conta? "))

total = atual + saldo

print("Você agora tem R$", total, "na sua conta.")

menos = float(input("Quanto você quer tirar da sua conta? "))

retirar = total - menos

print("Agora você está com R$", retirar, "reais na sua conta!")

print("Cliente:", nome)
print("Saldo final: R$", retirar)

print("Obrigado por usar o banco Python!")