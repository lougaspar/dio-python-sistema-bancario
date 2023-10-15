menu = """\n
================ MENU ================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[q]\tSair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == 'd':
    valor = float(input("Insira valor de depósito: "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
      print("Operação falhou! Valor inválido: ") 
  
  elif opcao == 's':
    valor = float(input("Insira valor de saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Saldo insuficiente.")

    elif excedeu_limite:
      print("Valor de saque excede o limite")
    
    elif excedeu_saques:
      print("Excedeu o limite de saques.")

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1
    
    else:
      print("Valor inválido")

  elif opcao == 'e':
    print("\n============= EXTRATO ==============")
    print("Sem movimentos realizados" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======================================")

  elif opcao == 'q':
    break
  
  else:
    print("Operação inválida, selecione novamente a operação desejada")
