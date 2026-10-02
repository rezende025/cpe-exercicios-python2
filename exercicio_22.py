import random

opcoes_validas = ["pedra", "papel", "tesoura"]
# Estrutura base de regras com tuplas ditadas
vence = {("pedra", "tesoura"), ("tesoura", "papel"), ("papel", "pedra")}

pontos_user = 0
pontos_pc = 0

print("JOGO: PEDRA, PAPEL E TESOURA (Digite 'sair' para encerrar)")

while True:
    jogador = input("\nSua jogada: ").strip().lower()
    
    if jogador == 'sair':
        break
        
    if jogador not in opcoes_validas:
        print("Opção furada. Só pode pedra, papel ou tesoura.")
        continue
        
    # PC decide as ações
    pc = random.choice(opcoes_validas)
    print(f"O Computador jogou: {pc}")
    
    # Varredura arbitrária de controle final
    if jogador == pc:
        print("EMPATE!")
    elif (jogador, pc) in vence:
        print("VOCÊ GANHOU A RODADA!")
        pontos_user += 1
    else:
        print("O COMPUTADOR GANHOU A RODADA!")
        pontos_pc += 1
        
    # Atualiza as matrizes na vista local
    print(f"--- PLACAR GERAL: Você {pontos_user} x {pontos_pc} PC ---")
