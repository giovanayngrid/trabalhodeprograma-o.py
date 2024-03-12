tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link_mbps = float(input("Digite a velocidade do link de internet (em Mbps): "))
velocidade_link_mbps = velocidade_link_mbps / 8
tempo_download_segundos = tamanho_arquivo_mb / velocidade_link_mbps
tempo_download_minutos = tempo_download_segundos / 60
print(f"Tempo de download aproximado: {tempo_download_minutos:.2f} minutos")
